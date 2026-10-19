#!/usr/bin/env python3
"""Fill templates/*.html with values from config.json and write the finished
pages (plus style.css) to the repo root, where GitHub Pages serves them.

Usage:  python3 build.py
Re-run any time you edit config.json or a template.
"""
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATES = ROOT / "templates"
PAGES = ["index.html", "privacy.html", "terms.html"]


def main() -> int:
    config = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
    today = date.today()
    config["DATE"] = today.strftime("%B %-d, %Y") if sys.platform != "win32" else today.strftime("%B %d, %Y")
    config["YEAR"] = str(today.year)

    unresolved = set()
    for name in PAGES:
        text = (TEMPLATES / name).read_text(encoding="utf-8")

        def sub(match):
            key = match.group(1)
            if key in config:
                return str(config[key])
            unresolved.add(key)
            return match.group(0)

        text = re.sub(r"\{\{([A-Z_]+)\}\}", sub, text)
        (ROOT / name).write_text(text, encoding="utf-8")
        print(f"wrote {name}")

    shutil.copyfile(TEMPLATES / "style.css", ROOT / "style.css")
    print("wrote style.css")

    if unresolved:
        print("WARNING: no value in config.json for: " + ", ".join(sorted(unresolved)))
        return 1

    leftovers = [k for k, v in config.items() if isinstance(v, str) and ("[" in v or "example.com" in v or v.startswith("Your "))]
    if leftovers:
        print("Reminder: these config values still look like placeholders: " + ", ".join(leftovers))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
