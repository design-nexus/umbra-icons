#!/usr/bin/env python3
"""Regenerate symbolic/: Umbra's symbolic icons as filled outlines.

GTK colours a symbolic icon by filling every shape in it, so 1.6 px strokes have to be
turned into filled outlines first. Needs skia-pathops (tools/requirements.txt), only to
regenerate; the results are committed.

    uv run --with skia-pathops tools/outline.py
"""
import math
import re
import shutil
import sys
from pathlib import Path

import pathops

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from umbra.symbolic_src import FILLED, ICONS, path  # noqa: E402

OUT = ROOT / "symbolic"
WIDTH = 1.6

TOKEN = re.compile(r"[MmLlHhVvCcSsQqTtAaZz]|-?(?:\d+\.?\d*|\.\d+)(?:e-?\d+)?")


def _arc_to_cubics(x1, y1, rx, ry, phi, large, sweep, x2, y2):
    """SVG arc endpoint form → cubic Béziers (the SVG spec's conversion)."""
    if rx == 0 or ry == 0:
        return [(x1, y1, x2, y2, x2, y2)]
    rx, ry = abs(rx), abs(ry)
    cp, sp = math.cos(math.radians(phi)), math.sin(math.radians(phi))
    dx, dy = (x1 - x2) / 2, (y1 - y2) / 2
    x1p, y1p = cp * dx + sp * dy, -sp * dx + cp * dy
    lam = x1p ** 2 / rx ** 2 + y1p ** 2 / ry ** 2
    if lam > 1:
        rx, ry = rx * math.sqrt(lam), ry * math.sqrt(lam)
    num = rx ** 2 * ry ** 2 - rx ** 2 * y1p ** 2 - ry ** 2 * x1p ** 2
    den = rx ** 2 * y1p ** 2 + ry ** 2 * x1p ** 2
    coef = math.sqrt(max(0, num / den)) if den else 0
    if large == sweep:
        coef = -coef
    cxp, cyp = coef * rx * y1p / ry, -coef * ry * x1p / rx
    cx, cy = cp * cxp - sp * cyp + (x1 + x2) / 2, sp * cxp + cp * cyp + (y1 + y2) / 2

    def ang(ux, uy, vx, vy):
        a = math.atan2(ux * vy - uy * vx, ux * vx + uy * vy)
        return a

    t1 = ang(1, 0, (x1p - cxp) / rx, (y1p - cyp) / ry)
    dt = ang((x1p - cxp) / rx, (y1p - cyp) / ry, (-x1p - cxp) / rx, (-y1p - cyp) / ry)
    if not sweep and dt > 0:
        dt -= 2 * math.pi
    elif sweep and dt < 0:
        dt += 2 * math.pi
    n = max(1, math.ceil(abs(dt) / (math.pi / 2)))
    step = dt / n
    k = 4 / 3 * math.tan(step / 4)
    out = []
    for i in range(n):
        a1, a2 = t1 + i * step, t1 + (i + 1) * step
        e1x, e1y = math.cos(a1), math.sin(a1)
        e2x, e2y = math.cos(a2), math.sin(a2)
        p = [(e1x - k * e1y, e1y + k * e1x), (e2x + k * e2y, e2y - k * e2x), (e2x, e2y)]
        pts = []
        for ux, uy in p:
            ux, uy = ux * rx, uy * ry
            pts += [cp * ux - sp * uy + cx, sp * ux + cp * uy + cy]
        out.append(tuple(pts))
    return out


