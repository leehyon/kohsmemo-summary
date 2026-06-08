import argparse
import json
import logging
import os
import re
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from functools import wraps
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple, Set
from urllib.parse import quote

# Optional dependency: enables more robust Markdown parsing when present. Falls back
# to a regex-based parser when unavailable so backfill/dry-run still work without it.
try:
    import mistune
except ImportError:  # pragma: no cover - fallback when optional dependency missing
    mistune = None  # type: ignore[assignment]

# Required for network operations (fetching article content via Jina reader and
# calling OpenAI). Backfill mode can run without it because no new content is fetched.
try:
    import requests
except ImportError:  # pragma: no cover - fallback when optional dependency missing
    requests = None  # type: ignore[assignment]

# -- exception hierarchy begin --
# Phase A: replaces the ad-hoc `raise Exception(...)` pattern that previously
# let any failure (404, 5xx, missing API key) kill the whole CI run with the
# same generic traceback. Callers (`ingest_bookmark` / `process_changes`) now
# branch on the subclass to decide soft-fail-with-stub vs hard-fail.
class IngestionError(Exception):
    """Base class for all bookmark-ingestion failures."""


class ContentUnavailableError(IngestionError):
    """Origin / mirror reports the resource no longer exists (404, 410, or a
    persistent non-retryable 4xx). Soft-fail: write a stub summary, mark the
    entry failed, continue the run."""


class FetchTransientError(IngestionError):
    """Network / HTTP failure that may resolve on retry (5xx, 429 from
    upstream mirror). After retries are exhausted the caller treats this as
    soft-fail with a stub."""


class LLMError(IngestionError):
    """OpenAI request failed in a way that means the setup or model is broken
    (4xx other than 429, missing `choices`, etc.). Hard-fail: surface to CI."""


class LLMRateLimitError(LLMError):
    """Specifically 429 from the LLM provider. Retried; if it persists,
    treated as soft-fail with stub so a temporary quota blip doesn't kill
    the whole pipeline."""


class ConfigError(IngestionError):
    """Local environment is broken (e.g. OPENAI_API_KEY missing). Hard-fail
    with a clear message — retrying won't help and the run is meaningless
    without the missing input."""
# -- exception hierarchy end --

# -- configurations begin --
MEMO_REPO_NAME: str = "kohsmemo"
SUMMARY_REPO_NAME: str = "kohsmemo-summary"
MAX_CONTENT_LENGTH: int = 32 * 1024  # 32KB
MIN_CONTENT_LENGTH: int = 200  # Minimum content length to consider valid
MAX_RETRIES: int = 3  # Maximum retry attempts for fetching content
NO_SUMMARY_TAG: str = "#nosummary"
TOMBSTONE_TAG: str = "tombstone"  # marker tag (without '#') that triggers summary deletion
HTTP_CONNECT_TIMEOUT_SECONDS: int = 5
HTTP_READ_TIMEOUT_SECONDS: int = 30
# -- configurations end --

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info("Entering %s", func.__name__)
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        logging.info(
            "Exiting %s - Elapsed time: %.4f seconds", func.__name__, elapsed_time
        )
        return result

    return wrapper


@dataclass
class SummarizedBookmark:
    month: str  # yyyyMM
    title: str
    url: str
    timestamp: int  # unix timestamp
    tags: List[str] = field(default_factory=list)
    # Phase A: True for entries where ingestion failed (404 / persistent 5xx /
    # network). The summary .md file is a stub, but the entry is still recorded
    # in data.json so a future run can retry. Defaults to False for backward
    # compatibility with existing data.json files (asdict will not include
    # `failed` in old entries — see `load_summarized_bookmarks`).
    failed: bool = False


@dataclass
class IngestionResult:
    bookmark: SummarizedBookmark
    summary_markdown: str
    summary_path: Path
    one_sentence: str
    # When True, summary_markdown is a stub and the caller should mark the
    # bookmark failed but still proceed (soft-fail path).
    failed: bool = False


CURRENT_MONTH: str = datetime.now(timezone.utc).strftime("%Y%m")
CURRENT_DATE: str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
CURRENT_DATE_AND_TIME: str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

SUMMARY_ROOT = Path(SUMMARY_REPO_NAME)
if not SUMMARY_ROOT.exists():
    SUMMARY_ROOT = Path(".")

DATA_PATH = SUMMARY_ROOT / "data.json"
SUMMARY_README_PATH = SUMMARY_ROOT / "README.md"

COLLECTION_ROOT = Path(MEMO_REPO_NAME)
COLLECTION_README_PATH = COLLECTION_ROOT / "README.md"


def ensure_directory(path: Path, dry_run: bool = False) -> None:
    if dry_run:
        logging.info("Dry-run: would ensure directory %s", path)
        return
    path.mkdir(parents=True, exist_ok=True)


def format_month(month: str) -> str:
    try:
        return datetime.strptime(month, "%Y%m").strftime("%Y-%m")
    except ValueError:
        return month


def normalize_tag(tag: str) -> str:
    return tag if tag.startswith("#") else f"#{tag}"


def format_tags(tags: Iterable[str]) -> str:
    return " ".join(normalize_tag(tag.strip()) for tag in tags if tag.strip())


def bookmark_identity(bookmark: SummarizedBookmark) -> Tuple[str, str, int]:
    return (bookmark.month, bookmark.title, bookmark.timestamp)


def write_text_file(path: Path, content: str, dry_run: bool = False) -> None:
    if dry_run:
        logging.info(
            "Dry-run: would write %s (%d bytes)", path, len(content.encode("utf-8"))
        )
        return
    ensure_directory(path.parent, dry_run=False)
    with path.open("w", encoding="utf-8") as handle:
        handle.write(content)


