#!/usr/bin/env python3
import argparse
import csv
import hashlib
import html
import json
import re
import smtplib
import ssl
import subprocess
import urllib.request
from datetime import date, datetime
from email.message import EmailMessage
from email.utils import getaddresses
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
STATE_DIR = ROOT / ".state"
SEND_STATE_PATH = STATE_DIR / "email_send_state.json"
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
REDACTED_EMAIL = "[redacted-email]"
SEND_STATE_VERSION = 2

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

    result["theme"] = strip_markdown_emphasis(" ".join(line.strip() for line in blocks.get("Theme", []) if line.strip()))
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
    if (
        re.match(r"^https://cabbageland\.github\.io/cabbageclaw-neuro-daily-web/(daily_papers|paper_notes|related_notes|related_work)/[^?#/]+$", url)
        and "." not in url.rsplit("/", 1)[-1]
    ):
        return url + ".md"
    return url


def public_app_route(url: str) -> str:
    if url.startswith(f"{SITE_BASE}/#/"):
        return url
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
            continue
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
    if not items:
        raise ValueError("No ranked papers with preserved note links were available for email rendering")
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


def normalize_email(email_address: str) -> str:
    return email_address.strip().lower()


def redact_email_text(text: str) -> str:
    return EMAIL_RE.sub(REDACTED_EMAIL, text)


def recipient_fingerprint(email_address: str) -> str:
    salted = f"neuro-daily-recipient:{normalize_email(email_address)}"
    return hashlib.sha256(salted.encode("utf-8")).hexdigest()[:16]


def assert_no_email_tokens(label: str, text: str):
    if EMAIL_RE.search(text):
        raise ValueError(f"{label} contains an unredacted email address")


def assert_no_known_recipient_addresses(label: str, text: str, recipients: list[str]):
    lowered = text.lower()
    leaked = [r for r in recipients if normalize_email(r) in lowered]
    if leaked:
        raise ValueError(f"{label} contains {len(leaked)} recipient email address(es)")


def read_recipients(extra: list[str], internal_test: bool = False) -> list[str]:
    if internal_test and extra:
        raise ValueError("Internal test mode only allows recipients-internal-test.csv recipients")
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
        key = normalize_email(r)
        if key not in seen:
            seen.add(key)
            deduped.append(r)
    if not deduped:
        raise ValueError("No recipients found. Populate recipients.csv or pass --to.")
    return deduped


def header_addresses(msg: EmailMessage, header: str) -> list[str]:
    return [normalize_email(addr) for _, addr in getaddresses(msg.get_all(header, [])) if addr]


def validate_recipient_privacy(messages: list[EmailMessage], recipients: list[str]):
    errors = []
    expected_recipients = [normalize_email(r) for r in recipients]
    if len(messages) != len(expected_recipients):
        errors.append(f"Expected {len(expected_recipients)} message(s), built {len(messages)}")

    for idx, msg in enumerate(messages):
        expected = expected_recipients[idx] if idx < len(expected_recipients) else None
        to_addrs = header_addresses(msg, "To")
        cc_addrs = header_addresses(msg, "Cc")
        bcc_addrs = header_addresses(msg, "Bcc")
        if expected and to_addrs != [expected]:
            errors.append(f"Message {idx + 1} must have exactly one To recipient")
        if cc_addrs:
            errors.append(f"Message {idx + 1} has Cc recipient(s)")
        if bcc_addrs:
            errors.append(f"Message {idx + 1} has Bcc recipient(s)")

        plain_part = msg.get_body(preferencelist=("plain",))
        html_part = msg.get_body(preferencelist=("html",))
        plain = plain_part.get_content() if plain_part else ""
        html_body = html_part.get_content() if html_part else ""
        assert_no_known_recipient_addresses(f"Message {idx + 1} body", plain + "\n" + html_body, recipients)

    if errors:
        raise ValueError("Recipient privacy gate failed: " + "; ".join(errors))


def validate_digest_structure(digest: dict, items: list[dict]):
    errors = []
    if len(items) < 3:
        errors.append(f"Expected at least 3 ranked papers with preserved notes, found {len(items)}")
    if len(items) > 4:
        errors.append(f"Expected at most 4 ranked papers in email, found {len(items)}")
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


def validate_rendered_message(msg: EmailMessage, recipients: list[str], internal_test: bool = False, expected_item_count: int = 4):
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
    expected_links = max(1 + expected_item_count * 2, 5)
    if html_body.count("<a href=") < expected_links:
        errors.append(f"HTML body has fewer hyperlinks than expected for {expected_item_count} items")
    if "Content-Type: multipart/alternative" not in msg.as_string().split("\n\n", 1)[0]:
        errors.append("Message is not multipart/alternative")
    if internal_test:
        allowed = {normalize_email(r) for r in read_recipients([], internal_test=True)}
        if any(normalize_email(r) not in allowed for r in recipients):
            errors.append("Internal test mode recipient is not in recipients-internal-test.csv")
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


def load_send_state() -> dict:
    if not SEND_STATE_PATH.exists():
        return {}
    try:
        return scrub_send_state(json.loads(read_text(SEND_STATE_PATH)))
    except Exception:
        return {}


def scrub_send_state(state: dict) -> dict:
    if not isinstance(state, dict):
        return {}
    for mode_data in state.values():
        if not isinstance(mode_data, dict):
            continue
        for sent in mode_data.values():
            if not isinstance(sent, dict):
                continue
            raw_recipients = sent.pop("recipients", None)
            if raw_recipients is not None:
                recipients = [str(r) for r in raw_recipients if str(r).strip()]
                sent["recipient_count"] = len(recipients)
                sent["recipient_fingerprints"] = [recipient_fingerprint(r) for r in recipients]
            sent.setdefault("recipient_count", 0)
            sent.setdefault("recipient_fingerprints", [])
            sent["state_version"] = SEND_STATE_VERSION
    return state


