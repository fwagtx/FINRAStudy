#!/usr/bin/env python3
"""Build app/index.html from chapters/*.md, CHEAT-SHEET.md and questions/question-bank.json.

Run from anywhere:  python3 app/build.py
Outputs:
  app/index.html          — full standalone page (open directly in a browser, works offline)
  app/artifact-body.html  — same page without the <html>/<head>/<body> skeleton (for publishing as a claude.ai artifact)
"""
import json, re, html, pathlib
import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
CH_DIR = ROOT / "chapters"
TEMPLATE = (ROOT / "app" / "template.html").read_text()

MD = lambda text: markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def build_chapter(path):
    text = path.read_text()
    title = re.match(r"#\s+(.*)", text).group(1).strip()
    num = int(re.match(r"Chapter (\d+)", title).group(1))
    name = title.split(":", 1)[1].strip()
    sections = []
    def add_ids(m):
        hashes, heading = m.group(1), m.group(2).strip()
        mm = re.match(r"(\d+(?:\.\d+)+)\s+(.*)", heading)
        if mm and len(hashes) in (2, 3):
            sid = "s" + mm.group(1).replace(".", "-")
            sections.append({"id": sid, "num": mm.group(1), "title": mm.group(2), "level": len(hashes)})
            return f'{hashes} <span class="secnum">{mm.group(1)}</span> {mm.group(2)} {{: id="{sid}"}}'
        return m.group(0)
    text = re.sub(r"^(#{2,3})\s+(.*)$", add_ids, text, flags=re.M)
    # convert the attr-list-ish marker into real ids after rendering
    body = MD(text)
    body = re.sub(r'<h([23])>(.*?)\s*\{: id="([^"]+)"\}</h\1>', r'<h\1 id="\3" data-sec="\3">\2</h\1>', body)
    body = re.sub(r"<h1>.*?</h1>", "", body, count=1)
    words = len(re.findall(r"\w+", path.read_text()))
    return {"num": num, "name": name, "file": path.name, "minutes": max(3, round(words / 200)),
            "sections": sections, "html": body}

chapters = [build_chapter(p) for p in sorted(CH_DIR.glob("*.md"))]
questions = json.loads((ROOT / "questions" / "question-bank.json").read_text())
cheat = MD((ROOT / "CHEAT-SHEET.md").read_text())

def embed(obj):
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")

page = (TEMPLATE.replace("/*CHAPTERS*/", embed(chapters))
        .replace("/*QUESTIONS*/", embed(questions))
        .replace("<!--CHEAT-->", cheat))

(ROOT / "app" / "artifact-body.html").write_text(page)
full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<style>[hidden]{display:none!important}body{margin:0}</style>\n' + page.split("</title>", 1)[0] + "</title>\n</head>\n<body>" +
        page.split("</title>", 1)[1] + "\n</body>\n</html>\n")
# title tag must be inside head: move it
m = re.search(r"<title>.*?</title>", page, re.S)
full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        f'{m.group(0)}\n<style>[hidden]{{display:none!important}}body{{margin:0}}</style>\n</head>\n<body>\n'
        + page.replace(m.group(0), "", 1) + "\n</body>\n</html>\n")
(ROOT / "app" / "index.html").write_text(full)
print(f"built {len(chapters)} chapters, {sum(len(c['sections']) for c in chapters)} sections, {len(questions)} questions")