def load_summarized_bookmarks() -> List[SummarizedBookmark]:
    if not DATA_PATH.exists():
        logging.info(
            "No data.json found at %s, starting with empty dataset.", DATA_PATH
        )
        return []

    with DATA_PATH.open("r", encoding="utf-8") as handle:
        raw_entries = json.load(handle)

    bookmarks: List[SummarizedBookmark] = []
    for entry in raw_entries:
        tags = entry.get("tags") or []
        # `failed` is a Phase A addition; older data.json files won't have it.
        # The dataclass default is False, so we don't need to special-case
        # missing keys — but we accept the key explicitly for forward
        # compatibility with files written by this version.
        bookmarks.append(
            SummarizedBookmark(
                month=entry["month"],
                title=entry["title"],
                url=entry["url"],
                timestamp=entry["timestamp"],
                tags=tags,
                failed=entry.get("failed", False),
            )
        )
    return bookmarks


def save_summarized_bookmarks(
    bookmarks: Iterable[SummarizedBookmark], dry_run: bool = False
) -> None:
    payload = [asdict(bookmark) for bookmark in bookmarks]
    if dry_run:
        logging.info(
            "Dry-run: would write %s with %d entries.", DATA_PATH, len(payload)
        )
        return

    ensure_directory(DATA_PATH.parent, dry_run=False)
    with DATA_PATH.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)


def read_bookmark_collection_lines() -> List[str]:
    if not COLLECTION_README_PATH.exists():
        logging.warning(
            "'%s' not found; skipping new bookmark ingestion.",
            COLLECTION_README_PATH,
        )
        return []

    with COLLECTION_README_PATH.open("r", encoding="utf-8") as handle:
        return handle.readlines()


def extract_tags_from_line(line: str) -> List[str]:
    closing_paren_index = line.find(")")
    if closing_paren_index == -1:
        return []
    trailing = line[closing_paren_index + 1 :]
    raw_tags = re.findall(r"#([^\s#]+)", trailing)

    tags: List[str] = []
    nosummary = NO_SUMMARY_TAG.lstrip("#")
    for raw_tag in raw_tags:
        cleaned = raw_tag.strip().rstrip(",.;:!?")
        if not cleaned or cleaned == nosummary:
            continue
        tags.append(cleaned)
    return tags


# Phase C: a single source of truth for parsing a kohsmemo README bookmark
# line. The 3 former parsers (build_url_tag_lookup, _extract_urls_with_tombstone,
# find_next_bookmark_to_process) all matched the same pattern, so we centralize
# the regex here.
_BOOKMARK_LINE_RE = re.compile(r"-\s*\[(.*?)\]\((.*?)\)")


@dataclass
class BookmarkEntry:
    """One URL discovered in the source README, after collapsing all
    duplicate rows.

    Attributes:
        title: Title from the first row that mentions this URL.
        url: The URL itself.
        tags: Union of all tags across all rows mentioning this URL, with
            `#nosummary` filtered out. Order is stable: tags appear in
            the order they were first seen across the README.
        has_tombstone: True if any of the rows carries `#tombstone`.
        has_nosummary: True if any of the rows carries `#nosummary`.
        row_count: How many README rows share this URL. Most entries are
            1; >1 means the same URL was added more than once (with
            possibly different tags).
    """

    title: str
    url: str
    tags: List[str]
    has_tombstone: bool
    has_nosummary: bool
    row_count: int


def parse_readme_to_entries(
    bookmark_lines: Iterable[str],
) -> List[BookmarkEntry]:
    """Parse the kohsmemo README into a list of BookmarkEntry, one per
    unique URL, preserving the README's first-seen order.

    Phase C: replaces the 3 places that used to scan the README each
    with their own regex and dedup logic.
    """
    nosummary_lower = NO_SUMMARY_TAG.lstrip("#").lower()

    def _raw_tags(line: str) -> List[str]:
        closing = line.find(")")
        if closing == -1:
            return []
        trailing = line[closing + 1 :]
        return re.findall(r"#([^\s#]+)", trailing)

    # First pass: collect raw + filtered rows in source order, grouped by URL.
    rows_by_url: Dict[str, List[Tuple[str, List[str], List[str]]]] = {}
    first_seen_index: Dict[str, int] = {}
    for line in bookmark_lines:
        match = _BOOKMARK_LINE_RE.search(line)
        if not match:
            continue
        title = match.group(1).strip()
        url = match.group(2).strip()
        raw_tags = _raw_tags(line)
        filtered_tags = extract_tags_from_line(line)
        if url not in rows_by_url:
            first_seen_index[url] = len(rows_by_url)
            rows_by_url[url] = []
        rows_by_url[url].append((title, filtered_tags, raw_tags))

    # Second pass: collapse to BookmarkEntry with union semantics.
    entries: List[BookmarkEntry] = []
    for url, rows in rows_by_url.items():
        # Tags: union in first-seen order, dedup case-insensitively while
        # preserving the first occurrence's original casing. #tombstone is
        # still in filtered_tags (extract_tags_from_line does NOT strip it);
        # #nosummary is not.
        seen_lower: Set[str] = set()
        merged_tags: List[str] = []
        has_tombstone = False
        has_nosummary = False
        for _title, filtered_tags, raw_tags in rows:
            for t in filtered_tags:
                tl = t.lower()
                if tl not in seen_lower:
                    seen_lower.add(tl)
                    merged_tags.append(t)
            if any(rt.lower() == nosummary_lower for rt in raw_tags):
                has_nosummary = True
            if any(rt.lower() == TOMBSTONE_TAG for rt in raw_tags):
                has_tombstone = True

        # Use the first row's title. In practice the title is the same
        # across all rows for a given URL; the README is not edited in a
        # way that retitles a link.
        entries.append(
            BookmarkEntry(
                title=rows[0][0],
                url=url,
                tags=merged_tags,
                has_tombstone=has_tombstone,
                has_nosummary=has_nosummary,
                row_count=len(rows),
            )
        )

    # Restore README source order
    entries.sort(key=lambda e: first_seen_index[e.url])
    return entries


