"""The colours Umbra draws in: a background, text, an accent and nine swatches.

From a palette file (`{"bg", "text", "accent", "light", "swatches": {...}}`, what Nyx
writes for the active theme), else Omarchy's current colors.toml, else Nyx Dark.
"""
import colorsys
import json
import os
from pathlib import Path
import tomllib

SWATCH_NAMES = ["blue", "violet", "pink", "red", "coral", "amber", "green", "teal", "graphite"]

NYX_DARK = {
    "name": "Nyx Dark", "light": False, "bg": "#09090a", "text": "#e8e8ea", "accent": "#5b9cff",
    "swatches": dict(zip(SWATCH_NAMES, ["#5b9cff", "#9d7bff", "#ff6fae", "#ff6b6b", "#ff7a59", "#f2b545", "#46d08a",
                                        "#4cc9d6", "#a3a3ab"])),
}
NYX_LIGHT = {
    "name": "Nyx Light", "light": True, "bg": "#f7f7f8", "text": "#18181b", "accent": "#2f6fea",
    "swatches": dict(zip(SWATCH_NAMES, ["#2f6fea", "#6f4de0", "#c93a7b", "#d93a3a", "#d4532f", "#b7791f", "#1f9e5c",
                                        "#1a8fa0", "#5a5a64"])),
}
OMARCHY_SWATCHES = [("blue", "blue"), ("violet", "magenta"), ("pink", "bright_magenta"), ("red", "red"),
                    ("coral", "orange"), ("amber", "yellow"), ("green", "green"), ("teal", "cyan"),
                    ("graphite", "dark_foreground")]


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def rgb_hex(rgb):
    return "#" + "".join(f"{round(max(0, min(1, c)) * 255):02x}" for c in rgb)


def mix(a, b, t):
    """`a` moved `t` of the way to `b`."""
    ra, rb = hex_rgb(a), hex_rgb(b)
    return rgb_hex(tuple(x + (y - x) * t for x, y in zip(ra, rb)))


def luminance(h):
    r, g, b = hex_rgb(h)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def lighten(h, amount):
    r, g, b = hex_rgb(h)
    hue, light, sat = colorsys.rgb_to_hls(r, g, b)
    return rgb_hex(colorsys.hls_to_rgb(hue, max(0, min(1, light + amount)), sat))


def _valid(value):
    if isinstance(value, str) and value.startswith("#") and len(value) in (4, 7, 9):
        if len(value) == 4:
            value = "#" + "".join(c * 2 for c in value[1:])
        return value[:7].lower()
    return None


def from_file(path):
    data = json.loads(Path(path).read_text())
    base = NYX_LIGHT if data.get("light") else NYX_DARK
    swatches = dict(base["swatches"])
    swatches.update({k: v for k, v in (data.get("swatches") or {}).items() if k in SWATCH_NAMES and _valid(v)})
    return {
        "name": data.get("name", "custom"),
        "light": bool(data.get("light", False)),
        "bg": _valid(data.get("bg")) or base["bg"],
        "text": _valid(data.get("text")) or base["text"],
        "accent": _valid(data.get("accent")) or base["accent"],
        "swatches": swatches,
    }


def omarchy_colors():
    state = Path(os.environ.get("XDG_STATE_HOME", Path.home() / ".local/state"))
    config = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))
    for path in (state / "omarchy/current/theme/colors.toml", config / "omarchy/current/theme/colors.toml"):
        if path.is_file():
            return path
    return None


def from_omarchy(path):
    data = tomllib.loads(Path(path).read_text())
    bg = _valid(data.get("background")) or NYX_DARK["bg"]
    light = data.get("mode") == "light" if "mode" in data else luminance(bg) > 0.5
    base = NYX_LIGHT if light else NYX_DARK
    swatches = {name: _valid(data.get(key)) or base["swatches"][name] for name, key in OMARCHY_SWATCHES}
    # Omarchy's magenta is often pink; keep violet distinct from it.
    if swatches["violet"] == swatches["pink"]:
        swatches["violet"] = mix(swatches["blue"], swatches["pink"], 0.5)
    return {
        "name": "Omarchy",
        "light": light,
        "bg": bg,
        "text": _valid(data.get("foreground")) or base["text"],
        "accent": _valid(data.get("accent")) or swatches["blue"],
        "swatches": swatches,
    }


def resolve(path=None, source=None):
    """The palette to draw with: a file, `nyx-dark`/`nyx-light`, or the current Omarchy theme."""
    if source == "nyx-dark":
        return NYX_DARK
    if source == "nyx-light":
        return NYX_LIGHT
    if path:
        return from_file(path)
    omarchy = omarchy_colors()
    return from_omarchy(omarchy) if omarchy else NYX_DARK


def colour(palette, name):
    if name in (None, "accent"):
        return palette["accent"]
    return palette["swatches"].get(name, name)


def surfaces(palette):
    """The satin colours derived from the background: tile and folder faces."""
    bg, text = palette["bg"], palette["text"]
    if palette["light"]:
        return {
            "tile_top": mix(bg, "#ffffff", 0.85), "tile_bottom": mix(bg, text, 0.08),
            "face_top": mix(bg, "#ffffff", 0.9), "face_bottom": mix(bg, text, 0.07),
            "back": mix(bg, text, 0.16), "fold": mix(bg, text, 0.14),
            "on_colour": "#ffffff", "neutral": mix(text, bg, 0.35),
        }
    return {
        "tile_top": mix(bg, text, 0.13), "tile_bottom": mix(bg, text, 0.04),
        "face_top": mix(bg, text, 0.21), "face_bottom": mix(bg, text, 0.10),
        "back": mix(bg, text, 0.15), "fold": mix(bg, text, 0.28),
        "on_colour": bg, "neutral": mix(text, bg, 0.35),
    }
