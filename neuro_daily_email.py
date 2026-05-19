#!/usr/bin/env python3
import argparse
import csv
import html
import re
import smtplib
import ssl
import subprocess
import urllib.request
from datetime import date, datetime
from email.message import EmailMessage
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIGEST_DIR = ROOT / "daily_papers"
NOTES_DIR = ROOT / "paper_notes"
RECIPIENTS_CSV = ROOT / "recipients.csv"
INTERNAL_TEST_RECIPIENTS_CSV = ROOT / "recipients-internal-test.csv"
CONFIG_PATH = Path.home() / ".config" / "himalaya" / "config.toml"
SITE_BASE = "https://cabbageland.github.io/cabbageclaw-neuro-daily-web"
DIGEST_WEB_BASE = f"{SITE_BASE}/daily_papers"
NOTES_WEB_BASE = f"{SITE_BASE}/paper_notes"

SECTION_HEADERS = {
    "Theme",
    "Short overview",
    "Ranked list",
    "Most relevant paper",
    "Novelty / framing / baseline impact",
    "One-paragraph takeaway",
    "Category calls",
    "Inspection notes / uncertainty",
}


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--date", help="Digest date in YYYY-MM-DD format. Defaults to today.")
    p.add_argument("--to", action="append", default=[], help="Optional extra recipient. Repeatable.")
    p.add_argument("--dry-run", action="store_true", help="Render output but do not send.")
    p.add_argument("--preview-path", help="Write rendered HTML preview to this path.")
    p.add_argument("--internal-test", action="store_true", help="Send only to recipients-internal-test.csv for debugging or maintenance.")
    return p.parse_args()


def pick_date(date_str: str | None) -> str:
    if date_str:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    return date.today().isoformat()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_digest(path: Path) -> dict:
    text = read_text(path)
    lines = text.splitlines()
    result = {
        "date": lines[0].lstrip("# ").strip(),
        "title": f"Neuro Daily, {lines[0].lstrip('# ').strip()}, Reporter: cabbageclaw",
        "overview": "",
        "takeaway": "",
        "ranked_titles": [],
        "note_links": {},
        "ranked_why": {},
    }

    current = None
    blocks: dict[str, list[str]] = {}
    for line in lines[1:]:
        if line.startswith("## "):
            current = line[3:].strip()
            blocks[current] = []
        elif current is not None:
            blocks[current].append(line)

    result["overview"] = "\n".join(blocks.get("Short overview", [])).strip()
    result["takeaway"] = "\n".join(blocks.get("One-paragraph takeaway", [])).strip()
    result["ranked_why"] = ranked_why_map(text)

    ranked = []
    for line in blocks.get("Ranked list", []):
        m = re.match(r"\d+\. \*\*(.+?)\*\*", line.strip())
        if m:
            ranked.append(m.group(1).strip())
    result["ranked_titles"] = ranked

    for section in ("Directly relevant", "Adjacent inspiration"):
        section_lines = blocks.get("Category calls", [])
        active = None
        for line in section_lines:
            if line.startswith("### "):
                active = line[4:].strip()
                continue
            if active in {"Directly relevant", "Adjacent inspiration"}:
                m = re.match(r"- \[(.+?)\]\((.+?)\)", line.strip())
                if m:
                    result["note_links"][m.group(1).strip()] = m.group(2).strip()

    return result


def split_overview_paragraphs(overview: str) -> list[str]:
    paras = [p.strip() for p in overview.split("\n\n") if p.strip()]
    return [strip_markdown_emphasis(p) for p in paras[:4]]


def read_note_metadata(slug: str) -> tuple[str | None, str | None]:
    note_path = NOTES_DIR / f"{slug}.md"
    if not note_path.exists():
        return None, None
    text = read_text(note_path)
    title = None
    doi = None
    for line in text.splitlines()[:20]:
        if line.startswith("# "):
            title = line[2:].strip()
        if line.startswith("* Link: "):
            doi = line.split(": ", 1)[1].strip()
    return title, doi


def normalize_web_markdown_url(url: str) -> str:
    if re.match(r"^https://cabbageland\.github\.io/cabbageclaw-neuro-daily-web/(daily_papers|paper_notes|related_notes)/[^?#/]+$", url):
        return url + ".md"
    return url


def public_app_route(url: str) -> str:
    normalized = normalize_web_markdown_url(url)
    prefix = f"{SITE_BASE}/"
    if normalized.startswith(prefix):
        return f"{SITE_BASE}/#/{normalized[len(prefix):]}"
    return normalized


def slug_from_note_url(url: str) -> str:
    slug = url.rstrip("/").split("/")[-1]
    return re.sub(r"\.md$", "", slug)