def build_url_tag_lookup(bookmark_lines: Iterable[str]) -> Dict[str, List[str]]:
    """Backward-compatible URL → tags lookup, now built from the unified
    BookmarkEntry list (Phase C). Returns the union of tags for each URL."""
    return {e.url: e.tags for e in parse_readme_to_entries(bookmark_lines)}


def slugify(text: str) -> str:
    invalid_fs_chars: str = '/\\:*?"<>|'
    return re.sub(
        r"[" + re.escape(invalid_fs_chars) + r"\s]+", "-", text.lower()
    ).strip("-")


def get_summary_file_path(
    title: str,
    timestamp: int,
    month: Optional[str] = None,
    in_readme_md: bool = False,
) -> Path:
    date_str = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime("%Y-%m-%d")
    summary_filename: str = f"{date_str}-{slugify(title)}.md"
    if in_readme_md:
        if month is None:
            raise ValueError("Month must be provided when in_readme_md is True")
        root = Path(month)
        summary_filename = f"{date_str}-{quote(slugify(title))}.md"
    else:
        if month is None:
            month = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime("%Y%m")
        root = SUMMARY_ROOT / month
    return root / summary_filename


def build_summary_file(
    title: str,
    url: str,
    summary: str,
    one_sentence: str,
    tags: List[str],
    month: str,
    failed: bool = False,
    failure_reason: str = "",
) -> str:
    tag_line = ""
    if tags:
        tag_line = f"- Tags: {format_tags(tags)}\n"

    if failed:
        # Soft-fail stub. Same file shape as a real summary so that
        # `extract_tldr_from_markdown` (which regexes "## TL;DR" / "## Summary")
        # doesn't choke on it. The body explains the failure and points the
        # reader at the source URL.
        tldr = (
            f"无法生成摘要：{failure_reason}。可在稍后重跑 CI 时再试。"
            if failure_reason
            else "无法生成摘要：上游内容暂时不可用。稍后重跑 CI 时会再试。"
        )
        body = (
            "本条目由 Phase A 软失败路径生成。\n\n"
            f"- 原因：{failure_reason or '上游内容暂时不可用'}\n"
            "- 处理：已写入 data.json（`failed: true`），下次 CI 触发时若该 URL\n"
            "  仍出现在源 README 中，将按原流程重新尝试。\n"
        )
        header_status = " [ingestion failed]"
    else:
        tldr = one_sentence
        body = summary
        header_status = ""

    return (
        f"# {title}{header_status}\n"
        f"- URL: {url}\n"
        f"- Added: {CURRENT_DATE_AND_TIME}\n"
        f"{tag_line}\n"
        f"## TL;DR\n{tldr}\n\n"
        f"## Summary\n{body}\n"
    )


@log_execution_time
def submit_to_wayback_machine(url: str):
    """Best-effort Wayback Machine submission.

    The previous implementation delegated to ``waybackpy.WaybackMachineSaveAPI``,
    whose ``save()`` performs unbounded HTTPS GETs and sleeps between retries
    with no caller-controllable timeout — a single slow response would block
    the whole CI run for many minutes. We call the SavePageNow endpoint
    directly with an explicit timeout and treat any failure as non-fatal.
    """
    if requests is None:
        logging.info(
            "requests not available; skipping Wayback submission for %s.", url
        )
        return

    user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    )
    # waybackpy's save() retries up to 8 times with 5-10s sleeps; we want at
    # most one fast attempt — a longer blocking pattern defeats the purpose
    # of a best-effort side effect.
    save_url = "https://web.archive.org/save/" + url
    try:
        response = requests.get(
            save_url,
            headers={"User-Agent": user_agent},
            timeout=(HTTP_CONNECT_TIMEOUT_SECONDS, 15),
            allow_redirects=True,
        )
    except requests.RequestException as error:
        logging.warning(
            "submit to wayback machine failed (network), skipping, url=%s", url
        )
        logging.debug("Wayback network error: %s", error)
        return

    if response.status_code != 200:
        logging.info(
            "Wayback submission returned HTTP %d, skipping, url=%s",
            response.status_code,
            url,
        )
        return

    content_location = response.headers.get("Content-Location", "")
    match = re.search(r"(/web/\d{14}/.*)", content_location)
    if match:
        wayback_url = "https://web.archive.org" + match.group(1)
        logging.info("Wayback Saved: %s", wayback_url)
    else:
        logging.info("Wayback submission accepted but no archive URL found, url=%s", url)


def normalize_http_url(url: str) -> str:
    url = url.strip()
    if not url:
        raise ValueError("URL is empty")
    if re.match(r"^https?://", url, flags=re.IGNORECASE):
        return url
    return f"https://{url}"


def preflight_check_url(url: str) -> Tuple[Optional[int], Optional[str]]:
    """Best-effort check whether the origin URL is reachable.

    Returns (status_code, error_message). If the request fails before receiving an
    HTTP response, status_code is None and error_message is set.
    """
    if requests is None:
        return None, "requests package not available"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
        )
    }
    timeout = (HTTP_CONNECT_TIMEOUT_SECONDS, HTTP_READ_TIMEOUT_SECONDS)

    try:
        response: requests.Response = requests.head(
            url,
            allow_redirects=True,
            headers=headers,
            timeout=timeout,
        )
        status = response.status_code

        # Some sites block/ignore HEAD; fall back to a lightweight GET.
        if status in (403, 405):
            response = requests.get(
                url,
                allow_redirects=True,
                headers=headers,
                timeout=timeout,
                stream=True,
            )
            status = response.status_code
            response.close()

        return status, None
    except requests.RequestException as error:
        return None, str(error)


