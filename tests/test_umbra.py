"""Every icon renders, every look writes a valid theme, the symbolic set is GTK-ready."""
import re
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from umbra import build, catalog, looks, palette  # noqa: E402
from umbra.glyphs import BRAND, G, LANG  # noqa: E402
from umbra.symbolic_src import ICONS  # noqa: E402

PALETTES = [palette.NYX_DARK, palette.NYX_LIGHT]


class Render(unittest.TestCase):
    def test_every_icon_in_every_look_is_valid_svg(self):
        for p in PALETTES:
            for look in looks.LOOKS:
                for _, names, spec in catalog.full_colour():
                    for size in build.FIXED + ["scalable"]:
                        svg = looks.render(look, spec, p, size)
                        ET.fromstring(svg)  # raises on bad XML
                        self.assertIn('viewBox="0 0 128 128"', svg, names[0])

    def test_marks_exist(self):
        for _, _, spec in catalog.full_colour():
            m = spec.get("mark")
            if not m or m == "open":
                continue
            if m.startswith("brand:"):
                self.assertIn(m[6:], BRAND)
            elif m.startswith("lang:"):
                self.assertIn(m[5:], LANG)
            else:
                self.assertIn(m, G)

    def test_names_are_unique_within_a_context(self):
        seen = {}
        for context, names, _ in catalog.full_colour():
            for n in names:
                self.assertNotIn((context, n), seen, n)
                seen[(context, n)] = True

    def test_line_is_thinner_when_large(self):
        spec = {"kind": "folder", "mark": None, "colour": "blue"}
        width = lambda size: float(re.search(r'stroke-width="([\d.]+)"', looks.render("line", spec, palette.NYX_DARK, size)).group(1))
        self.assertLess(width("scalable"), width(24))

    def test_code_files_carry_their_language(self):
        names = {n for _, ns, s in catalog.full_colour() if s["mark"] and str(s["mark"]).startswith("lang:") for n in ns}
        for n in ["text-rust", "text-x-python", "text-x-go", "application-x-typescript", "text-javascript"]:
            self.assertIn(n, names)

    def test_home_folder_names_point_at_drawn_icons(self):
        drawn = {n for _, names, s in catalog.full_colour() for n in names}
        for icon in catalog.FOLDER_NAMES.values():
            self.assertIn(icon, drawn)


class Theme(unittest.TestCase):
    def test_build_writes_three_themes(self):
        with tempfile.TemporaryDirectory() as out:
            counts = build.build(palette.NYX_DARK, out)
            self.assertEqual(set(counts), {"tile", "solid", "line"})
            for look, (directory, name) in build.THEMES.items():
                index = (Path(out) / directory / "index.theme").read_text()
                self.assertIn(f"Name={name}", index)
                for d in re.search(r"Directories=(.*)", index).group(1).split(","):
                    self.assertIn(f"[{d}]", index)
            self.assertTrue((Path(out) / "Umbra/scalable/places/folder-games.svg").is_file())
            self.assertTrue((Path(out) / "Umbra-Line/16x16/mimetypes/text-rust.svg").is_file())
            self.assertTrue((Path(out) / "Umbra/symbolic/actions/edit-copy-symbolic.svg").is_file())
            self.assertIn("Inherits=Umbra,", (Path(out) / "Umbra-Solid/index.theme").read_text())


class Symbolic(unittest.TestCase):
    def test_symbolic_icons_are_filled_outlines(self):
        files = list((ROOT / "symbolic").rglob("*.svg"))
        self.assertGreater(len(files), 400)
        for f in files:
            text = f.read_text()
            self.assertNotIn("stroke", text, f.name)
            self.assertRegex(text, r'd="M', f.name)

    def test_every_source_is_written(self):
        written = {f.name for f in (ROOT / "symbolic").rglob("*.svg")}
        for _, names, _ in ICONS:
            self.assertIn(f"{names[0]}-symbolic.svg", written)

    def test_omarchy_palette(self):
        with tempfile.NamedTemporaryFile("w", suffix=".toml", delete=False) as f:
            f.write('accent = "#89b4fa"\nbackground = "#1e1e2e"\nforeground = "#cdd6f4"\nblue = "#89b4fa"\n'
                    'magenta = "#f5c2e7"\nbright_magenta = "#f5c2e7"\n')
        p = palette.from_omarchy(f.name)
        self.assertFalse(p["light"])
        self.assertEqual(p["accent"], "#89b4fa")
        self.assertNotEqual(p["swatches"]["violet"], p["swatches"]["pink"])


if __name__ == "__main__":
    unittest.main()
