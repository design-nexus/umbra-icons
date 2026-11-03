#!/usr/bin/env python3
"""A contact sheet of every full-colour icon in each look, as an HTML page (and a PNG
with --png). For checking the drawings; nothing opens on screen.

    tools/sheet.py [--palette nyx-dark|nyx-light|FILE] [--size N] [--only folders|files|langs|devices] OUT.html
"""
import argparse
import base64
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from umbra import catalog, looks, palette as pal  # noqa: E402


def data_uri(svg):
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--palette", default="nyx-dark")
    ap.add_argument("--size", default="64")
    ap.add_argument("--only")
    ap.add_argument("--png", action="store_true")
    a = ap.parse_args()
    p = pal.resolve(source=a.palette) if a.palette.startswith("nyx-") else pal.resolve(path=a.palette)
    shown = int(a.size)
    render_size = "scalable" if shown >= 64 else shown
    groups = {
        "folders": [(n[0], s) for c, n, s in catalog.full_colour() if s["kind"] == "folder"],
        "files": [(n[0], s) for c, n, s in catalog.full_colour() if s["kind"] == "file" and not s["mark"].startswith("lang:")],
        "langs": [(n[0], s) for c, n, s in catalog.full_colour() if s["kind"] == "file" and s["mark"].startswith("lang:")],
        "devices": [(n[0], s) for c, n, s in catalog.full_colour() if s["kind"] == "device"],
    }
    if a.only:
        groups = {a.only: groups[a.only]}
    rows = []
    for look in looks.LOOKS:
        rows.append(f"<h2>{look}</h2>")
        for g, items in groups.items():
            cells = "".join(
                f'<div><img width="{shown}" height="{shown}" src="{data_uri(looks.render(look, s, p, render_size))}">'
                f"<span>{n}</span></div>" for n, s in items)
            rows.append(f'<h3>{g}</h3><div class="grid">{cells}</div>')
    bg, fg = (p["bg"], p["text"])
    html = f"""<!doctype html><meta charset="utf-8"><style>
    body{{background:{bg};color:{fg};font:12px Inter,sans-serif;margin:16px}}
    .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax({max(shown + 20, 92)}px,1fr));gap:6px}}
    .grid div{{display:flex;flex-direction:column;align-items:center;gap:3px}}
    span{{font-size:10px;opacity:.7;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
    h2{{margin:18px 0 4px}} h3{{margin:8px 0 4px;opacity:.6;font-size:11px;text-transform:uppercase}}</style>
    {''.join(rows)}"""
    Path(a.out).write_text(html)
    if a.png:
        browser = shutil.which("chromium") or shutil.which("google-chrome-stable")
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run([browser, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                            "--no-first-run", f"--user-data-dir={tmp}", "--window-size=1500,2600",
                            "--virtual-time-budget=1500", f"--screenshot={Path(a.out).with_suffix('.png')}",
                            f"file://{Path(a.out).resolve()}"], capture_output=True, check=False)


if __name__ == "__main__":
    main()