@log_execution_time
def get_text_content(url: str) -> str:
    if requests is None:
        raise RuntimeError("requests package not available; cannot fetch content.")

    url = normalize_http_url(url)
    status_code, preflight_error = preflight_check_url(url)
    if preflight_error:
        logging.warning("Preflight check failed for %s: %s", url, preflight_error)
    elif status_code is not None:
        if status_code in (404, 410):
            raise ContentUnavailableError(
                f"Origin URL not found (HTTP {status_code}): {url}"
            )
        if status_code >= 400 and status_code not in (401, 403, 429):
            logging.warning(
                "Origin URL returned HTTP %d for %s; content fetch may fail.",
                status_code,
                url,
            )

    jina_url: str = f"https://r.jina.ai/{url}"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
        )
    }
    timeout = (HTTP_CONNECT_TIMEOUT_SECONDS, HTTP_READ_TIMEOUT_SECONDS)

    for attempt in range(MAX_RETRIES):
        try:
            response: requests.Response = requests.get(
                jina_url,
                headers=headers,
                timeout=timeout,
            )
            if response.status_code >= 400:
                status = response.status_code
                error_msg = f"Jina fetch failed (HTTP {status}) - attempt {attempt + 1}/{MAX_RETRIES}"
                logging.warning(error_msg)

                should_retry = status in (429, 500, 502, 503, 504)
                if should_retry and attempt < MAX_RETRIES - 1:
                    wait_time = 2**attempt
                    logging.info("Retrying in %d seconds...", wait_time)
                    time.sleep(wait_time)
                    continue
                # Retries exhausted. 5xx/429 → transient; everything else
                # means the resource is gone or unreachable in a way that
                # retrying won't fix.
                if status in (429, 500, 502, 503, 504):
                    raise FetchTransientError(
                        f"All {MAX_RETRIES} retry attempts failed. Last error: {error_msg}"
                    )
                raise ContentUnavailableError(
                    f"All {MAX_RETRIES} retry attempts failed. Last error: {error_msg}"
                )

            content = response.text.strip()

            if len(content) < MIN_CONTENT_LENGTH:
                if (
                    "upstream connect error" in content.lower()
                    or "connection termination" in content.lower()
                ):
                    error_msg = f"Connection error detected (attempt {attempt + 1}/{MAX_RETRIES})"
                else:
                    error_msg = (
                        f"Content too short ({len(content)} chars, minimum {MIN_CONTENT_LENGTH}) "
                        f"- attempt {attempt + 1}/{MAX_RETRIES}"
                    )

                logging.warning(error_msg)

                if attempt < MAX_RETRIES - 1:
                    wait_time = 2**attempt
                    logging.info("Retrying in %d seconds...", wait_time)
                    time.sleep(wait_time)
                    continue
                # Short / connection-error content from a mirror is treated
                # as transient: a later CI run may succeed.
                raise FetchTransientError(
                    f"All {MAX_RETRIES} retry attempts failed. Last error: {error_msg}"
                )

            if len(content) > MAX_CONTENT_LENGTH:
                logging.warning(
                    "Content length (%d) exceeds maximum (%d), truncating...",
                    len(content),
                    MAX_CONTENT_LENGTH,
                )
                content = content[:MAX_CONTENT_LENGTH]

            logging.info(
                "Successfully fetched content with %d characters", len(content)
            )
            return content

        except requests.RequestException as error:
            logging.warning(
                "Request failed (attempt %d/%d): %s",
                attempt + 1,
                MAX_RETRIES,
                error,
            )
            if attempt < MAX_RETRIES - 1:
                wait_time = 2**attempt
                logging.info("Retrying in %d seconds...", wait_time)
                time.sleep(wait_time)
            else:
                raise FetchTransientError(
                    f"All {MAX_RETRIES} retry attempts failed. Last error: {error}"
                ) from error


@log_execution_time
def call_openai_api_json(prompt: str, content: str) -> dict:
    """Call OpenAI chat completions in strict JSON mode.

    The response body is parsed as JSON and returned as a dict. Any failure
    to parse (LLM returned prose around the JSON, truncated, or a non-object
    payload) is treated as a hard `LLMError` — we do not retry, because
    re-running with the same input usually produces the same style of
    output. The expectation is that strict prompting + OpenAI's
    `response_format={"type": "json_object"}` mode is enough to keep
    parse failures rare; if they ever become common we can switch to a
    one-shot retry (Phase B follow-up).

    Status-code handling matches the prior `call_openai_api`:
    429 → `LLMRateLimitError` (soft-fail in caller); other non-200 and
    any missing/malformed `choices` → `LLMError` (hard-fail).
    """
    if requests is None:
        raise ConfigError("requests package not available; cannot call OpenAI API.")

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ConfigError(
            "OPENAI_API_KEY is not set. Export it before running the pipeline."
        )

    model: str = os.environ.get("OPENAI_API_MODEL", "gpt-4o-mini")
    headers: dict = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data: dict = {
        "model": model,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": content},
        ],
        # OpenAI's native JSON mode: when set, the model is constrained to
        # emit a JSON object. The system prompt must instruct the model to
        # produce JSON; we do that in `summarize_to_json` below.
        "response_format": {"type": "json_object"},
    }
    api_endpoint: str = os.environ.get(
        "OPENAI_API_ENDPOINT", "https://api.openai.com/v1/chat/completions"
    )

    logging.info("Calling OpenAI API with model: %s", model)
    logging.info("API endpoint: %s", api_endpoint)

    response: requests.Response = requests.post(
        api_endpoint, headers=headers, data=json.dumps(data)
    )

    logging.info("Response status code: %d", response.status_code)
    response_json = response.json()
    logging.debug("Response content: %s", json.dumps(response_json, ensure_ascii=False))

    if response.status_code != 200:
        error_msg = f"OpenAI API request failed with status {response.status_code}"
        logging.error(error_msg)
        logging.error("Error response: %s", response_json)
        if response.status_code == 429:
            raise LLMRateLimitError(error_msg)
        raise LLMError(error_msg)

    if "choices" not in response_json:
        error_msg = "Response does not contain 'choices' field"
        logging.error(error_msg)
        logging.error("Full response: %s", response_json)
        raise LLMError(error_msg)

    raw_content: str = response_json["choices"][0]["message"]["content"]
    try:
        parsed = json.loads(raw_content)
    except (TypeError, ValueError) as err:
        # LLM did not return a valid JSON object. Strict mode contract: this
        # is a hard failure, no fallback to regex extraction.
        snippet = raw_content[:200] if isinstance(raw_content, str) else str(raw_content)
        logging.error("OpenAI response is not valid JSON: %s", snippet)
        raise LLMError(
            f"OpenAI response is not valid JSON: {err}"
        )

    if not isinstance(parsed, dict):
        logging.error(
            "OpenAI JSON response is not an object: type=%s value=%s",
            type(parsed).__name__,
            str(parsed)[:200],
        )
        raise LLMError(
            f"OpenAI JSON response is not an object (got {type(parsed).__name__})"
        )

    return parsed


