# Umbra

A complete icon theme for Linux desktops, drawn in the colours of your theme. Folders,
file types, devices and status icons come in three looks, with a matching set of
symbolic icons for toolbars and menus.

## Install

```sh
curl -fsSL https://raw.githubusercontent.com/design-nexus/umbra-icons/main/install.sh | bash
```

This builds the themes in your current Omarchy theme's colours, switches to Umbra, and
rebuilds them whenever you change the Omarchy theme. To start with another look:

```sh
curl -fsSL https://raw.githubusercontent.com/design-nexus/umbra-icons/main/install.sh | bash -s -- --look line
```

It also gives folders like Games, Projects and Dropbox their icons. `umbra-icons remove`
(or `uninstall.sh`) goes back to the icon theme you had before.

## Looks

| Theme | Look |
| --- | --- |
| **Umbra** (default) | A satin rounded tile with a coloured line glyph: a folder or page outline with its mark. |
| **Umbra Solid** | Solid satin folders with the mark on the front and an accent edge; files are satin pages with a folded corner and a coloured type badge. |
| **Umbra Line** | Coloured line glyphs only. Strokes thin out at large sizes. |

All three share the symbolic set: 24 px grid, 1.6 px round strokes, recoloured by apps
like any symbolic icon. Change the look with `umbra-icons look tile|solid|line`, or pick
Umbra, Umbra Solid or Umbra Line in any app that sets the icon theme.

## What's drawn

- **Folders:** Home, Desktop, Documents, Downloads, Pictures, Videos, Music, Templates,
  Public, plus Games, Projects, Wallpapers, Work, Private, Screenshots, Books, Backups,
  Git and Applications, and cloud drives: Dropbox, Google Drive, OneDrive, Nextcloud,
  MEGA, Proton Drive, iCloud, Box, pCloud, Syncthing and GitHub, in their own colours.
- **File types:** documents, PDFs, spreadsheets, presentations, images, video, audio,
  archives, packages, executables, disk images, fonts, calendars, contacts, databases,
  torrents, e-books, 3D models, keys and logs.
- **Code:** the language's mark is on the file, so you can tell a Rust file from a
  Python one without its extension. About 50 languages and formats, including Rust,
  Python, JavaScript, TypeScript, Go, C, C++, C#, Java, Kotlin, Swift, Ruby, PHP, Lua,
  shell, HTML, CSS, JSON, YAML, TOML, Markdown, SQL, Dart, Zig, Haskell, Elixir, Nix,
  Docker, CMake and more.
- **Devices, dialogs and app categories**, and about 460 symbolic icons: actions, media,
  formatting, network, battery, volume, weather, places and devices.

Anything Umbra doesn't draw comes from Adwaita, then hicolor. Apps keep their own icons.

## Folder icons

Folders that aren't standard XDG folders (Games, Projects, Wallpapers, Work, Dropbox…)
get their icons from file-manager metadata:

```sh
umbra-icons folders           # set the icons of matching folders in your home folder
umbra-icons folders --reset   # take them off again
```

## Commands

```
umbra-icons install [--look tile|solid|line]   build, use the look, follow theme changes, set folder icons
umbra-icons refresh [--palette FILE]           rebuild in the current colours
umbra-icons look [tile|solid|line|off]         show or change the look; off stops using Umbra
umbra-icons folders [--reset]                  icons for Games, Dropbox and other folders
umbra-icons follow on|off                      rebuild when the Omarchy theme changes
umbra-icons build --out DIR                    write the themes somewhere else
umbra-icons status
umbra-icons remove                             back to the previous icon theme
```

Colours come from a palette file when given (`{"bg", "text", "accent", "light",
"swatches": {"blue", "violet", "pink", "red", "coral", "amber", "green", "teal",
"graphite"}}`), else from Omarchy's current `colors.toml`, else a dark default.

## Developing

`python3 -m unittest discover -s tests` checks every icon in every look. The drawings
are in `umbra/glyphs.py`, the icon names in `umbra/catalog.py` and the looks in
`umbra/looks.py`. `tools/sheet.py OUT.html --png` draws a contact sheet.

The symbolic set is committed as filled outlines, since GTK fills every shape in a
symbolic icon. After changing `umbra/symbolic_src.py`, regenerate it with:

```sh
uv run --with skia-pathops==0.9.2 tools/outline.py
```

## License

MIT
