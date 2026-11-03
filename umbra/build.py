"""Write the Umbra icon themes.

Umbra is the Tile look and holds the symbolic set; Umbra Solid and Umbra Line inherit
it for symbolic icons. Anything Umbra doesn't draw falls back to Adwaita, then hicolor.
"""
import json
import os
import shutil
import subprocess
from pathlib import Path

from . import catalog, looks

ROOT = Path(__file__).resolve().parent.parent
SYMBOLIC = ROOT / "symbolic"

THEMES = {
    "tile": ("Umbra", "Umbra"),
    "solid": ("Umbra-Solid", "Umbra Solid"),
    "line": ("Umbra-Line", "Umbra Line"),
}
FIXED = [16, 22, 24, 32, 48]
CONTEXTS = {"places": "Places", "mimetypes": "MimeTypes", "devices": "Devices", "status": "Status", "apps": "Applications"}
SYMBOLIC_CONTEXTS = {"actions": "Actions", "places": "Places", "mimetypes": "MimeTypes", "devices": "Devices",
                     "status": "Status", "apps": "Applications", "categories": "Categories", "emblems": "Emblems"}
COMMENT = "Satin icons for Nyx and Omarchy, in the colours of the current theme"


def theme_dir(look):
    return THEMES[look][0]


def _index(look, has_symbolic):
    dirs, sections = [], []
    for size in FIXED:
        for ctx, name in CONTEXTS.items():
            d = f"{size}x{size}/{ctx}"
            dirs.append(d)
            sections.append(f"[{d}]\nSize={size}\nContext={name}\nType=Fixed\n")
    for ctx, name in CONTEXTS.items():
        d = f"scalable/{ctx}"
        dirs.append(d)
        sections.append(f"[{d}]\nSize=64\nMinSize=56\nMaxSize=512\nContext={name}\nType=Scalable\n")
    if has_symbolic:
        for ctx, name in SYMBOLIC_CONTEXTS.items():
            d = f"symbolic/{ctx}"
            dirs.append(d)
            sections.append(f"[{d}]\nSize=16\nMinSize=8\nMaxSize=512\nContext={name}\nType=Scalable\n")
    inherits = "Adwaita,hicolor" if look == "tile" else "Umbra,Adwaita,hicolor"
    head = (f"[Icon Theme]\nName={THEMES[look][1]}\nComment={COMMENT}\nInherits={inherits}\nExample=folder\n"
            f"Directories={','.join(dirs)}\n")
    return head + "\n" + "\n".join(sections)


def _write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(text)
    tmp.replace(path)


def _link(path, target):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink() or path.exists():
        path.unlink()
    path.symlink_to(target)


def build_look(look, palette, out):
    """Write one look's theme under `out`; returns the number of icon names."""
    base = Path(out) / theme_dir(look)
    tmp = base.with_name(base.name + ".building")
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir(parents=True)
    count = 0
    for context, names, spec in catalog.full_colour():
        for size in FIXED + ["scalable"]:
            d = tmp / ("scalable" if size == "scalable" else f"{size}x{size}") / context
            first = d / f"{names[0]}.svg"
            _write(first, looks.render(look, spec, palette, size))
            for alias in names[1:]:
                _link(d / f"{alias}.svg", first.name)
        count += len(names)
    has_symbolic = look == "tile" and SYMBOLIC.is_dir()
    if has_symbolic:
        for src in SYMBOLIC.rglob("*.svg"):
            dest = tmp / "symbolic" / src.relative_to(SYMBOLIC)
            dest.parent.mkdir(parents=True, exist_ok=True)
            if src.is_symlink():
                _link(dest, os.readlink(src))
            else:
                shutil.copyfile(src, dest)
            count += 1
    _write(tmp / "index.theme", _index(look, has_symbolic))
    _write(tmp / "umbra.json", json.dumps({"look": look, "palette": palette}, indent=2) + "\n")
    # Swap in whole, so an app never reads a half-written theme.
    old = base.with_name(base.name + ".old")
    if old.exists():
        shutil.rmtree(old)
    if base.exists():
        base.rename(old)
    tmp.rename(base)
    if old.exists():
        shutil.rmtree(old)
    cache(base)
    return count


def cache(theme):
    if shutil.which("gtk-update-icon-cache"):
        subprocess.run(["gtk-update-icon-cache", "-f", "-q", "-t", str(theme)], check=False,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def build(palette, out, which=None):
    return {look: build_look(look, palette, out) for look in (which or looks.LOOKS)}