@dataclass
class SummaryAndTldr:
    """Result of a single combined summarization call (Phase B)."""

    summary: str
    tldr: str


# The combined prompt. It must instruct the model to return a JSON object so
# that OpenAI's `response_format={"type": "json_object"}` mode is satisfied.
# The two former prompts (summarize_text, one_sentence_summary) are fused:
# the model now emits both fields in one round-trip.
_SUMMARIZE_JSON_PROMPT: str = """
你的任务是对一篇文章同时产出「结构化总结」与「TL;DR」两个字段，并以严格的 JSON 对象形式返回，不允许任何额外文本、解释、Markdown 代码块或前后缀。

字段约定：
- "summary"：结构化总结本文，提炼核心主题、关键信息与逻辑脉络，分点呈现且层次清晰。
- "tldr"：对该文章的简短总结，长度不超过 100 个字。

风格要求：
- 输出为简体中文，中英字符间要有空格。
- 直接展示总结内容，无任何前缀、标题及冗余表述。
- 仅输出一个 JSON 对象，键名固定为 "summary" 与 "tldr"。
"""


@log_execution_time
def summarize_to_json(text: str) -> SummaryAndTldr:
    """One-shot summarization: returns both the structured summary and the
    TL;DR in a single OpenAI call. Replaces the two-call sequence
    `summarize_text` + `one_sentence_summary`."""
    parsed = call_openai_api_json(_SUMMARIZE_JSON_PROMPT, text)
    summary = parsed.get("summary")
    tldr = parsed.get("tldr")
    if not isinstance(summary, str) or not isinstance(tldr, str):
        missing = [
            k for k, v in (("summary", summary), ("tldr", tldr)) if not isinstance(v, str)
        ]
        raise LLMError(
            f"OpenAI JSON response is missing/typed-wrong fields: {missing}"
        )
    if not summary.strip() or not tldr.strip():
        raise LLMError(
            "OpenAI JSON response contains empty summary or tldr"
        )
    return SummaryAndTldr(summary=summary, tldr=tldr)


def extract_tldr_from_markdown(file_path: str) -> str:
    def extract_tldr_with_regex(content: str) -> str:
        match = re.search(r"##\s*TL;DR\s+(.*?)\n##\s", content, re.DOTALL)
        if not match:
            match = re.search(r"##\s*TL;DR\s+(.*)", content, re.DOTALL)
        if not match:
            return ""
        extracted = match.group(1).strip()
        return re.sub(r"\s+", " ", extracted)

    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            content = handle.read()
    except Exception as error:  # noqa: BLE001 - tolerate read failures
        logging.warning("Could not read TL;DR from %s: %s", file_path, error)
        return ""

    if not content:
        return ""

    if mistune is None:
        return extract_tldr_with_regex(content)

    try:
        markdown = mistune.create_markdown(renderer=None)
        ast = markdown(content)
    except Exception as error:  # noqa: BLE001 - fallback to regex parser
        logging.warning(
            "Mistune parsing failed for %s: %s. Falling back to regex parser.",
            file_path,
            error,
        )
        return extract_tldr_with_regex(content)

    tldr_content: List[str] = []
    found_tldr = False

    for token in ast:
        if token["type"] == "heading" and token.get("attrs", {}).get("level") == 2:
            if "TL;DR" in str(token.get("children", [])):
                found_tldr = True
                continue
            if found_tldr:
                break
        elif found_tldr and token["type"] == "paragraph":

            def extract_text(children):
                parts: List[str] = []
                for child in children:
                    if child["type"] == "text":
                        parts.append(child["raw"])
                    elif "children" in child:
                        parts.extend(extract_text(child["children"]))
                return parts

            text_parts = extract_text(token.get("children", []))
            tldr_content.append("".join(text_parts))

    if not tldr_content:
        return extract_tldr_with_regex(content)

    return "\n".join(tldr_content).strip()


def render_bookmark_lines(
    bookmark: SummarizedBookmark,
    link: str,
    tldr: str,
) -> List[str]:
    date_str = datetime.fromtimestamp(bookmark.timestamp, tz=timezone.utc).strftime(
        "%Y-%m-%d"
    )
    lines = [f"({date_str}) [{bookmark.title}]({link})"]
    if tldr:
        lines.append(f"- {tldr}")
    if bookmark.tags:
        lines.append(f"- Tags: {format_tags(bookmark.tags)}")
    return lines


