"""The command an icon family installs (umbra-icons, vellum-icons): build the themes in
the current colours, pick a look, keep them following the theme.

    install [--look LOOK]          build, use the look, follow theme changes, set folder icons
    refresh [--palette FILE]       rebuild in the current colours (the theme hook runs this)
    look [LOOK|off]                show or change the look in use; off: stop using these icons
    folders [--reset]              give home folders (Games, Dropbox…) their icons
    follow on|off                  rebuild when the Omarchy theme changes
    build --out DIR [--palette …]  write the themes somewhere else
    remove                         go back to the icon theme used before
    status
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from . import build, catalog, palette as pal

HOME = Path.home()
DATA = Path(os.environ.get("XDG_DATA_HOME", HOME / ".local/share"))
CONFIG = Path(os.environ.get("XDG_CONFIG_HOME", HOME / ".config"))
ICONS = DATA / "icons"
GSCHEMA = "org.gnome.desktop.interface"
# Icon themes that draw the folder icons `folders` sets (folder-games, folder-dropbox…).
FOLDER_THEMES = ("Umbra", "Vellum")


@dataclass(frozen=True)
class IconSet:
    prog: str  # the command: umbra-icons
    name: str  # Umbra
    family: build.Family
    config: str  # its folder in ~/.config: umbra
    hook: str  # its Omarchy theme-set hook: 50-umbra-icons
    default_look: str

    @property
    def settings_file(self):
        return CONFIG / self.config / "settings.json"

    @property
    def hook_file(self):
        return CONFIG / "omarchy/hooks/theme-set.d" / self.hook

    @property
    def hook_mark(self):
        return f"# Installed by {self.prog} follow on"

    def owns(self, theme):
        return any(theme == d for d, _ in self.family.themes.values())


UMBRA = IconSet("umbra-icons", "Umbra", build.UMBRA, "umbra", "50-umbra-icons", "tile")


def settings(s):
    try:
        return json.loads(s.settings_file.read_text())
    except (OSError, ValueError):
        return {}


def save_settings(s, data):
    s.settings_file.parent.mkdir(parents=True, exist_ok=True)
    s.settings_file.write_text(json.dumps(data, indent=2) + "\n")


def current_icon_theme():
    if not shutil.which("gsettings"):
        return None
    r = subprocess.run(["gsettings", "get", GSCHEMA, "icon-theme"], capture_output=True, text=True)
    return r.stdout.strip().strip("'") or None if r.returncode == 0 else None


def set_icon_theme(name):
    """Use `name` everywhere apps read the icon theme: GNOME settings (GTK 4, Omarchy)
    and GTK 3's settings.ini."""
    if shutil.which("gsettings"):
        subprocess.run(["gsettings", "set", GSCHEMA, "icon-theme", name], check=False)
    for version in ("gtk-3.0", "gtk-4.0"):
        ini = CONFIG / version / "settings.ini"
        if not ini.is_file():
            continue
        lines = ini.read_text().splitlines()
        out, found = [], False
        for line in lines:
            if line.strip().startswith("gtk-icon-theme-name"):
                out.append(f"gtk-icon-theme-name={name}")
                found = True
            else:
                out.append(line)
        if not found:
            out.append(f"gtk-icon-theme-name={name}")
        ini.write_text("\n".join(out) + "\n")


def resolve_palette(s, arg):
    if arg in ("nyx-dark", "nyx-light"):
        return pal.resolve(source=arg)
    if arg:
        return pal.resolve(path=arg)
    saved = settings(s).get("palette_file")
    if saved and Path(saved).is_file():
        return pal.resolve(path=saved)
    return pal.resolve()


def do_build(s, palette, out=ICONS, quiet=False):
    counts = build.build(palette, out, family=s.family)
    if not quiet:
        names = ", ".join(f"{s.family.themes[k][1]} ({v})" for k, v in counts.items())
        print(f"Built {names} in {palette['name']} colours → {out}")


def use_look(s, look):
    data = settings(s)
    current = current_icon_theme()
    if current and not s.owns(current) and "previous" not in data:
        data["previous"] = current
    data["look"] = look
    save_settings(s, data)
    set_icon_theme(s.family.theme_dir(look))


def follow(s, on, exe):
    if on:
        s.hook_file.parent.mkdir(parents=True, exist_ok=True)
        s.hook_file.write_text(f"#!/bin/sh\n{s.hook_mark}\n\"{exe}\" refresh --quiet >/dev/null 2>&1 &\n")
        s.hook_file.chmod(0o755)
    elif s.hook_file.is_file() and s.hook_mark in s.hook_file.read_text():
        s.hook_file.unlink()
    data = settings(s)
    data["follow"] = on
    save_settings(s, data)


# ---------- Home folders ----------

def xdg_dirs():
    """XDG user folders: their path → role icon."""
    roles = {"DESKTOP": "user-desktop", "DOCUMENTS": "folder-documents", "DOWNLOAD": "folder-download",
             "MUSIC": "folder-music", "PICTURES": "folder-pictures", "VIDEOS": "folder-videos",
             "TEMPLATES": "folder-templates", "PUBLICSHARE": "folder-publicshare"}
    out = {}
    f = CONFIG / "user-dirs.dirs"
    if f.is_file():
        for line in f.read_text().splitlines():
            if line.startswith("XDG_") and "=" in line:
                key, val = line.split("=", 1)
                role = key[4:-4]
                path = Path(os.path.expandvars(val.strip().strip('"')))
                if role in roles and path != HOME:
                    out[path] = roles[role]
    return out


