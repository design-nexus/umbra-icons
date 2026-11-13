"""The looks: Tile (the default), Solid, Line, Tinted, Frame and Colour.

Every icon is drawn on a 128 px canvas for a given size: small sizes drop fine detail
and keep strokes at least a pixel and a bit wide; Line thins its strokes at large sizes.
Tinted and Frame are Tile on another tile; Colour puts a white shape on a tile in the
icon's colour.
"""
from .glyphs import BRAND, G, LANG, label, text_width
from .palette import colour, mix, surfaces

LOOKS = ["tile", "solid", "line", "tinted", "frame", "colour"]
SCALABLE = 96  # what "scalable" is drawn for


def _px(size):
    return SCALABLE if size == "scalable" else size


def _w(canvas_width, size, min_px):
    """A stroke `canvas_width` wide on the 128 canvas, but at least `min_px` on screen."""
    return max(canvas_width, min_px * 128 / _px(size))


def stroke(d, col, width):
    return (f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{width:.3f}" stroke-linecap="round" '
            f'stroke-linejoin="round"/>')


def placed(inner, x, y, s):
    return f'<g transform="translate({x:g} {y:g}) scale({s:g})">{inner}</g>'


def glyph(name, col, x, y, s, canvas_width):
    """Glyph `name` at (x, y), `s` times its 24 px size, with a stroke `canvas_width` wide."""
    return placed(stroke(G[name], col, canvas_width / s), x, y, s)


def brand(name, on_light=False):
    """A cloud-drive mark. GitHub's is one colour by its own rules: dark on light
    surfaces, light on dark ones."""
    if name == "github" and on_light:
        return BRAND[name].replace("#e8e8ea", "#1f2328")
    return BRAND[name]


def mark(m, palette, x, y, s, canvas_width, col, on_light=False):
    if m.startswith("brand:"):
        return placed(brand(m[6:], on_light), x, y, s)
    if m.startswith("lang:"):
        return placed(LANG[m[5:]][0](), x, y, s)
    return glyph(m, col, x, y, s, canvas_width)


def svg(body, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128">'
            f'{"<defs>" + defs + "</defs>" if defs else ""}{body}</svg>\n')


def spec_colour(spec, palette):
    m = spec.get("mark") or ""
    if m.startswith("lang:"):
        return LANG[m[5:]][1]
    if m.startswith("brand:"):
        return surfaces(palette)["neutral"]
    return colour(palette, spec.get("colour"))


# ---------- Tile ----------

def _tile(palette, accent, inner, size=None, top=None, bottom=None, rim=0.3):
    s = surfaces(palette)
    glow = 0.14 if palette["light"] else 0.2
    defs = (f'<linearGradient id="t" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top or s["tile_top"]}"/>'
            f'<stop offset="1" stop-color="{bottom or s["tile_bottom"]}"/></linearGradient>'
            f'<radialGradient id="g" cx=".18" cy=".1" r=".75"><stop offset="0" stop-color="{accent}" stop-opacity="{glow}"/>'
            f'<stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>')
    body = ('<rect x="8" y="8" width="112" height="112" rx="28" fill="url(#t)"/>'
            '<rect x="8" y="8" width="112" height="112" rx="28" fill="url(#g)"/>'
            f'<rect x="8.5" y="8.5" width="111" height="111" rx="27.5" fill="none" stroke="{accent}" stroke-opacity="{rim}"/>'
            + inner)
    return svg(body, defs)


def tile(spec, palette, size, base=_tile):
    """Tile's glyph and mark on `base(palette, accent, inner, size)`: Tile's own satin
    tile, or Tinted's or Frame's."""
    kind, m = spec["kind"], spec.get("mark")
    col = spec_colour(spec, palette)
    small = _px(size) <= 22
    outline = _w(6, size, 1.3)
    inner_w = _w(3.8, size, 1.15)
    if kind == "folder":
        if m == "open":
            return base(palette, col, glyph("folder-open", col, 22, 20, 3.5, outline), size)
        body = glyph("folder", col, 22, 20, 3.5, outline)
        if m and not small:
            body += mark(m, palette, 47 if not m.startswith("brand:") else 46, 52, 1.42, inner_w, col)
        accent = palette["accent"] if m and m.startswith("brand:") else col
        return base(palette, accent, body, size)
    if kind == "file":
        if m.startswith("lang:") and small:
            return base(palette, col, mark(m, palette, 22, 22, 3.5, inner_w, col), size)
        body = glyph("page", col, 21, 18, 3.6, outline)
        if not small:
            body += mark(m, palette, 44, 50, 1.6, inner_w, col) if not m.startswith("lang:") else \
                mark(m, palette, 41, 44, 1.9, inner_w, col)
        return base(palette, col, body, size)
    return base(palette, col, glyph(m, col, 28, 28, 3, _w(4.8, size, 1.3)), size)


# ---------- Tinted and Frame: Tile on another tile ----------