def build_monthly_index_markdown(
    month: str,
    bookmarks: List[SummarizedBookmark],
    tldr_lookup: Dict[Tuple[str, str, int], str],
) -> str:
    lines: List[str] = [f"# {format_month(month)} Monthly Index", ""]

    for bookmark in bookmarks:
        link = get_summary_file_path(
            title=bookmark.title,
            timestamp=bookmark.timestamp,
            month=bookmark.month,
            in_readme_md=True,
        ).name
        key = bookmark_identity(bookmark)
        lines.extend(render_bookmark_lines(bookmark, link, tldr_lookup.get(key, "")))
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def build_summary_readme_md(
    summarized_bookmarks: List[SummarizedBookmark],
    grouped_bookmarks: Dict[str, List[SummarizedBookmark]],
    tldr_lookup: Dict[Tuple[str, str, int], str],
) -> str:
    initial_prefix = """# Bookmark Summary 
自动读取 [kohsmemo](https://github.com/leehyon/kohsmemo) 仓库中的书签数据，通过 Jina Reader 获取网页文本内容，再借助大模型生成内容总结。
"""

    lines: List[str] = [initial_prefix.rstrip(), "", "## Latest 10 Entries", ""]

    latest_entries = sorted(
        summarized_bookmarks, key=lambda b: b.timestamp, reverse=True
    )[:10]
    if latest_entries:
        for bookmark in latest_entries:
            link = get_summary_file_path(
                title=bookmark.title,
                timestamp=bookmark.timestamp,
                month=bookmark.month,
                in_readme_md=True,
            ).as_posix()
            key = bookmark_identity(bookmark)
            lines.extend(
                render_bookmark_lines(bookmark, link, tldr_lookup.get(key, ""))
            )
            lines.append("")
    else:
        lines.append("- _No summaries available yet._")
        lines.append("")

    lines.append("## Monthly Archive")
    lines.append("")

    sorted_months = sorted(grouped_bookmarks.keys(), reverse=True)
    if sorted_months:
        for month in sorted_months:
            link = Path(month, "monthly-index.md").as_posix()
            count = len(grouped_bookmarks[month])
            lines.append(f"- [{format_month(month)}]({link}) ({count} entries)")
    else:
        lines.append("- _Archive will appear after the first summary._")

    return "\n".join(lines).strip() + "\n"


def build_all_summary_md(
    summarized_bookmarks: List[SummarizedBookmark],
    tldr_lookup: Dict[Tuple[str, str, int], str],
) -> str:
    lines: List[str] = [
        "# All Summary",
        "",
    ]

    for bookmark in sorted(
        summarized_bookmarks, key=lambda b: b.timestamp, reverse=True
    ):
        date_str = datetime.fromtimestamp(bookmark.timestamp, tz=timezone.utc).strftime(
            "%Y-%m-%d"
        )
        key = bookmark_identity(bookmark)
        tldr = tldr_lookup.get(key, "").strip()
        tags_str = format_tags(bookmark.tags) if bookmark.tags else ""

        summary_file_path = get_summary_file_path(
            title=bookmark.title,
            timestamp=bookmark.timestamp,
            month=bookmark.month,
            in_readme_md=True,
        )
        github_link = summary_file_path.as_posix()

        title_with_link = f"[{bookmark.title}]({github_link})"

        lines.append(f"- ({date_str}) {title_with_link}")
        if tags_str:
            lines.append(f"  - Tags: {tags_str}")
        if tldr:
            lines.append(f"  - Summary: {tldr}")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def collect_tldrs(
    bookmarks: Iterable[SummarizedBookmark],
    overrides: Optional[Dict[Tuple[str, str, int], str]] = None,
) -> Dict[Tuple[str, str, int], str]:
    overrides = overrides or {}
    lookup: Dict[Tuple[str, str, int], str] = {}

    for bookmark in bookmarks:
        key = bookmark_identity(bookmark)
        if key in overrides:
            lookup[key] = overrides[key]
            continue

        summary_file_path = get_summary_file_path(
            title=bookmark.title,
            timestamp=bookmark.timestamp,
            month=bookmark.month,
            in_readme_md=False,
        )
        lookup[key] = extract_tldr_from_markdown(str(summary_file_path))

    return lookup


def group_bookmarks_by_month(
    bookmarks: Iterable[SummarizedBookmark],
) -> Dict[str, List[SummarizedBookmark]]:
    grouped: Dict[str, List[SummarizedBookmark]] = {}
    for bookmark in bookmarks:
        grouped.setdefault(bookmark.month, []).append(bookmark)

    for month in grouped:
        grouped[month].sort(key=lambda b: b.timestamp, reverse=True)

    return grouped


def write_monthly_indexes(
    grouped_bookmarks: Dict[str, List[SummarizedBookmark]],
    tldr_lookup: Dict[Tuple[str, str, int], str],
    dry_run: bool = False,
) -> None:
    for month in sorted(grouped_bookmarks.keys(), reverse=True):
        month_dir = SUMMARY_ROOT / month
        if not month_dir.exists():
            ensure_directory(month_dir, dry_run=dry_run)

        content = build_monthly_index_markdown(
            month=month,
            bookmarks=grouped_bookmarks[month],
            tldr_lookup=tldr_lookup,
        )
        output_path = month_dir / "monthly-index.md"
        write_text_file(output_path, content, dry_run=dry_run)


@log_execution_time
def process_bookmark_file():
    raise RuntimeError(
        "process_bookmark_file has been superseded by process_changes(). "
        "Invoke main() or process_changes() with explicit arguments."
    )