def folder_icons():
    """Folders in the home folder the catalog has an icon for: path → icon name."""
    found = {}
    xdg = xdg_dirs()
    for child in sorted(HOME.iterdir()):
        if not child.is_dir() or child.name.startswith("."):
            continue
        icon = xdg.get(child) or catalog.FOLDER_NAMES.get(child.name.lower())
        if icon and icon not in ("folder",):
            found[child] = icon
    return found


def folders(s, reset=False, quiet=False):
    if not shutil.which("gio"):
        sys.exit(f"{s.prog}: gio is needed to set folder icons")
    xdg = xdg_dirs()
    for path, icon in folder_icons().items():
        if path in xdg:
            continue  # file managers already know the XDG folders
        if reset:
            subprocess.run(["gio", "set", "-t", "unset", str(path), "metadata::custom-icon-name"], check=False)
            if not quiet:
                print(f"{path.name}: reset")
        else:
            subprocess.run(["gio", "set", str(path), "metadata::custom-icon-name", icon], check=False)
            if not quiet:
                print(f"{path.name}: {icon}")


# ---------- Commands ----------

def main(s, argv=None):
    looks = list(s.family.themes)
    exe = Path(sys.argv[0]).resolve()
    usage = __doc__.split("\n\n", 1)[1] + f"\nLOOK is {', '.join(looks[:-1])} or {looks[-1]}."
    ap = argparse.ArgumentParser(prog=s.prog, description=f"{s.name} icons: build the themes in the current colours, "
                                 f"pick a look, keep them following the theme.\n\n{usage}",
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("install")
    p.add_argument("--look", choices=looks, default=None)
    p.add_argument("--palette")
    p.add_argument("--no-follow", action="store_true")
    p = sub.add_parser("refresh")
    p.add_argument("--palette")
    p.add_argument("--quiet", action="store_true")
    p = sub.add_parser("look")
    p.add_argument("look", nargs="?", choices=[*looks, "off"])
    p = sub.add_parser("folders")
    p.add_argument("--reset", action="store_true")
    p = sub.add_parser("follow")
    p.add_argument("state", choices=["on", "off"])
    p = sub.add_parser("build")
    p.add_argument("--out", required=True)
    p.add_argument("--palette")
    sub.add_parser("remove")
    sub.add_parser("status")
    a = ap.parse_args(argv)

    if a.cmd == "install":
        look = a.look or settings(s).get("look", s.default_look)
        if a.palette:
            data = settings(s)
            data["palette_file"] = str(Path(a.palette).resolve())
            save_settings(s, data)
        do_build(s, resolve_palette(s, a.palette))
        use_look(s, look)
        if not a.no_follow:
            follow(s, True, exe)
        if shutil.which("gio"):
            folders(s, quiet=True)
        print(f"Using {s.family.themes[look][1]}.")
    elif a.cmd == "refresh":
        if a.palette:
            data = settings(s)
            data["palette_file"] = str(Path(a.palette).resolve())
            save_settings(s, data)
        do_build(s, resolve_palette(s, a.palette), quiet=a.quiet)
        look = settings(s).get("look")
        # Omarchy's theme switch sets its own icon theme; put the chosen look back.
        if look in s.family.themes and current_icon_theme() != s.family.theme_dir(look):
            set_icon_theme(s.family.theme_dir(look))
    elif a.cmd == "look":
        if not a.look:
            print(settings(s).get("look", "off"))
        elif a.look == "off":
            # Another icon theme was chosen (Nyx Settings does this): keep the themes and
            # their colours up to date, but stop putting this family back after theme changes.
            data = settings(s)
            data.pop("look", None)
            save_settings(s, data)
        else:
            if not (ICONS / s.family.theme_dir(a.look)).is_dir():
                do_build(s, resolve_palette(s, None))
            use_look(s, a.look)
            print(f"Using {s.family.themes[a.look][1]}.")
    elif a.cmd == "folders":
        folders(s, a.reset)
    elif a.cmd == "follow":
        follow(s, a.state == "on", exe)
    elif a.cmd == "build":
        do_build(s, resolve_palette(s, a.palette), Path(a.out))
    elif a.cmd == "remove":
        data = settings(s)
        back = data.get("previous") or "Adwaita"
        set_icon_theme(back)
        follow(s, False, exe)
        if shutil.which("gio") and not back.startswith(FOLDER_THEMES):
            folders(s, reset=True, quiet=True)
        for look in s.family.themes:
            shutil.rmtree(ICONS / s.family.theme_dir(look), ignore_errors=True)
        data.pop("look", None)
        save_settings(s, data)
        print(f"Back to {back}.")
    elif a.cmd == "status":
        data = settings(s)
        print(f"look: {data.get('look', 'not in use')}")
        print(f"icon theme: {current_icon_theme()}")
        print(f"following theme changes: {'yes' if s.hook_file.is_file() else 'no'}")
        for look in s.family.themes:
            info = ICONS / s.family.theme_dir(look) / f"{s.family.id}.json"
            if info.is_file():
                print(f"{s.family.themes[look][1]}: built in {json.loads(info.read_text())['palette']['name']} colours")
    return 0
