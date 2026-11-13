"""Write the Umbra icon themes, or another family's drawn from the same catalog.

Umbra is the Tile look and holds the symbolic set; the other looks inherit it for
symbolic icons. Anything Umbra doesn't draw falls back to Adwaita, then hicolor.

A family (Umbra, or Vellum from vellum-icons) is its looks' theme folders and names,
a renderer, and the look that carries the symbolic set.
"""
import json
import os
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from . import catalog, looks

ROOT = Path(__file__).resolve().parent.parent
SYMBOLIC = ROOT / "symbolic"

THEMES = {
    "tile": ("Umbra", "Umbra"),
    "solid": ("Umbra-Solid", "Umbra Solid"),
    "line": ("Umbra-Line", "Umbra Line"),
    "tinted": ("Umbra-Tinted", "Umbra Tinted"),
    "frame": ("Umbra-Frame", "Umbra Frame"),
    "colour": ("Umbra-Colour", "Umbra Colour"),
}
FIXED = [16, 22, 24, 32, 48]
CONTEXTS = {"places": "Places", "mimetypes": "MimeTypes", "devices": "Devices", "status": "Status", "apps": "Applications"}
SYMBOLIC_CONTEXTS = {"actions": "Actions", "places": "Places", "mimetypes": "MimeTypes", "devices": "Devices",
                     "status": "Status", "apps": "Applications", "categories": "Categories", "emblems": "Emblems"}
COMMENT = "Satin icons for Nyx and Omarchy, in the colours of the current theme"


@dataclass(frozen=True)
class Family:
    id: str  # also the name of the stamp file each theme folder gets: <id>.json
    themes: dict  # look -> (theme folder, display name)
    render: Callable  # (look, spec, palette, size) -> SVG
    comment: str
    symbolic_look: str  # the look whose theme holds the symbolic set

    def theme_dir(self, look):
        return self.themes[look][0]


UMBRA = Family("umbra", THEMES, looks.render, COMMENT, "tile")


def theme_dir(look):
    return THEMES[look][0]


def _index(family, look, has_symbolic):
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
    holder = family.theme_dir(family.symbolic_look)
    inherits = "Adwaita,hicolor" if look == family.symbolic_look else f"{holder},Adwaita,hicolor"
    head = (f"[Icon Theme]\nName={family.themes[look][1]}\nComment={family.comment}\nInherits={inherits}\n"
            f"Example=folder\nDirectories={','.join(dirs)}\n")
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


def build_look(look, palette, out, family=UMBRA):
    """Write one look's theme under `out`; returns the number of icon names."""
    base = Path(out) / family.theme_dir(look)
    tmp = base.with_name(base.name + ".building")
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir(parents=True)
    count = 0
    for context, names, spec in catalog.full_colour():
        for size in FIXED + ["scalable"]:
            d = tmp / ("scalable" if size == "scalable" else f"{size}x{size}") / context
            first = d / f"{names[0]}.svg"
            _write(first, family.render(look, spec, palette, size))
            for alias in names[1:]:
                _link(d / f"{alias}.svg", first.name)
        count += len(names)
    has_symbolic = look == family.symbolic_look and SYMBOLIC.is_dir()
    if has_symbolic:
        for src in SYMBOLIC.rglob("*.svg"):
            dest = tmp / "symbolic" / src.relative_to(SYMBOLIC)
            dest.parent.mkdir(parents=True, exist_ok=True)
            if src.is_symlink():
                _link(dest, os.readlink(src))
            else:
                shutil.copyfile(src, dest)
            count += 1
    _write(tmp / "index.theme", _index(family, look, has_symbolic))
    _write(tmp / f"{family.id}.json", json.dumps({"look": look, "palette": palette}, indent=2) + "\n")
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


def build(palette, out, which=None, family=UMBRA):
    return {look: build_look(look, palette, out, family) for look in (which or family.themes)}