def _extract_urls_with_tombstone(
    bookmark_lines: Iterable[str],
) -> Set[str]:
    """Return the set of URLs marked with #tombstone in the kohsmemo README.

    Phase C: built from the unified BookmarkEntry list.
    """
    return {e.url for e in parse_readme_to_entries(bookmark_lines) if e.has_tombstone}


def find_tombstoned_bookmarks(
    bookmark_lines: Iterable[str],
    summarized_bookmarks: Iterable[SummarizedBookmark],
) -> List[SummarizedBookmark]:
    """Return summary entries whose source URL is marked #tombstone.

    Phase C: uses the unified BookmarkEntry list to look up the tombstoned
    URL set. The caller passes `summarized_bookmarks` for the cross-check.
    """
    tombstoned_urls = _extract_urls_with_tombstone(bookmark_lines)
    if not tombstoned_urls:
        return []
    return [b for b in summarized_bookmarks if b.url in tombstoned_urls]


def remove_bookmark(bookmark: SummarizedBookmark, dry_run: bool = False) -> None:
    """Delete the .md summary file for a bookmark from disk."""
    summary_path = get_summary_file_path(
        title=bookmark.title,
        timestamp=bookmark.timestamp,
        month=bookmark.month,
        in_readme_md=False,
    )
    if not summary_path.exists():
        logging.info(
            "Summary file already absent for %s (%s); nothing to remove.",
            bookmark.title,
            summary_path,
        )
        return
    if dry_run:
        logging.info("Dry-run: would remove %s", summary_path)
        return
    summary_path.unlink()
    logging.info("Removed %s", summary_path)


def find_next_bookmark_to_process(
    bookmark_lines: Iterable[str], summarized_urls: Iterable[str]
) -> Optional[Tuple[str, str, List[str]]]:
    """Return (title, url, tags) for the first bookmark in the README that
    hasn't been summarized yet, ignoring rows with #nosummary.

    Phase C: scans the unified BookmarkEntry list (deduplicated, in README
    order) and returns the first one not in `summarized_urls` whose entry
    is not marked #nosummary.
    """
    summarized_url_set = set(summarized_urls)
    for entry in parse_readme_to_entries(bookmark_lines):
        if entry.url in summarized_url_set:
            continue
        if entry.has_nosummary:
            logging.debug(
                "Skipping bookmark with %s tag: %s", NO_SUMMARY_TAG, entry.title
            )
            continue
        return entry.title, entry.url, entry.tags
    return None


def _build_failed_ingestion_result(
    title: str, url: str, tags: List[str], reason: str
) -> IngestionResult:
    """Build a stub IngestionResult for soft-fail (content fetch / LLM
    transient errors). Same shape as a real result so the caller can append
    it to ``summarized_bookmarks`` and write the stub .md file. Sets
    ``IngestionResult.failed = True`` and marks the embedded bookmark with
    ``failed = True``."""
    timestamp = int(datetime.now(timezone.utc).timestamp())
    month = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime("%Y%m")
    summary_file_content = build_summary_file(
        title, url, "", "", tags, month, failed=True, failure_reason=reason
    )
    summary_path = get_summary_file_path(title, timestamp=timestamp, month=month)
    bookmark = SummarizedBookmark(
        month=month,
        title=title,
        url=url,
        timestamp=timestamp,
        tags=tags,
        failed=True,
    )
    return IngestionResult(
        bookmark=bookmark,
        summary_markdown=summary_file_content,
        summary_path=summary_path,
        one_sentence="",
        failed=True,
    )


def ingest_bookmark(title: str, url: str, tags: List[str]) -> IngestionResult:
    """Ingest a single bookmark. Catches soft-fail exceptions (content fetch
    / LLM rate-limit) and returns a stub IngestionResult; hard-fail
    exceptions (ConfigError, LLMError other than rate-limit, including
    strict-JSON parse failures) propagate to the caller.

    Phase B: one LLM round-trip replaces the prior 2-call sequence
    `summarize_text` + `one_sentence_summary`.
    """
    submit_to_wayback_machine(url)
    try:
        text_content: str = get_text_content(url)
        combined = summarize_to_json(text_content)
    except (ContentUnavailableError, FetchTransientError, LLMRateLimitError) as err:
        logging.warning(
            "Soft-fail ingesting %s (%s): %s",
            url,
            type(err).__name__,
            err,
        )
        return _build_failed_ingestion_result(
            title, url, tags, reason=f"{type(err).__name__}: {err}"
        )
    # ConfigError, LLMError (including parse failures from strict JSON mode),
    # and anything unexpected will propagate. The caller is expected to let
    # those abort the run.

    summary: str = combined.summary
    one_sentence: str = combined.tldr

    timestamp = int(datetime.now(timezone.utc).timestamp())
    month = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime("%Y%m")
    summary_file_content: str = build_summary_file(
        title, url, summary, one_sentence, tags, month
    )
    summary_path = get_summary_file_path(title, timestamp=timestamp, month=month)

    bookmark = SummarizedBookmark(
        month=month,
        title=title,
        url=url,
        timestamp=timestamp,
        tags=tags,
    )
    return IngestionResult(
        bookmark=bookmark,
        summary_markdown=summary_file_content,
        summary_path=summary_path,
        one_sentence=one_sentence,
    )


