"""Rebuild the artifact index page from template.html and data.json.

Usage: python3 build.py <template.html> <data.json> <out.html>
The template holds one /*DATA*/ marker; the entries replace it as JSON.
"""
import json, sys

tpl, data, out = sys.argv[1:4]
entries = json.load(open(data))
ids = [e["id"] for e in entries]
dupes = {i for i in ids if ids.count(i) > 1}
if dupes:
    sys.exit("duplicate ids: " + ", ".join(sorted(dupes)))
for e in entries:
    for k in ("id", "title", "description", "category", "format"):
        if not e.get(k):
            sys.exit(f"{e.get('id', '?')}: missing {k}")
    if not (e.get("href") or e.get("media")):
        sys.exit(f"{e['id']}: needs href or media")
html = open(tpl).read().replace("/*DATA*/", json.dumps(entries, ensure_ascii=False).replace("</", "<\\/"))
open(out, "w").write(html)
print(f"{len(entries)} entries -> {out}")
