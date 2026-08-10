#!/usr/bin/env python3
"""Update README citation emojis via Semantic Scholar Graph API, with OpenAlex fallback.

Reads paper ids from config.yaml, maps influential/citation counts to ◼️🔹🔸🔥🌟,
and rewrites matching lines in README.md. Optional env: S2_API_KEY.
"""
from __future__ import annotations

import os
import re
import time
from pathlib import Path
from urllib.parse import urlparse

import requests
import yaml

try:
    from tqdm import tqdm
except ImportError:  # pragma: no cover
    def tqdm(iterable, desc=None):
        if desc:
            print(desc, flush=True)
        return iterable


S2_GRAPH = "https://api.semanticscholar.org/graph/v1/paper"
OPENALEX = "https://api.openalex.org/works"
FIELDS = "influentialCitationCount,citationCount,title"
DEFAULT_SLEEP = 3.5
KEYED_SLEEP = 1.0
OA_SLEEP = 0.2


def s2_headers() -> dict:
    h = {"User-Agent": "awesome-3d-point-cloud-denoising-updater/2.1"}
    key = os.environ.get("S2_API_KEY", "").strip()
    if key:
        h["x-api-key"] = key
    return h


def paper_id_from_url(url: str) -> str | None:
    path = urlparse(url).path.rstrip("/")
    if not path:
        return None
    pid = path.split("/")[-1]
    return pid if pid and pid != "0" else None


def get_emoji(count: int | None) -> str | None:
    if count is None:
        return None
    if count >= 50:
        return "🌟"
    if count > 25:
        return "🔥"
    if count >= 10:
        return "🔸"
    if count >= 5:
        return "🔹"
    return "◼️"


def replace_emoji(line: str, new_emoji: str | None) -> str:
    if not new_emoji:
        return line
    emoji_pattern = re.compile(r"(◼️|🔹|🔸|🔥|🌟)")
    matches = list(emoji_pattern.finditer(line))
    if not matches:
        return line.rstrip() + " " + new_emoji + "\n"
    last = matches[-1]
    return line[: last.start()] + new_emoji + line[last.end() :]


def fetch_s2(paper_id: str, session: requests.Session, retries: int = 4) -> int | None:
    url = f"{S2_GRAPH}/{paper_id}"
    keyed = bool(os.environ.get("S2_API_KEY", "").strip())
    for attempt in range(retries):
        try:
            r = session.get(url, params={"fields": FIELDS}, timeout=45)
        except requests.RequestException as exc:
            print(f"  S2 network: {exc}", flush=True)
            time.sleep(5 * (attempt + 1))
            continue

        if r.status_code == 429:
            if not keyed:
                print("  S2 429 (no API key); falling back to OpenAlex", flush=True)
                return None
            retry_after = r.headers.get("Retry-After")
            wait = int(retry_after) if retry_after and retry_after.isdigit() else 15 * (attempt + 1)
            print(f"  S2 429; sleep {wait}s", flush=True)
            time.sleep(wait)
            continue
        if r.status_code == 404:
            print(f"  S2 not found: {paper_id}", flush=True)
            return None
        if r.status_code >= 400:
            print(f"  S2 HTTP {r.status_code}: {r.text[:120]}", flush=True)
            return None

        data = r.json()
        count = data.get("influentialCitationCount")
        if count is None:
            count = data.get("citationCount", 0)
        print(f"  S2 {int(count or 0):>4} | {(data.get('title') or '')[:55]}", flush=True)
        return int(count or 0)
    return None


def fetch_openalex(title: str, session: requests.Session) -> int | None:
    # Prefer exact-ish title match; OpenAlex is generous with rate limits.
    params = {
        "filter": f"title.search:{title}",
        "per-page": 5,
        "select": "id,title,cited_by_count",
    }
    try:
        r = session.get(
            OPENALEX,
            params=params,
            headers={"User-Agent": "awesome-3d-point-cloud-denoising-updater/2.1"},
            timeout=45,
        )
        r.raise_for_status()
    except requests.RequestException as exc:
        print(f"  OpenAlex error: {exc}", flush=True)
        return None

    results = (r.json() or {}).get("results") or []
    if not results:
        print("  OpenAlex: no results", flush=True)
        return None

    title_l = title.lower().strip()
    best = None
    for item in results:
        t = (item.get("title") or "").lower().strip()
        if t == title_l or title_l in t or t in title_l:
            best = item
            break
    if best is None:
        best = results[0]

    count = int(best.get("cited_by_count") or 0)
    print(f"  OA  {count:>4} | {(best.get('title') or '')[:55]}", flush=True)
    time.sleep(OA_SLEEP)
    return count


def main() -> None:
    root = Path(__file__).resolve().parent
    config = yaml.safe_load((root / "config.yaml").read_text(encoding="utf-8"))
    papers = config.get("papers", [])

    keyed = bool(os.environ.get("S2_API_KEY", "").strip())
    pause = KEYED_SLEEP if keyed else DEFAULT_SLEEP
    print(
        f"Updater | S2_API_KEY={'yes' if keyed else 'no'} | S2 pause={pause}s | OpenAlex fallback=on",
        flush=True,
    )
    if not keyed:
        print(
            "Tip: export S2_API_KEY=... for influentialCitationCount at higher quota "
            "(https://www.semanticscholar.org/product/api#api-key-form)",
            flush=True,
        )

    entries: list[tuple[str, str]] = []
    for paper in papers:
        name = (paper.get("name") or "").strip()
        url = (paper.get("url") or "").strip()
        pid = paper_id_from_url(url) if url else None
        if name and pid:
            entries.append((name, pid))

    print(f"papers to query: {len(entries)}", flush=True)

    s2 = requests.Session()
    s2.headers.update(s2_headers())
    oa = requests.Session()

    counts: dict[str, int] = {}
    s2_ok = 0
    oa_ok = 0
    s2_disabled = False

    for name, pid in tqdm(entries, desc="Updating citations..."):
        print(f"> {name[:70]}", flush=True)
        count = None
        if not s2_disabled:
            count = fetch_s2(pid, s2)
            if count is not None:
                s2_ok += 1
                counts[name] = count
                time.sleep(pause)
                continue
            # If S2 keeps 429-ing, skip further S2 attempts after a few failures
            # once we already know the IP is throttled (no API key).
            if not keyed:
                # probe: one more quick call pattern handled inside fetch_s2;
                # after miss, fall back and optionally disable S2 for speed.
                pass

        count = fetch_openalex(name, oa)
        if count is not None:
            oa_ok += 1
            counts[name] = count
            if not keyed:
                s2_disabled = True  # unauthenticated S2 quota exhausted; finish via OA
        elif not keyed:
            time.sleep(pause)

    if s2_disabled:
        print("Note: finished via OpenAlex after Semantic Scholar rate limits.", flush=True)

    readme = root / "README.md"
    lines = readme.read_text(encoding="utf-8").splitlines(keepends=True)
    updated = 0
    unmatched = 0
    for name, count in counts.items():
        emoji = get_emoji(count)
        matched = False
        for i, line in enumerate(lines):
            if name in line:
                new_line = replace_emoji(line, emoji)
                if new_line != line:
                    lines[i] = new_line
                    updated += 1
                matched = True
                break
        if not matched:
            unmatched += 1
            print(f"WARNING: no README match for: {name}", flush=True)

    readme.write_text("".join(lines), encoding="utf-8")
    print(
        f"Done. resolved={len(counts)} s2={s2_ok} openalex={oa_ok} "
        f"updated_lines={updated} unmatched={unmatched}",
        flush=True,
    )


if __name__ == "__main__":
    main()