def build_items(digest: dict) -> list[dict]:
    paras = split_overview_paragraphs(digest["overview"])
    items = []
    for idx, title in enumerate(digest["ranked_titles"][:4]):
        note_url = digest["note_links"].get(title)
        if not note_url:
            raise ValueError(f"Missing note link for ranked paper: {title}")
        note_url = normalize_web_markdown_url(note_url)
        slug = slug_from_note_url(note_url)
        note_title, paper_url = read_note_metadata(slug)
        if not paper_url:
            raise ValueError(f"Missing paper link in note: {slug}")
        para = paras[idx] if idx < len(paras) else ""
        body, why = extract_body_and_why(para)
        items.append({
            "title": title,
            "paper_url": paper_url,
            "paper_label": note_title or title,
            "notes_url": note_url,
            "body": body,
            "why": digest["ranked_why"].get(title, why),
        })
    return items


def ranked_why_map(digest_text: str) -> dict[str, str]:
    lines = digest_text.splitlines()
    result: dict[str, str] = {}
    in_ranked = False
    current_title = None
    for line in lines:
        if line.startswith("## "):
            section = line[3:].strip()
            in_ranked = section == "Ranked list"
            if not in_ranked:
                current_title = None
            continue
        if not in_ranked:
            continue
        title_match = re.match(r"\d+\. \*\*(.+?)\*\*", line.strip())
        if title_match:
            current_title = strip_markdown_emphasis(title_match.group(1).strip())
            continue
        why_match = re.match(r"Why it matters:\s*(.+)", line.strip())
        if current_title and why_match:
            result[current_title] = strip_markdown_emphasis(why_match.group(1).strip())
    return result


def extract_body_and_why(paragraph: str) -> tuple[str, str]:
    paragraph = paragraph.strip()
    match = re.search(r"Why it matters:\s*(.+)$", paragraph)
    if match:
        body = paragraph[:match.start()].strip()
        why = match.group(1).strip()
        return strip_markdown_emphasis(body), strip_markdown_emphasis(why)
    return strip_markdown_emphasis(paragraph), ""


def strip_markdown_emphasis(text: str) -> str:
    return text.replace("**", "").strip()


def read_recipients(extra: list[str], internal_test: bool = False) -> list[str]:
    recipients = []
    recipients_path = INTERNAL_TEST_RECIPIENTS_CSV if internal_test else RECIPIENTS_CSV
    if recipients_path.exists():
        with recipients_path.open(newline="", encoding="utf-8") as f:
            for row in csv.reader(f):
                if not row:
                    continue
                email = row[0].strip()
                if email and not email.startswith("#"):
                    recipients.append(email)
    recipients.extend(extra)
    deduped = []
    seen = set()
    for r in recipients:
        if r not in seen:
            seen.add(r)
            deduped.append(r)
    if not deduped:
        raise ValueError("No recipients found. Populate recipients.csv or pass --to.")
    return deduped


def validate_digest_structure(digest: dict, items: list[dict]):
    errors = []
    if len(items) != 4:
        errors.append(f"Expected 4 ranked papers, found {len(items)}")
    if not digest["takeaway"]:
        errors.append("Missing one-paragraph takeaway")
    if not digest["overview"]:
        errors.append("Missing short overview")
    for idx, item in enumerate(items, start=1):
        if not item["paper_url"].startswith("http"):
            errors.append(f"Item {idx} missing valid paper URL")
        if not item["notes_url"].startswith("http"):
            errors.append(f"Item {idx} missing valid notes URL")
        if not item["why"]:
            errors.append(f"Item {idx} missing Why it matters")
        if len(item["body"]) < 120:
            errors.append(f"Item {idx} body looks too short")
    if errors:
        raise ValueError("Email QC failed: " + "; ".join(errors))


def validate_rendered_message(msg: EmailMessage, recipients: list[str], internal_test: bool = False):
    errors = []
    plain_part = msg.get_body(preferencelist=("plain",))
    html_part = msg.get_body(preferencelist=("html",))
    plain = plain_part.get_content() if plain_part else ""
    html_body = html_part.get_content() if html_part else ""

    if not recipients:
        errors.append("Recipient list is empty")
    if "**" in plain or "**" in html_body:
        errors.append("Raw markdown emphasis leaked into rendered email")
    for token in ["Paper:", "Notes:", "Bottom line:"]:
        if token not in plain:
            errors.append(f"Missing plain-text token: {token}")
    if "<a href=" not in html_body:
        errors.append("HTML body has no hyperlinks")
    if html_body.count("<a href=") < 8:
        errors.append("HTML body has fewer hyperlinks than expected")
    if "Content-Type: multipart/alternative" not in msg.as_string().split("\n\n", 1)[0]:
        errors.append("Message is not multipart/alternative")
    if internal_test and recipients != read_recipients([], internal_test=True):
        errors.append("Internal test mode recipients differ from recipients-internal-test.csv")
    if errors:
        raise ValueError("Rendered email QC failed: " + "; ".join(errors))