def _tinted_tile(palette, accent, inner, size):
    """The satin tile washed with the icon's own colour."""
    s = surfaces(palette)
    if palette["light"]:
        top, bottom = mix(s["tile_top"], accent, 0.1), mix(s["tile_bottom"], accent, 0.16)
    else:
        top, bottom = mix(s["tile_top"], accent, 0.2), mix(s["tile_bottom"], accent, 0.1)
    return _tile(palette, accent, inner, size, top, bottom, rim=0.42)


def _frame_tile(palette, accent, inner, size):
    """No satin: the tile's outline in the icon's colour over a faint wash of it."""
    return svg(f'<rect x="10" y="10" width="108" height="108" rx="27" fill="{accent}" fill-opacity=".07" '
               f'stroke="{accent}" stroke-opacity=".6" stroke-width="{_w(3, size, 1):.2f}"/>' + inner)


def tinted(spec, palette, size):
    return tile(spec, palette, size, _tinted_tile)


def frame(spec, palette, size):
    return tile(spec, palette, size, _frame_tile)


# ---------- Colour: a white shape on a tile in the icon's colour ----------

_SHAPE = 'transform="translate(64 64) scale(.62) translate(-64 -64)"'
_PAGE_SHAPE = 'transform="translate(64 66) scale(.6) translate(-64 -65)"'
_SQUIRCLE = 'x="8" y="8" width="112" height="112" rx="28"'


def _colour_tile(col, inner, size):
    defs = (f'<linearGradient id="t" x1="0" y1="0" x2=".6" y2="1"><stop offset="0" stop-color="{mix(col, "#ffffff", 0.14)}"/>'
            f'<stop offset="1" stop-color="{mix(col, "#000000", 0.2)}"/></linearGradient>'
            '<radialGradient id="s" cx=".2" cy=".05" r=".8"><stop offset="0" stop-color="#ffffff" stop-opacity=".28"/>'
            '<stop offset="1" stop-color="#ffffff" stop-opacity="0"/></radialGradient>')
    rim = '' if _px(size) <= 22 else ('<rect x="8.75" y="8.75" width="110.5" height="110.5" rx="27.25" fill="none" '
                                       'stroke="#ffffff" stroke-opacity=".22" stroke-width="1.5"/>')
    return svg(f'<rect {_SQUIRCLE} fill="url(#t)"/><rect {_SQUIRCLE} fill="url(#s)"/>{rim}{inner}', defs)


def _centred(m, palette, cx, cy, s, canvas_width, col):
    return mark(m, palette, cx - 12 * s, cy - 12 * s, s, canvas_width, col, on_light=True)


def colour_tile(spec, palette, size):
    kind, m = spec["kind"], spec.get("mark")
    small = _px(size) <= 22
    if kind == "folder":
        brand_mark = bool(m and m.startswith("brand:"))
        col = palette["accent"] if brand_mark else colour(palette, spec.get("colour"))
        front = FOLDER_FRONT_OPEN if m == "open" else FOLDER_FRONT
        inner = (f'<g {_SHAPE}><path d="{FOLDER_BACK}" fill="#ffffff" fill-opacity=".6"/>'
                 f'<path d="{front}" fill="#ffffff"/></g>')
        if m and m != "open" and not small:
            inner += _centred(m, palette, 64, 70, 1.35 if brand_mark else 1.5, _w(4.2, size, 1.1),
                              mix(col, "#000000", 0.08))
        return _colour_tile(col, inner, size)
    col = spec_colour(spec, palette)
    if kind == "file":
        lang = m.startswith("lang:")
        if lang and small:
            return svg(f'<rect {_SQUIRCLE} fill="#ffffff"/>' + placed(LANG[m[5:]][0](), 16, 16, 4))
        inner = (f'<g {_PAGE_SHAPE}><path d="{PAGE}" fill="#ffffff"/>'
                 f'<path d="{FOLD}" fill="{mix(col, "#ffffff", 0.45)}"/></g>')
        if not small:
            inner += _centred(m, palette, 64, 72, 1.6 if lang else 1.7, _w(4.2, size, 1.1), mix(col, "#000000", 0.08))
        return _colour_tile(col, inner, size)
    return _colour_tile(col, _centred(m, palette, 64, 64, 2.9, _w(5, size, 1.3), "#ffffff"), size)


# ---------- Solid ----------

FOLDER_BACK = ("M10 30a10 10 0 0 1 10-10h28a6 6 0 0 1 4.6 2.2l5 5.6a6 6 0 0 0 4.6 2.2H108a10 10 0 0 1 10 10v56"
               "a10 10 0 0 1-10 10H20a10 10 0 0 1-10-10z")
FOLDER_FRONT = "M8 46a9 9 0 0 1 9-9h94a9 9 0 0 1 9 9v52a10 10 0 0 1-10 10H18a10 10 0 0 1-10-10z"
FOLDER_FRONT_OPEN = "M8 50a9 9 0 0 1 8.4-9l96-6.4a8 8 0 0 1 8.5 9.2L113.6 99a10 10 0 0 1-9.9 9H18a10 10 0 0 1-10-10z"
PAGE = "M32 10h44l28 28v74a8 8 0 0 1-8 8H32a8 8 0 0 1-8-8V18a8 8 0 0 1 8-8z"
FOLD = "M76 10v20a8 8 0 0 0 8 8h20z"