def process_changes(backfill: bool = False, dry_run: bool = False) -> None:
    summarized_bookmarks = load_summarized_bookmarks()
    summarized_urls = [bookmark.url for bookmark in summarized_bookmarks]

    bookmark_lines = read_bookmark_collection_lines()
    url_tag_lookup = build_url_tag_lookup(bookmark_lines)
    if url_tag_lookup:
        for bookmark in summarized_bookmarks:
            if bookmark.url in url_tag_lookup:
                bookmark.tags = url_tag_lookup[bookmark.url]

    overrides: Dict[Tuple[str, str, int], str] = {}

    ingestion_result: Optional[IngestionResult] = None

    # --- Removal pass: tombstoned + directly-removed links ---
    # Runs even in dry-run (we log "would remove" but never unlink) and even
    # when `requests` is missing (no ingest possible, but cleanup is safe).
    # Backfill is the only mode that skips this branch — it must not mutate
    # the source-of-truth on disk.
    if backfill:
        logging.info(
            "Backfill mode enabled; rebuilding summaries/indexes from existing data only."
        )
    else:
        # Only #tombstone triggers deletion. Direct URL removal in the
        # source README is intentionally NOT handled here — workflow_dispatch
        # re-runs would otherwise delete summaries for URLs that still exist
        # in the user's local working copy but were never part of the
        # triggering commit.
        tombstoned = find_tombstoned_bookmarks(
            bookmark_lines, summarized_bookmarks
        )
        # Stable order by timestamp (oldest first) for predictable logging.
        to_remove = sorted(tombstoned, key=lambda b: b.timestamp)
        if to_remove:
            logging.info("Removing %d bookmark(s) from summary:", len(to_remove))
            for bookmark in to_remove:
                logging.info(
                    "  - %s (%s) [tombstoned in source] -> %s",
                    bookmark.title,
                    bookmark.url,
                    get_summary_file_path(
                        title=bookmark.title,
                        timestamp=bookmark.timestamp,
                        month=bookmark.month,
                    ),
                )
                remove_bookmark(bookmark, dry_run=dry_run)
            remove_urls = {b.url for b in to_remove}
            summarized_bookmarks = [
                b for b in summarized_bookmarks if b.url not in remove_urls
            ]
            summarized_urls = [b.url for b in summarized_bookmarks]
        else:
            logging.info("No bookmarks to remove.")

    # --- Ingest pass: at most one new bookmark per run ---
    # Requires `requests` and a non-dry-run. Dry-run mode intentionally skips
    # network calls and writes; backfill explicitly skips ingest by definition.
    can_ingest = (not backfill) and (not dry_run) and (requests is not None)
    if not can_ingest:
        if dry_run and not backfill:
            logging.info(
                "Dry-run mode enabled; skipping network calls and writes."
            )
        elif requests is None and not backfill:
            logging.warning(
                "requests dependency missing; cannot ingest new bookmarks. "
                "Run with --backfill or install optional dependencies."
            )
    else:
        next_bookmark = find_next_bookmark_to_process(bookmark_lines, summarized_urls)

        if next_bookmark:
            title, url, tags = next_bookmark
            if TOMBSTONE_TAG in [t.lower() for t in tags]:
                logging.info(
                    "Skipping tombstoned URL (would otherwise be ingested): %s",
                    url,
                )
            else:
                logging.info("Processing new bookmark: %s", title)
                # Hard-fail (ConfigError, LLMError other than rate-limit) must
                # abort the run — there is no point in writing a stub for a
                # permanent configuration problem. Soft-fail exceptions are
                # caught inside `ingest_bookmark` and turned into a stub
                # IngestionResult, so they don't reach this point.
                try:
                    ingestion_result = ingest_bookmark(title, url, tags)
                except (ConfigError, LLMError) as err:
                    logging.error(
                        "Hard-fail ingesting %s (%s): %s",
                        url,
                        type(err).__name__,
                        err,
                    )
                    logging.error(
                        "Aborting the run before writing derived files; "
                        "data.json / indexes will not be touched."
                    )
                    return
                summarized_bookmarks.append(ingestion_result.bookmark)
                write_text_file(
                    ingestion_result.summary_path,
                    ingestion_result.summary_markdown,
                    dry_run=False,
                )
                if not ingestion_result.failed:
                    # Only override the TL;DR for successful ingests. Failed
                    # entries keep the stub TL;DR that's already in the file.
                    overrides[bookmark_identity(ingestion_result.bookmark)] = (
                        ingestion_result.one_sentence
                    )
        else:
            logging.info("No new bookmarks to process.")

    # --- Rebuild derived files (data.json, indexes, READMEs) ---
    # `dry_run=True` makes all writers log "would write" without touching disk.
    save_summarized_bookmarks(summarized_bookmarks, dry_run=dry_run)

    grouped = group_bookmarks_by_month(summarized_bookmarks)
    tldr_lookup = collect_tldrs(
        summarized_bookmarks,
        overrides=overrides,
    )

    write_monthly_indexes(grouped, tldr_lookup, dry_run=dry_run)

    readme_content = build_summary_readme_md(
        summarized_bookmarks,
        grouped,
        tldr_lookup,
    )
    write_text_file(SUMMARY_README_PATH, readme_content, dry_run=dry_run)

    all_summary_content = build_all_summary_md(
        summarized_bookmarks,
        tldr_lookup,
    )
    all_summary_path = SUMMARY_ROOT / "all_summary.md"
    write_text_file(all_summary_path, all_summary_content, dry_run=dry_run)

    if dry_run:
        logging.info("Dry-run complete; no files were written.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update bookmark summaries.")
    parser.add_argument(
        "--backfill",
        action="store_true",
        help="Rebuild README and monthly indexes without ingesting new bookmarks.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run the pipeline without writing changes to disk.",
    )
    args = parser.parse_args()

    env_dry_run = os.getenv("BOOKMARK_SUMMARY_DRY_RUN", "").lower() in (
        "1",
        "true",
        "yes",
    )
    if env_dry_run:
        args.dry_run = True

    return args


def main():
    args = parse_args()
    process_changes(backfill=args.backfill, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