def verify_web_links_before_send(digest: dict, items: list[dict]):
    urls = [public_app_route(f"{DIGEST_WEB_BASE}/{digest['date']}")]
    urls.extend(public_app_route(item["notes_url"]) for item in items)
    errors = []
    for url in urls:
        try:
            with urllib.request.urlopen(url, timeout=15) as response:
                status = getattr(response, "status", 200)
                final_url = getattr(response, "url", url)
                body = response.read(2048).decode("utf-8", errors="ignore")
                if status >= 400:
                    errors.append(f"{url} returned HTTP {status}")
                elif final_url.rstrip("/") != url.rstrip("/"):
                    errors.append(f"{url} redirected unexpectedly to {final_url}")
                elif "Failed to load dashboard" in body:
                    errors.append(f"{url} loaded dashboard error page")
        except Exception as exc:
            errors.append(f"{url} failed: {exc}")
    if errors:
        raise ValueError("Pre-send link verification failed: " + "; ".join(errors))


def smtp_settings() -> tuple[str, int, str, str]:
    text = read_text(CONFIG_PATH)
    host = re.search(r'message\.send\.backend\.host = "([^"]+)"', text)
    port = re.search(r'message\.send\.backend\.port = (\d+)', text)
    login = re.search(r'message\.send\.backend\.login = "([^"]+)"', text)
    cmd = re.search(r'message\.send\.backend\.auth\.cmd = "([^"]+)"', text)
    if not all([host, port, login, cmd]):
        raise ValueError("Could not parse SMTP settings from Himalaya config")
    password = subprocess.check_output(cmd.group(1), shell=True, text=True).strip()
    return host.group(1), int(port.group(1)), login.group(1), password


def render_plain(digest: dict, items: list[dict]) -> str:
    lines = [
        "Hello!",
        "",
        f"Welcome to the {human_date(digest['date'])} Neuro Daily at Cabbageland: {DIGEST_WEB_BASE}/{digest['date']}.md",
        "",
        "Today's strongest papers are the ones that make neuromodulation less fuzzy and more operational.",
        "",
    ]
    for item in items:
        lines.extend([
            item["title"],
            f"Paper: {item['paper_url']}",
            f"Notes: {item['notes_url']}",
            item["body"],
            f"Why it matters: {item['why']}",
            "",
        ])
    lines.extend([
        f"Bottom line: {digest['takeaway']}",
        "",
        "Yours,",
        "cabbageclaw 🥬🐾",
    ])
    return "\n".join(lines)


def render_html(digest: dict, items: list[dict]) -> str:
    parts = [
        "<html><body>",
        "<p>Hello!</p>",
        f"<p>Welcome to the <a href=\"{DIGEST_WEB_BASE}/{digest['date']}.md\">{html.escape(human_date(digest['date']))} Neuro Daily</a> at Cabbageland.</p>",
        "<p>Today's strongest papers are the ones that make neuromodulation less fuzzy and more operational.</p>",
    ]
    for item in items:
        parts.extend([
            f"<p><strong>{html.escape(item['title'])}</strong></p>",
            f"<p><strong>Paper:</strong> <a href=\"{html.escape(item['paper_url'])}\">{html.escape(item['paper_label'])}</a><br><strong>Notes:</strong> <a href=\"{html.escape(item['notes_url'])}\">Cabbageland notes</a></p>",
            f"<p>{html.escape(item['body'])}</p>",
            f"<p><strong>Why it matters:</strong> {html.escape(item['why'])}</p>",
        ])
    parts.extend([
        f"<p><strong>Bottom line:</strong> {html.escape(digest['takeaway'])}</p>",
        "<p>Yours,<br>cabbageclaw 🥬🐾</p>",
        "</body></html>",
    ])
    return "".join(parts)


def human_date(iso_date: str) -> str:
    d = datetime.strptime(iso_date, "%Y-%m-%d")
    return d.strftime("%B %-d, %Y")


def build_message(digest: dict, items: list[dict], recipients: list[str]) -> EmailMessage:
    msg = EmailMessage()
    _, _, login, _ = smtp_settings()
    msg["Subject"] = digest["title"]
    msg["From"] = login
    msg["To"] = ", ".join(recipients)
    msg.set_content(render_plain(digest, items))
    msg.add_alternative(render_html(digest, items), subtype="html")
    return msg


def send_message(msg: EmailMessage):
    host, port, login, password = smtp_settings()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as s:
        s.login(login, password)
        s.send_message(msg)


def main():
    args = parse_args()
    digest_date = pick_date(args.date)
    digest_path = DIGEST_DIR / f"{digest_date}.md"
    if not digest_path.exists():
        raise SystemExit(f"Digest not found: {digest_path}")
    digest = parse_digest(digest_path)
    items = build_items(digest)
    validate_digest_structure(digest, items)
    recipients = read_recipients(args.to, internal_test=args.internal_test)
    msg = build_message(digest, items, recipients)
    validate_rendered_message(msg, recipients, internal_test=args.internal_test)
    verify_web_links_before_send(digest, items)
    if args.preview_path:
        Path(args.preview_path).write_text(msg.as_string(), encoding="utf-8")
    if args.dry_run or args.preview_path:
        if args.dry_run:
            print(msg.as_string())
        else:
            print(f"PREVIEW_WRITTEN {args.preview_path}")
        return
    send_message(msg)
    print(f"SENT {digest['date']} to {len(recipients)} recipient(s)")


if __name__ == "__main__":
    main()
