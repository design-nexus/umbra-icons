# Umbra icons

Python 3.11+, standard library only at runtime. `bin/umbra-icons` builds the themes
(`umbra/build.py`) from the glyphs (`umbra/glyphs.py`), names (`umbra/catalog.py`) and
looks (`umbra/looks.py`) in a palette (`umbra/palette.py`).

Commands: `python3 -m unittest discover -s tests`; `tools/sheet.py OUT.html --png` for a
contact sheet (headless Chromium, nothing on screen); `./install.sh` installs and switches
the user's icon theme.

- Glyphs: 24 px grid, 1.6 px round strokes. Brand and language marks keep their own
  colours; everything else takes the palette's swatches.
- `symbolic/` is generated: edit `umbra/symbolic_src.py`, then run
  `uv run --with skia-pathops==0.9.2 tools/outline.py` and commit the result.
- Never add an alias that is a real app's icon name (`dropbox`, `org.gnome.Terminal`):
  the theme would replace that app's own icon.
- Style rules: the canonical STYLE.md in design-nexus/nyx-design (section 9, Icons).