def to_path(d):
    """SVG path data → a pathops Path (open subpaths stay open, for stroking)."""
    p = pathops.Path()
    toks = TOKEN.findall(d)
    i, cmd = 0, None
    x = y = sx = sy = 0.0
    last_c = None  # last control point, for S/T
    started = False

    def num():
        nonlocal i
        v = float(toks[i])
        i += 1
        return v

    while i < len(toks):
        if toks[i].isalpha():
            cmd = toks[i]
            i += 1
            if cmd in "Zz":
                p.close()
                x, y = sx, sy
                last_c = None
                continue
        rel = cmd.islower()
        c = cmd.upper()
        ox, oy = (x, y) if rel else (0, 0)
        if c == "M":
            x, y = num() + ox, num() + oy
            p.moveTo(x, y)
            sx, sy, started = x, y, True
            cmd = "l" if rel else "L"
            last_c = None
        elif c == "L":
            x, y = num() + ox, num() + oy
            p.lineTo(x, y)
            last_c = None
        elif c == "H":
            x = num() + (x if rel else 0)
            p.lineTo(x, y)
            last_c = None
        elif c == "V":
            y = num() + (y if rel else 0)
            p.lineTo(x, y)
            last_c = None
        elif c == "C":
            x1, y1, x2, y2 = num() + ox, num() + oy, num() + ox, num() + oy
            x, y = num() + ox, num() + oy
            p.cubicTo(x1, y1, x2, y2, x, y)
            last_c = (x2, y2)
        elif c == "S":
            x1, y1 = (2 * x - last_c[0], 2 * y - last_c[1]) if last_c else (x, y)
            x2, y2 = num() + ox, num() + oy
            x, y = num() + ox, num() + oy
            p.cubicTo(x1, y1, x2, y2, x, y)
            last_c = (x2, y2)
        elif c == "Q":
            x1, y1 = num() + ox, num() + oy
            x, y = num() + ox, num() + oy
            p.quadTo(x1, y1, x, y)
            last_c = (x1, y1)
        elif c == "T":
            x1, y1 = (2 * x - last_c[0], 2 * y - last_c[1]) if last_c else (x, y)
            x, y = num() + ox, num() + oy
            p.quadTo(x1, y1, x, y)
            last_c = (x1, y1)
        elif c == "A":
            rx, ry, phi = num(), num(), num()
            large, sweep = int(num()), int(num())
            x2, y2 = num() + ox, num() + oy
            for seg in _arc_to_cubics(x, y, rx, ry, phi, large, sweep, x2, y2):
                p.cubicTo(*seg)
            x, y = x2, y2
            last_c = None
        else:
            raise ValueError(f"unknown command {cmd} in {d!r}")
    assert started
    return p


def outline(d, width=WIDTH, filled=False):
    p = to_path(d)
    p.stroke(width, pathops.LineCap.ROUND_CAP, pathops.LineJoin.ROUND_JOIN, 4)
    p.convertConicsToQuads(0.02)
    if filled:
        inside = to_path(d)
        inside.close()
        p = pathops.op(p, inside, pathops.PathOp.UNION, fix_winding=True)
    p.simplify(fix_winding=True)
    return p


def svg_d(p):
    """Path → SVG data. Quadratic runs come TrueType-style: several off-curve points
    with implied on-curve midpoints, and None for a closing point."""
    parts = []
    for verb, pts in p.segments:
        if verb == "moveTo":
            parts.append("M" + _pts(pts))
        elif verb == "lineTo":
            parts.append("L" + _pts(pts))
        elif verb == "curveTo":
            parts.append("C" + _pts(pts))
        elif verb == "qCurveTo":
            offs, end = list(pts[:-1]), pts[-1]
            if end is None:
                # A closed contour of only off-curve points: it starts and ends at the
                # midpoint between its last and first.
                end = ((offs[-1][0] + offs[0][0]) / 2, (offs[-1][1] + offs[0][1]) / 2)
                if not parts or parts[-1] == "Z":
                    parts.append("M" + _pts([end]))
            for i, off in enumerate(offs):
                on = end if i == len(offs) - 1 else ((off[0] + offs[i + 1][0]) / 2, (off[1] + offs[i + 1][1]) / 2)
                parts.append("Q" + _pts([off, on]))
        elif verb == "closePath":
            parts.append("Z")
    return "".join(parts)


def _fmt(v):
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def _pts(pts):
    return " ".join(f"{_fmt(x)} {_fmt(y)}" for x, y in pts)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    seen = set()
    count = 0
    for context, names, key in ICONS:
        names = [n for n in names if n not in seen]
        if not names:
            continue
        seen.update(names)
        d = svg_d(outline(path(key), filled=key in FILLED))
        target = OUT / context / f"{names[0]}-symbolic.svg"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24">'
                          f'<path fill="#2e3436" d="{d}"/></svg>\n')
        for alias in names[1:]:
            (OUT / context / f"{alias}-symbolic.svg").symlink_to(target.name)
        count += len(names)
    print(f"{count} symbolic names")


if __name__ == "__main__":
    main()
