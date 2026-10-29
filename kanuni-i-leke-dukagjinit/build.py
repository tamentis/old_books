"""Build the HTML pages of the Kanun from the Markdown sources.

Each language lives in its own directory (sq/, en/, fr/) with:

- front.md: title, introduction and editor's notes, with a <!-- toc --> marker
- kanuni.md: the text of the Kanun
- glossary.md: optional, appended at the end

Usage: python build.py <lang>     writes <lang>/index.html
       python build.py index      writes the landing page index.html
"""

import html
import re
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).parent

LANGS = {
    "sq": {
        "name": "Shqip",
        "title": "Kanuni i Lekë Dukagjinit",
        "contents": "Përmbajtja",
        "quotes": ("“", "”", "‘", "’"),
    },
    "en": {
        "name": "English",
        "title": "The Kanun of Lekë Dukagjini",
        "contents": "Contents",
        "quotes": ("“", "”", "‘", "’"),
    },
    "fr": {
        "name": "Français",
        "title": "Le Kanun de Lekë Dukagjini",
        "contents": "Table des matières",
        "quotes": ("«&nbsp;", "&nbsp;»", "‘", "’"),
    },
}


def available():
    return [lang for lang in LANGS if (ROOT / lang / "kanuni.md").exists()]


def to_html(text, lang):
    ldq, rdq, lsq, rsq = LANGS[lang]["quotes"]
    md = markdown.Markdown(
        extensions=["attr_list", "md_in_html", "smarty", "tables"],
        extension_configs={
            "smarty": {
                "substitutions": {
                    "left-double-quote": ldq,
                    "right-double-quote": rdq,
                    "left-single-quote": lsq,
                    "right-single-quote": rsq,
                }
            }
        },
    )
    body = md.convert(text)
    if lang == "fr":
        # French typography: narrow no-break space before ; : ! ? (text only, not tags).
        body = re.sub(
            r">[^<]+<",
            lambda m: re.sub(r" ([;:!?])", "&#8239;\\1", m.group(0)),
            body,
        )
    return body


HEADING_RE = re.compile(r"^(#{2,4}) (.*?) \{#([a-z0-9-]+)\}$", re.M)


def toc(text, lang):
    """Books are folded; chapters and sections are listed inside each."""
    out = [f'<nav class="toc">', f"<h2>{LANGS[lang]['contents']}</h2>"]
    book_open = False
    for level, title, anchor in HEADING_RE.findall(text):
        title = html.escape(title)
        link = f'<a href="#{anchor}">{title}</a>'
        if level == "##":
            if book_open:
                out.append("</ul></details>")
            out.append(f"<details><summary>{link}</summary><ul>")
            book_open = True
        elif level == "###":
            out.append(f"<li><strong>{link}</strong></li>")
        else:
            out.append(f"<li>{link}</li>")
    if book_open:
        out.append("</ul></details>")
    out.append("</nav>")
    return "\n".join(out)


def decorate(body):
    # § paragraphs get an anchor, the number links to itself.
    body = re.sub(
        r"<p><strong>§ (\d+)\.</strong>",
        r'<p class="para" id="p-\1"><a class="pnum" href="#p-\1">§ \1.</a>',
        body,
    )
    # Numbered and lettered items.
    body = re.sub(r"<p>(?=(?:\d+[.)]|[a-z]\)|[IVX]+\.) )", '<p class="item">', body)
    # Paragraphs that are a single maxim between quotes.
    body = re.sub(
        r"<p>((?:“|«&nbsp;)(?:[^<]|</?em>)*?(?:”|&nbsp;»)\.?(?: \[[^<]*\])?)</p>",
        r'<p class="maxim">\1</p>',
        body,
    )
    return body


def languages_nav(current, prefix):
    links = []
    for lang in available():
        name = LANGS[lang]["name"]
        if lang == current:
            links.append(f"<strong>{name}</strong>")
        else:
            links.append(f'<a href="{prefix}{lang}/" hreflang="{lang}">{name}</a>')
    return '<nav class="languages">' + "".join(links) + "</nav>"


def render(lang, title, languages, content):
    page = (ROOT / "template.html").read_text()
    return (
        page.replace("{lang}", lang)
        .replace("{title}", title)
        .replace("{languages}", languages)
        .replace("{content}", content)
    )


def build_lang(lang):
    src = ROOT / lang
    # The title line duplicates the one in front.md.
    kanuni = re.sub(r"\A# .*\n", "", (src / "kanuni.md").read_text())
    front = (src / "front.md").read_text() if (src / "front.md").exists() else ""
    glossary = (src / "glossary.md").read_text() if (src / "glossary.md").exists() else ""

    front_html = to_html(front, lang).replace("<!-- toc -->", toc(kanuni, lang))
    content = "\n".join(
        [front_html, decorate(to_html(kanuni, lang)), to_html(glossary, lang)]
    )
    page = render(lang, LANGS[lang]["title"], languages_nav(lang, "../"), content)
    (src / "index.html").write_text(page)


def build_index():
    text = (ROOT / "index.md").read_text()
    page = render("en", LANGS["sq"]["title"], "", to_html(text, "en"))
    (ROOT / "index.html").write_text(page)


if __name__ == "__main__":
    target = sys.argv[1]
    if target == "index":
        build_index()
    else:
        build_lang(target)
