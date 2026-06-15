#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DIGEST_SECTIONS = [
    "Theme",
    "Short overview",
    "Ranked list",
    "Most relevant paper",
    "Novelty / framing / baseline impact",
    "One-paragraph takeaway",
    "Category calls",
    "Inspection notes / uncertainty",
]

REQUIRED_NOTE_SECTIONS = [
    "Basic info",
    "Quick verdict",
    "One-paragraph overview",
    "Model definition",
    "Key questions this summary must address",
]

REQUIRED_NOTE_QUESTIONS = [
    "1. What problem is the paper trying to solve?",
    "2. What is the method?",
    "3. What is the method motivation?",
    "4. What data does it use?",
    "5. How is it evaluated?",
    "6. What are the main results?",
    "7. What is actually novel?",
    "8. What are the strengths?",
    "9. What are the weaknesses, limitations, or red flags?",
    "10. What challenges or open problems remain?",
    "11. What future work naturally follows?",
    "12. Why does this matter for cabbageland?",
    "13. What ideas are steal-worthy?",
    "14. Final decision",
]


def today_la() -> str:
    return datetime.now(ZoneInfo("America/Los_Angeles")).date().isoformat()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def extract_section(text: str, section: str) -> str:
    pattern = rf"^## {re.escape(section)}\n+(.*?)(?=^## |\Z)"
    match = re.search(pattern, text, flags=re.M | re.S)
    return match.group(1).strip() if match else ""


def linked_note_map(text: str) -> dict[str, str]:
    links: dict[str, str] = {}
    for title, url in re.findall(r"- \[(.+?)\]\((.+?)\)", text):
        if "/paper_notes/" not in url:
            continue
        slug = url.rstrip("/").rsplit("/", 1)[-1]
        slug = re.sub(r"\.md$", "", slug)
        links[title.strip()] = slug
    return links


def ranked_titles(text: str) -> list[str]:
    ranked = extract_section(text, "Ranked list")
    return [m.strip() for m in re.findall(r"^\d+\. \*\*(.+?)\*\*", ranked, flags=re.M)]


def verify_note(path: Path, *, require_date: str | None, errors: list[str]) -> None:
    text = read_text(path)
    if not text.startswith("# "):
        errors.append(f"{path.relative_to(ROOT)} missing top-level title")
    for section in REQUIRED_NOTE_SECTIONS:
        if not re.search(rf"^## {re.escape(section)}\s*$", text, flags=re.M):
            errors.append(f"{path.relative_to(ROOT)} missing note section: {section}")
    for question in REQUIRED_NOTE_QUESTIONS:
        if not re.search(rf"^### {re.escape(question)}\s*$", text, flags=re.M):
            errors.append(f"{path.relative_to(ROOT)} missing question: {question}")
    if require_date and not re.search(rf"^\* Date surfaced:\s*{re.escape(require_date)}\s*$", text, flags=re.M):
        errors.append(f"{path.relative_to(ROOT)} missing Date surfaced: {require_date}")
    if not re.search(r"^\* Link:\s*https?://", text, flags=re.M):
        errors.append(f"{path.relative_to(ROOT)} missing http Link metadata")
    if "abstract-only" in text.lower() and "10 full-text" not in text.lower():
        errors.append(f"{path.relative_to(ROOT)} says abstract-only without explicit full-text-attempt caveat")


def verify_email_render(date: str, errors: list[str]) -> None:
    module_path = ROOT / "neuro_daily_email.py"
    spec = importlib.util.spec_from_file_location("neuro_daily_email", module_path)
    if spec is None or spec.loader is None:
        errors.append("could not load neuro_daily_email.py for render verification")
        return

    neuro_daily_email = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(neuro_daily_email)

    try:
        digest = neuro_daily_email.parse_digest(ROOT / "daily_papers" / f"{date}.md")
        items = neuro_daily_email.build_items(digest)
        neuro_daily_email.validate_digest_structure(digest, items)

        msg = EmailMessage()
        msg["Subject"] = digest["title"]
        msg["From"] = "neuro-daily@example.invalid"
        msg["To"] = "recipient@example.invalid"
        msg.set_content(neuro_daily_email.render_plain(digest, items))
        msg.add_alternative(neuro_daily_email.render_html(digest, items), subtype="html")
        neuro_daily_email.validate_rendered_message(
            msg,
            ["recipient@example.invalid"],
            expected_item_count=len(items),
        )
    except Exception as exc:
        errors.append(f"email render verification failed: {exc}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify Neuro Daily markdown content before web/audio publishing")
    parser.add_argument("--date", default=today_la(), help="Digest date to verify, YYYY-MM-DD")
    args = parser.parse_args()

    errors: list[str] = []
    digest_path = ROOT / "daily_papers" / f"{args.date}.md"
    if not digest_path.exists():
        errors.append(f"missing source digest daily_papers/{args.date}.md")
        digest_text = ""
    else:
        digest_text = read_text(digest_path)

    if digest_text:
        if not digest_text.startswith(f"# {args.date}\n"):
            errors.append(f"daily_papers/{args.date}.md first heading must be # {args.date}")
        for section in REQUIRED_DIGEST_SECTIONS:
            if not extract_section(digest_text, section):
                errors.append(f"daily_papers/{args.date}.md missing/nonempty section: {section}")

        titles = ranked_titles(digest_text)
        if len(titles) < 3:
            errors.append(f"daily_papers/{args.date}.md must rank at least 3 preserved items, found {len(titles)}")
        links = linked_note_map(extract_section(digest_text, "Category calls"))
        for title in titles[:4]:
            slug = links.get(title)
            if not slug:
                errors.append(f"ranked title lacks preserved note link in Category calls: {title}")
                continue
            note_path = ROOT / "paper_notes" / f"{slug}.md"
            if not note_path.exists():
                errors.append(f"ranked title links missing note: paper_notes/{slug}.md")

        verify_email_render(args.date, errors)

    for note_path in sorted((ROOT / "paper_notes").glob("*.md")):
        if note_path.name == ".gitkeep":
            continue
        text = read_text(note_path)
        if re.search(rf"^\* Date surfaced:\s*{re.escape(args.date)}\s*$", text, flags=re.M):
            verify_note(note_path, require_date=args.date, errors=errors)

    if errors:
        print("CONTENT_VERIFY_FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("CONTENT_VERIFY_OK")
    print(f"date={args.date}")
    print(f"ranked_items={len(ranked_titles(digest_text)) if digest_text else 0}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