def _face_defs(palette, col, light_glow):
    s = surfaces(palette)
    return (f'<linearGradient id="f" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{s["face_top"]}"/>'
            f'<stop offset="1" stop-color="{s["face_bottom"]}"/></linearGradient>'
            f'<radialGradient id="g" cx=".15" cy="0" r=".8"><stop offset="0" stop-color="{col}" stop-opacity="{light_glow}"/>'
            f'<stop offset="1" stop-color="{col}" stop-opacity="0"/></radialGradient>')


def solid(spec, palette, size):
    kind, m = spec["kind"], spec.get("mark")
    s = surfaces(palette)
    small = _px(size) <= 22
    inner_w = _w(3.6, size, 1.15)
    if kind == "folder":
        brand = bool(m and m.startswith("brand:"))
        col = palette["accent"] if brand else colour(palette, spec.get("colour"))
        glow = 0.14 if palette["light"] else 0.28
        front = FOLDER_FRONT_OPEN if m == "open" else FOLDER_FRONT
        body = (f'<path d="{FOLDER_BACK}" fill="{s["back"]}"/><path d="{front}" fill="url(#f)"/>'
                f'<path d="{front}" fill="url(#g)"/>')
        if m != "open":
            body += (f'<path d="M17 37.5h94a8.5 8.5 0 0 1 8.5 8.5" fill="none" stroke="{col}" stroke-opacity=".8" '
                     f'stroke-width="{_w(1.5, size, .8):.2f}" stroke-linecap="round"/>')
        if m and m != "open" and not small:
            body += mark(m, palette, 46 if brand else 44, 54 if brand else 52, 1.5 if brand else 1.65, inner_w, col)
        return svg(body, _face_defs(palette, col, glow))
    if kind == "file":
        lang = m.startswith("lang:")
        col = spec_colour(spec, palette)
        text = LANG[m[5:]][2] if lang else spec.get("label") or ""
        body = (f'<path d="{PAGE}" fill="url(#f)"/><path d="M32 10.5h44" stroke="{col}" stroke-opacity=".45"/>'
                f'<path d="{FOLD}" fill="{s["fold"]}"/>')
        if small:
            body += (mark(m, palette, 36, 40, 2.3, inner_w, col) if lang
                     else f'<rect x="32" y="78" width="64" height="26" rx="7" fill="{col}"/>')
            return svg(body, _face_defs(palette, col, 0))
        body += mark(m, palette, 41, 30, 1.9, inner_w, col) if lang else mark(m, palette, 38, 30, 1.55, inner_w, col)
        if _px(size) >= 32 and text:
            h = 11 if len(text) <= 3 else 9.5
            w = max(40, text_width(text, h) + 18)
            body += (f'<rect x="{64 - w / 2:.1f}" y="85" width="{w:.1f}" height="23" rx="6.5" fill="{col}"/>'
                     + label(text, 64, 96.5, h, s["on_colour"], weight=_w(2.2, size, .9)))
        else:
            body += f'<rect x="38" y="88" width="52" height="18" rx="6" fill="{col}"/>'
        return svg(body, _face_defs(palette, col, 0))
    # Devices, status and apps: the tile, as in the default look.
    return tile(spec, palette, size)


# ---------- Line ----------

def _line_width(size):
    """Stroke in 24-grid units: 1.6 px at 24 px, a little more when small, thinner when large."""
    px = _px(size)
    if px <= 16:
        return 1.9
    if px <= 24:
        return 1.6
    if px <= 32:
        return 1.5
    if px <= 48:
        return 1.35
    return 1.1


def line(spec, palette, size):
    kind, m = spec["kind"], spec.get("mark")
    col = spec_colour(spec, palette)
    small = _px(size) <= 22
    k = 5  # the 24 grid fills the canvas
    w = _line_width(size) * k
    inner = w * 0.8
    if kind == "folder":
        if m == "open":
            return svg(glyph("folder-open", col, 4, 4, k, w))
        body = glyph("folder", col, 4, 4, k, w)
        if m and not small:
            body += mark(m, palette, 45 if m.startswith("brand:") else 43, 51, 1.6 if m.startswith("brand:") else 1.75,
                         inner, col)
        return svg(body)
    if kind == "file":
        if m.startswith("lang:") and small:
            return svg(mark(m, palette, 4, 4, k, inner, col))
        body = glyph("page", col, 4, 4, k, w)
        if not small:
            body += mark(m, palette, 42, 50, 1.8, inner, col) if not m.startswith("lang:") else \
                mark(m, palette, 39, 42, 2.1, inner, col)
        return svg(body)
    return svg(glyph(m, col, 4, 4, k, w))


RENDER = {"tile": tile, "solid": solid, "line": line, "tinted": tinted, "frame": frame, "colour": colour_tile}


def render(look, spec, palette, size):
    return RENDER[look](spec, palette, size)
