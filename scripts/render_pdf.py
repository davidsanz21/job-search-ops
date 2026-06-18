#!/usr/bin/env python3
"""
render_pdf.py — Markdown -> print-quality A4 PDF for the job-search-ops agent.

Presets
  cv          2–3 page CV: serif navy headings, identity header, right-aligned dates
  letter      1-page application letter
  cheatsheet  dense interview prep sheet: section bands, answer blocks, delivery notes

Usage
  python render_pdf.py INPUT.md --style cv -o OUTPUT.pdf
  python render_pdf.py INPUT.md --style cv -o cv.pdf --footer "Jane Doe"
  python render_pdf.py prep.md --style cheatsheet -o prep.pdf --footer "Interview Prep · Candidate"

Options
  --lang es            tighter typography for verbose languages (cv preset)
  --font-size 9.0      override body font size (pt)
  --line-height 1.32   override line height
  --footer "text"      footer text. cv: centered "<text> · CV · n / m" (default:
                       no name, just "CV · n / m"). cheatsheet: bottom-left label
                       (default: the document's H1 title).

The script prints the rendered page count; the calling agent must check it
against the length discipline (cv <= 3, letter <= 1, screen cheatsheet <= 2)
and restructure content rather than shrink type when over.

Markdown conventions handled:
  * leading HTML-comment metadata (<!-- ... -->), blockquote build-notes, and
    horizontal rules (---) are stripped; a leading H1 is stripped for cv/letter
    (the identity block renders the name instead)
  * the cv/letter identity block's second line is tagged as an italic subtitle;
    redundant <br> after the name/subtitle blocks is removed so spacing doesn't
    double-stack
  * lines starting with em-dash bullets ("— ") become standalone paragraphs
  * cv H3 role lines "Role — Company · Mon YYYY – Mon YYYY" split on the last
    " · " into a flex row with a right-aligned date
  * cheatsheet lines starting with "▸ " become styled delivery notes
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import markdown
from weasyprint import CSS, HTML

STYLE_DIR = Path(__file__).resolve().parent / "styles"

PRESETS = {
    "cv": {"font_size": 9.2, "line_height": 1.34},
    "cv_es": {"font_size": 9.0, "line_height": 1.32},
    "letter": {"font_size": 10.0, "line_height": 1.45},
    "cheatsheet": {"font_size": 8.8, "line_height": 1.32},
}

YEAR_RE = re.compile(r"(19|20)\d\d")


def strip_leading_meta(text: str, drop_h1: bool) -> str:
    """Remove leading blank lines, HTML comments, blockquote build-notes, horizontal
    rules, and (optionally) one H1 — everything before the real content starts."""
    lines = text.split("\n")
    i = 0
    h1_dropped = False
    while i < len(lines):
        ln = lines[i]
        stripped = ln.strip()
        # blank line
        if not stripped:
            i += 1
            continue
        # multi-line HTML comment: skip until the closing -->
        if stripped.startswith("<!--"):
            while i < len(lines) and "-->" not in lines[i]:
                i += 1
            i += 1  # consume the line containing -->
            continue
        # blockquote build-note (may wrap across lines, but each starts with >)
        if stripped.startswith(">"):
            i += 1
            continue
        # horizontal rule separator
        if stripped in ("---", "***", "___"):
            i += 1
            continue
        # optional single H1 title
        if drop_h1 and not h1_dropped and ln.startswith("# "):
            h1_dropped = True
            i += 1
            continue
        break
    return "\n".join(lines[i:])


def emdash_paragraphs(text: str) -> str:
    """Give '— ' bullet lines breathing room so markdown keeps them as separate <p>."""
    out: list[str] = []
    for ln in text.split("\n"):
        if ln.lstrip().startswith("— "):
            out.extend(["", ln, ""])
        else:
            out.append(ln)
    return "\n".join(out)


def identity_linebreaks(text: str) -> str:
    """cv/letter: keep the header block's lines (name / subtitle / contact) on
    separate lines by giving each a hard markdown line break."""
    lines = text.split("\n")
    block_end = 0
    for i, ln in enumerate(lines):
        if not ln.strip():
            block_end = i
            break
    else:
        block_end = len(lines)
    head = [ln.rstrip() + "  " for ln in lines[:block_end]]
    return "\n".join(head + lines[block_end:])


def split_role_dates(html: str) -> str:
    """cv preset: '<h3>Role — Co · Jan 2019 – Mar 2023</h3>' -> flex title/date row."""

    def repl(m: re.Match) -> str:
        inner = m.group(1)
        if " · " not in inner:
            return m.group(0)
        left, right = inner.rsplit(" · ", 1)
        if not YEAR_RE.search(right):
            return m.group(0)
        return (
            '<h3 class="role"><span class="role-title">%s</span>'
            '<span class="role-date">%s</span></h3>' % (left, right)
        )

    return re.sub(r"<h3>(.*?)</h3>", repl, html)


def tag_identity_block(html: str) -> str:
    """cv/letter: in the first identity paragraph, wrap the line after the name
    <strong> in a .subtitle span, then drop the redundant <br> that follows the
    name and the subtitle (both are display:block, so the <br> double-stacks)."""

    def tag_subtitle(m: re.Match) -> str:
        block = m.group(1)
        parts = block.split("<br />")
        if len(parts) >= 2:
            parts[1] = '<span class="subtitle">%s</span>' % parts[1].strip()
            return '<p class="identity">' + "<br />".join(parts) + "</p>"
        return m.group(0)

    html = re.sub(r'<p class="identity">(.*?)</p>', tag_subtitle, html, count=1, flags=re.S)
    html = html.replace("</strong><br />", "</strong>")
    html = html.replace("</span><br />", "</span>")
    return html


def first_h1_text(text: str) -> str:
    for ln in text.split("\n"):
        if ln.startswith("# "):
            return re.sub(r"[*_`]", "", ln[2:]).strip()
    return ""


def build_html(md_text: str, style: str) -> str:
    body = markdown.markdown(md_text, extensions=["extra", "sane_lists"])
    if style in ("cv", "letter"):
        body = body.replace("<p>", '<p class="identity">', 1)
        body = tag_identity_block(body)
        if style == "cv":
            body = split_role_dates(body)
    if style == "cheatsheet":
        body = body.replace("<p>▸", '<p class="delivery">▸')
    return "<html><body>%s</body></html>" % body


def override_css(style: str, font_size: float, line_height: float, footer: str) -> str:
    css = "body{font-size:%spt;line-height:%s;}" % (font_size, line_height)
    safe = footer.replace("\\", "\\\\").replace('"', '\\"') if footer else ""
    if style == "cv":
        # centered footer: "<name> · CV · n / m", or "CV · n / m" when no name given
        label = ('"%s · CV · "' % safe) if safe else '"CV · "'
        css += (
            "@page{@bottom-center{content:%s counter(page) \" / \" counter(pages);"
            "font-size:7.5pt;color:#999;font-family:'Liberation Sans',Arial,sans-serif;}}"
            % label
        )
    if style == "cheatsheet" and footer:
        css += (
            '@page{@bottom-left{content:"%s";font-size:7pt;color:#999;'
            "font-family:'Liberation Sans',Arial,sans-serif;}}" % safe
        )
    return css


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="Markdown file to render")
    ap.add_argument("-o", "--output", required=True, help="Output PDF path")
    ap.add_argument("--style", choices=["cv", "letter", "cheatsheet"], default="cv")
    ap.add_argument("--lang", default="en", help="Language code; 'es' (etc.) tightens the cv preset")
    ap.add_argument("--font-size", type=float, default=None)
    ap.add_argument("--line-height", type=float, default=None)
    ap.add_argument("--footer", default=None,
                    help="cv: name for the centered footer (optional). "
                         "cheatsheet: footer label (default: H1 title).")
    args = ap.parse_args()

    src = Path(args.input)
    if not src.exists():
        print("error: input not found: %s" % src, file=sys.stderr)
        return 2

    raw = src.read_text(encoding="utf-8")

    preset_key = args.style
    if args.style == "cv" and args.lang.lower().split("-")[0] not in ("en",):
        preset_key = "cv_es"
    preset = PRESETS[preset_key]
    font_size = args.font_size if args.font_size else preset["font_size"]
    line_height = args.line_height if args.line_height else preset["line_height"]

    footer = args.footer
    if args.style == "cheatsheet" and footer is None:
        footer = first_h1_text(raw)

    text = strip_leading_meta(raw, drop_h1=args.style in ("cv", "letter"))
    if args.style in ("cv", "letter"):
        text = identity_linebreaks(text)
    text = emdash_paragraphs(text)
    html = build_html(text, args.style)

    base_css = STYLE_DIR / ("%s.css" % args.style)
    stylesheets = [
        CSS(filename=str(base_css)),
        CSS(string=override_css(args.style, font_size, line_height, footer or "")),
    ]

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    doc = HTML(string=html).render(stylesheets=stylesheets)
    doc.write_pdf(str(out))
    pages = len(doc.pages)
    print("rendered %s -> %s (%d page%s, style=%s, %spt/%s)" % (
        src.name, out, pages, "s" if pages != 1 else "", args.style, font_size, line_height
    ))
    return 0


if __name__ == "__main__":
    sys.exit(main())
