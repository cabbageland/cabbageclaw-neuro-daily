#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
WEB_ROOT = ROOT.parent / "cabbageclaw-neuro-daily-web"
CONTENT_JSON = WEB_ROOT / "data" / "content.json"
SITE_BASE = "https://cabbageland.github.io/cabbageclaw-neuro-daily-web"


def today_la() -> str:
    return datetime.now(ZoneInfo("America/Los_Angeles")).date().isoformat()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def load_content(path: Path) -> dict:
    return json.loads(read_text(path))


def note_slugs_linked_from_digest(text: str) -> set[str]:
    slugs = set(re.findall(r"/paper_notes/([A-Za-z0-9_-]+)", text))
    slugs.update(re.findall(r"\]\((?:\.\./)?paper_notes/([A-Za-z0-9_-]+)(?:\.md)?\)", text))
    return slugs


def notes_surfaced_on(date: str) -> set[str]:
    surfaced = set()
    for path in (ROOT / "paper_notes").glob("*.md"):
        if path.name == ".gitkeep":
            continue
        text = read_text(path)
        if re.search(rf"^\* Date surfaced:\s*{re.escape(date)}\s*$", text, flags=re.M):
            surfaced.add(path.stem)
    return surfaced


def url_ok(url: str) -> tuple[bool, str]:
    request = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            status = getattr(response, "status", 200)
            if 200 <= status < 400:
                return True, f"HTTP {status}"
            return False, f"HTTP {status}"
    except urllib.error.HTTPError as exc:
        return False, f"HTTP {exc.code}"
    except Exception as exc:
        return False, str(exc)


def fetch_live_content() -> dict:
    with urllib.request.urlopen(f"{SITE_BASE}/data/content.json", timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def check_audio_entry(
    *,
    content: dict,
    source_key: str,
    errors: list[str],
    check_live: bool,
    live_content: dict | None,
) -> None:
    audio = content.get("audio", {}).get(source_key)
    if not audio:
        errors.append(f"missing local content audio entry for {source_key}")
        return

    script_path = audio.get("scriptPath")
    if script_path and not (ROOT / script_path).exists():
        errors.append(f"missing source audio script {script_path} for {source_key}")

    audio_path = audio.get("audioPath")
    if not audio_path:
        errors.append(f"missing audioPath for {source_key}")
        return
    if not (WEB_ROOT / audio_path).exists():
        errors.append(f"missing local web audio file {audio_path} for {source_key}")

    if check_live:
        live_audio = (live_content or {}).get("audio", {}).get(source_key)
        if not live_audio:
            errors.append(f"missing live content audio entry for {source_key}")
            return
        live_audio_path = live_audio.get("audioPath")
        if not live_audio_path:
            errors.append(f"missing live audioPath for {source_key}")
            return
        ok, detail = url_ok(f"{SITE_BASE}/{live_audio_path}")
        if not ok:
            errors.append(f"live audio URL failed for {source_key}: {detail}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify Neuro Daily publish wiring")
    parser.add_argument("--date", default=today_la(), help="Digest date to verify, YYYY-MM-DD")
    parser.add_argument("--live", action="store_true", help="Also verify live GitHub Pages content/audio")
    args = parser.parse_args()

    errors: list[str] = []
    digest_key = f"daily_papers/{args.date}.md"
    digest_path = ROOT / digest_key
    if not digest_path.exists():
        errors.append(f"missing source digest {digest_key}")
        digest_text = ""
    else:
        digest_text = read_text(digest_path)

    if not CONTENT_JSON.exists():
        errors.append(f"missing web content snapshot {CONTENT_JSON}")
        content = {}
    else:
        content = load_content(CONTENT_JSON)

    if digest_key not in content.get("markdown", {}):
        errors.append(f"missing local content markdown for {digest_key}")
    if not any(item.get("date") == args.date for item in content.get("digests", [])):
        errors.append(f"missing local digest index entry for {args.date}")

    live_content = None
    if args.live:
        try:
            live_content = fetch_live_content()
        except Exception as exc:
            errors.append(f"failed to fetch live content.json: {exc}")
        if live_content is not None:
            if digest_key not in live_content.get("markdown", {}):
                errors.append(f"missing live content markdown for {digest_key}")
            if not any(item.get("date") == args.date for item in live_content.get("digests", [])):
                errors.append(f"missing live digest index entry for {args.date}")

    check_audio_entry(
        content=content,
        source_key=digest_key,
        errors=errors,
        check_live=args.live,
        live_content=live_content,
    )

    note_slugs = note_slugs_linked_from_digest(digest_text) | notes_surfaced_on(args.date)
    for slug in sorted(note_slugs):
        note_key = f"paper_notes/{slug}.md"
        note_path = ROOT / note_key
        if not note_path.exists():
            errors.append(f"missing source note {note_key}")
            continue
        if note_key not in content.get("markdown", {}):
            errors.append(f"missing local content markdown for {note_key}")
        if not any(item.get("slug") == slug for item in content.get("notes", [])):
            errors.append(f"missing local note index entry for {slug}")
        if args.live and live_content is not None:
            if note_key not in live_content.get("markdown", {}):
                errors.append(f"missing live content markdown for {note_key}")
            if not any(item.get("slug") == slug for item in live_content.get("notes", [])):
                errors.append(f"missing live note index entry for {slug}")
        check_audio_entry(
            content=content,
            source_key=note_key,
            errors=errors,
            check_live=args.live,
            live_content=live_content,
        )

    if errors:
        print("VERIFY_FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VERIFY_OK")
    print(f"date={args.date}")
    print(f"notes_checked={len(note_slugs)}")
    print(f"live={str(args.live).lower()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