def save_send_state(state: dict):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    sanitized = scrub_send_state(state)
    serialized = json.dumps(sanitized, indent=2, sort_keys=True) + "\n"
    assert_no_email_tokens("Send state", serialized)
    SEND_STATE_PATH.write_text(serialized, encoding="utf-8")


def send_mode_key(internal_test: bool) -> str:
    return "internal_test" if internal_test else "production"


def assert_not_already_sent(digest_date: str, recipients: list[str], internal_test: bool = False):
    state = load_send_state()
    mode = send_mode_key(internal_test)
    sent = state.get(mode, {}).get(digest_date)
    if sent:
        prior_count = sent.get("recipient_count", 0)
        raise ValueError(
            f"Refusing duplicate send for {digest_date} in {mode} mode. "
            f"Already sent at {sent.get('sent_at')} to {prior_count} recipient(s)."
        )


def record_send(digest_date: str, recipients: list[str], internal_test: bool = False):
    state = load_send_state()
    mode = send_mode_key(internal_test)
    bucket = state.setdefault(mode, {})
    bucket[digest_date] = {
        "sent_at": datetime.now().isoformat(timespec="seconds"),
        "recipient_count": len(recipients),
        "recipient_fingerprints": [recipient_fingerprint(r) for r in recipients],
        "state_version": SEND_STATE_VERSION,
    }
    save_send_state(state)


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
    digest_url = public_app_route(f"{DIGEST_WEB_BASE}/{digest['date']}")
    lines = [
        "Hello!",
        "",
        f"Welcome to the {human_date(digest['date'])} Neuro Daily at Cabbageland: {digest_url}",
        "",
        digest["theme"],
        "",
    ]
    for item in items:
        notes_url = public_app_route(item["notes_url"])
        lines.extend([
            item["title"],
            f"Paper: {item['paper_url']}",
            f"Notes: {notes_url}",
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
    digest_url = public_app_route(f"{DIGEST_WEB_BASE}/{digest['date']}")
    parts = [
        "<html><body>",
        "<p>Hello!</p>",
        f"<p>Welcome to the <a href=\"{html.escape(digest_url)}\">{html.escape(human_date(digest['date']))} Neuro Daily</a> at Cabbageland.</p>",
        f"<p>{html.escape(digest['theme'])}</p>",
    ]
    for item in items:
        notes_url = public_app_route(item["notes_url"])
        parts.extend([
            f"<p><strong>{html.escape(item['title'])}</strong></p>",
            f"<p><strong>Paper:</strong> <a href=\"{html.escape(item['paper_url'])}\">{html.escape(item['paper_label'])}</a><br><strong>Notes:</strong> <a href=\"{html.escape(notes_url)}\">Cabbageland notes</a></p>",
            f"<p>{html.escape(item['body'])}</p>",
            f"<p><strong>Why it matters:</strong> {html.escape(item['why'])}</p>",
        ])
    parts.extend([
        f"<p><strong>Bottom line:</strong> {html.escape(digest['takeaway'])}</p>",
        "<p><strong>Yours,<br>cabbageclaw 🥬🐾</strong></p>",
        "</body></html>",
    ])
    return "".join(parts)


def human_date(iso_date: str) -> str:
    d = datetime.strptime(iso_date, "%Y-%m-%d")
    return d.strftime("%B %-d, %Y")


def build_message(digest: dict, items: list[dict], recipient: str) -> EmailMessage:
    msg = EmailMessage()
    _, _, login, _ = smtp_settings()
    msg["Subject"] = digest["title"]
    msg["From"] = login
    msg["To"] = recipient
    msg.set_content(render_plain(digest, items))
    msg.add_alternative(render_html(digest, items), subtype="html")
    return msg


def send_messages(messages: list[EmailMessage]):
    host, port, login, password = smtp_settings()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as s:
        s.login(login, password)
        for msg in messages:
            s.send_message(msg)


def serialized_redacted_messages(messages: list[EmailMessage]) -> str:
    serialized = "\n\n".join(redact_email_text(msg.as_string()) for msg in messages)
    assert_no_email_tokens("Redacted message preview", serialized)
    return serialized


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
    messages = [build_message(digest, items, recipient) for recipient in recipients]
    for msg in messages:
        validate_rendered_message(msg, [msg["To"]], internal_test=args.internal_test, expected_item_count=len(items))
    validate_recipient_privacy(messages, recipients)
    verify_web_links_before_send(digest, items)
    redacted_preview = None
    if args.preview_path:
        redacted_preview = serialized_redacted_messages(messages)
        Path(args.preview_path).write_text(redacted_preview, encoding="utf-8")
    if args.dry_run or args.preview_path:
        if args.dry_run:
            if redacted_preview is None:
                redacted_preview = serialized_redacted_messages(messages)
            print(redacted_preview)
        else:
            print(f"PREVIEW_WRITTEN {args.preview_path}")
        return
    assert_not_already_sent(digest["date"], recipients, internal_test=args.internal_test)
    send_messages(messages)
    record_send(digest["date"], recipients, internal_test=args.internal_test)
    print(f"SENT {digest['date']} to {len(recipients)} recipient(s) individually")


if __name__ == "__main__":
    main()
