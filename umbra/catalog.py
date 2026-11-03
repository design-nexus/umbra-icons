"""Every full-colour icon Umbra draws: its freedesktop names, what it shows and its colour.

Colours name the theme's swatches (blue, violet, pink, red, coral, amber, green, teal,
graphite) or `accent`; brands and languages bring their own.
"""

# ---------- Folders (places) ----------
# (names, mark, colour). A mark is a glyph, `brand:<id>`, or None for a plain folder.

FOLDERS = [
    (["folder", "inode-directory", "folder-drag-accept"], None, "accent"),
    (["folder-open", "folder-visiting"], "open", "accent"),
    (["user-home", "folder-home", "go-home"], "home", "accent"),
    (["user-desktop", "folder-desktop"], "desktop", "accent"),
    (["folder-documents"], "documents", "blue"),
    (["folder-download", "folder-downloads"], "downloads", "teal"),
    (["folder-pictures", "folder-images", "folder-photos"], "pictures", "green"),
    (["folder-videos", "folder-video", "folder-movies"], "videos", "violet"),
    (["folder-music", "folder-audio"], "music", "pink"),
    (["folder-games"], "games", "coral"),
    (["folder-projects", "folder-development", "folder-code"], "projects", "amber"),
    (["folder-wallpapers", "folder-wallpaper"], "wallpapers", "teal"),
    (["folder-work"], "work", "graphite"),
    (["folder-private", "folder-porn"], "private", "red"),
    (["folder-templates"], "templates", "graphite"),
    (["folder-publicshare", "folder-public"], "public", "graphite"),
    (["folder-remote", "folder-network"], "remote", "blue"),
    (["folder-recent", "document-open-recent"], "recent", "graphite"),
    (["folder-saved-search"], "search", "graphite"),
    (["user-bookmarks", "folder-bookmarks"], "bookmark", "amber"),
    (["folder-screenshots"], "screenshots", "teal"),
    (["folder-books", "folder-ebooks"], "books", "coral"),
    (["folder-backup", "folder-backups"], "backups", "graphite"),
    (["folder-git", "folder-repositories"], "git", "coral"),
    (["folder-applications", "folder-apps"], "apps", "violet"),
    (["folder-dropbox"], "brand:dropbox", None),
    (["folder-google-drive", "folder-gdrive"], "brand:google-drive", None),
    (["folder-onedrive"], "brand:onedrive", None),
    (["folder-nextcloud"], "brand:nextcloud", None),
    (["folder-mega"], "brand:mega", None),
    (["folder-proton-drive", "folder-proton"], "brand:proton-drive", None),
    (["folder-icloud"], "brand:icloud", None),
    (["folder-box"], "brand:box", None),
    (["folder-pcloud"], "brand:pcloud", None),
    (["folder-syncthing"], "brand:syncthing", None),
    (["folder-github"], "brand:github", None),
]

# Home folders by name (case-insensitive) → icon. The XDG user folders are found by
# their XDG role first; these catch the rest and common translations stay with XDG.
FOLDER_NAMES = {
    "desktop": "user-desktop",
    "documents": "folder-documents",
    "downloads": "folder-download",
    "pictures": "folder-pictures",
    "photos": "folder-pictures",
    "videos": "folder-videos",
    "movies": "folder-videos",
    "music": "folder-music",
    "templates": "folder-templates",
    "public": "folder-publicshare",
    "games": "folder-games",
    "projects": "folder-projects",
    "code": "folder-projects",
    "dev": "folder-projects",
    "src": "folder-projects",
    "wallpapers": "folder-wallpapers",
    "wallpaper": "folder-wallpapers",
    "backgrounds": "folder-wallpapers",
    "work": "folder-work",
    "porn": "folder-private",
    "private": "folder-private",
    "nsfw": "folder-private",
    "screenshots": "folder-screenshots",
    "books": "folder-books",
    "ebooks": "folder-books",
    "backups": "folder-backup",
    "backup": "folder-backup",
    "repos": "folder-git",
    "git": "folder-git",
    "applications": "folder-applications",
    "apps": "folder-applications",
    "dropbox": "folder-dropbox",
    "google drive": "folder-google-drive",
    "googledrive": "folder-google-drive",
    "gdrive": "folder-google-drive",
    "my drive": "folder-google-drive",
    "onedrive": "folder-onedrive",
    "nextcloud": "folder-nextcloud",
    "mega": "folder-mega",
    "megasync": "folder-mega",
    "proton drive": "folder-proton-drive",
    "protondrive": "folder-proton-drive",
    "icloud drive": "folder-icloud",
    "icloud": "folder-icloud",
    "box": "folder-box",
    "pcloud drive": "folder-pcloud",
    "pcloud": "folder-pcloud",
    "sync": "folder-syncthing",
    "syncthing": "folder-syncthing",
    "github": "folder-github",
}


def _mimes(*names):
    return [n.replace("/", "-") for n in names]


# ---------- Files (mimetypes) ----------
# (names, mark, colour, label). A mark is a glyph or `lang:<id>`; the label is the
# extension shown on the Solid look's badge.

FILES = [
    (["text-x-generic", "text-plain", "text-x-readme", "text-x-authors", "text-x-copying", "text-x-credits",
      "text-x-install", "text-x-changelog", "text-x-todo-txt", "text-rtf", "text-x-nfo"], "text", "graphite", "TXT"),
    (["application-pdf", "application-x-pdf"], "doc", "red", "PDF"),
    (["x-office-document", "application-msword", "application-rtf", "application-vnd.oasis.opendocument.text",
      "application-vnd.openxmlformats-officedocument.wordprocessingml.document", "application-x-abiword",
      "application-vnd.oasis.opendocument.text-template", "application-vnd.ms-word"], "doc", "blue", "DOC"),
    (["x-office-spreadsheet", "application-vnd.ms-excel", "application-vnd.oasis.opendocument.spreadsheet",
      "application-vnd.openxmlformats-officedocument.spreadsheetml.sheet", "text-csv", "text-tab-separated-values",
      "application-x-gnumeric"], "sheet", "green", "XLS"),
    (["x-office-presentation", "application-vnd.ms-powerpoint", "application-vnd.oasis.opendocument.presentation",
      "application-vnd.openxmlformats-officedocument.presentationml.presentation"], "slides", "coral", "PPT"),
    (["x-office-drawing", "application-vnd.oasis.opendocument.graphics", "image-x-xcf", "image-vnd.adobe.photoshop",
      "image-x-krita", "application-x-krita"], "drawing", "pink", "ART"),
    (["image-x-generic", "image-png", "image-jpeg", "image-gif", "image-webp", "image-bmp", "image-tiff", "image-avif",
      "image-heif", "image-jxl", "image-x-icon", "image-vnd.microsoft.icon", "image-x-portable-pixmap"], "image", "green", "IMG"),
    (["image-svg+xml", "image-svg+xml-compressed"], "drawing", "amber", "SVG"),
    (["video-x-generic", "video-mp4", "video-x-matroska", "video-webm", "video-quicktime", "video-x-msvideo",
      "video-mpeg", "video-ogg", "video-x-flv"], "video", "violet", "VID"),
    (["audio-x-generic", "audio-mpeg", "audio-flac", "audio-x-flac", "audio-ogg", "audio-x-vorbis+ogg", "audio-x-wav",
      "audio-wav", "audio-mp4", "audio-x-m4a", "audio-aac", "audio-opus", "audio-x-opus+ogg", "audio-x-mpegurl",
      "audio-x-scpls"], "audio", "pink", "AUD"),
    (["package-x-generic", "application-zip", "application-x-zip", "application-x-tar", "application-x-compressed-tar",
      "application-x-bzip-compressed-tar", "application-x-xz-compressed-tar", "application-x-zstd-compressed-tar",
      "application-gzip", "application-x-gzip", "application-x-bzip", "application-x-xz", "application-zstd",
      "application-x-7z-compressed", "application-x-rar", "application-vnd.rar", "application-x-archive",
      "application-x-cpio", "application-x-lzma"], "archive", "amber", "ZIP"),
    (["application-x-deb", "application-vnd.debian.binary-package", "application-x-rpm", "application-x-redhat-package-manager",
      "application-vnd.flatpak", "application-vnd.flatpak.ref", "application-x-appimage", "application-vnd.appimage",
      "application-x-arch-pkg", "application-vnd.snap", "application-x-addon"], "package", "violet", "PKG"),
    (["application-x-executable", "application-x-sharedlib", "application-x-object", "application-x-ms-dos-executable",
      "application-x-msdownload", "application-x-msi", "application-vnd.microsoft.portable-executable"], "exec", "graphite", "EXE"),
    (["text-x-script", "application-x-desktop", "text-x-systemd-unit", "application-x-trash"], "exec", "teal", "RUN"),
    (["application-x-cd-image", "application-x-iso9660-image", "application-x-raw-disk-image", "application-x-qemu-disk"],
     "disc", "graphite", "ISO"),
    (["font-x-generic", "font-ttf", "font-otf", "font-woff", "font-woff2", "application-x-font-ttf",
      "application-vnd.ms-opentype", "application-x-font-otf"], "font", "violet", "FONT"),
    (["text-calendar", "x-office-calendar", "text-x-vcalendar"], "calendar", "red", "ICS"),
    (["text-vcard", "text-x-vcard", "x-office-address-book", "text-directory"], "contact", "teal", "VCF"),
    (["application-x-sqlite3", "application-vnd.sqlite3", "application-x-sqlite2"], "database", "blue", "DB"),
    (["application-x-bittorrent"], "torrent", "green", "TOR"),
    (["application-epub+zip", "application-x-mobipocket-ebook", "application-x-fictionbook+xml", "application-vnd.amazon.ebook"],
     "ebook", "coral", "EPUB"),
    (["model-gltf+json", "model-gltf-binary", "model-stl", "model-obj", "application-x-blender", "model-x-generic"],
     "model", "amber", "3D"),
    (["application-x-x509-ca-cert", "application-pkix-cert", "application-x-pem-file", "application-pgp-keys",
      "application-pgp-signature", "text-x-ssh-public-key", "text-x-ssh-private-key", "application-x-pkcs12"],
     "key", "amber", "KEY"),
    (["text-x-log"], "log", "graphite", "LOG"),
    (["application-xhtml+xml", "text-x-uri", "application-x-mswinurl"], "web", "blue", "URL"),
    (["application-x-firmware", "application-octet-stream"], "chip", "graphite", "BIN"),
    (["application-x-ipynb+json"], "code", "coral", "IPYNB"),
]

# Languages: their mark on the file. (lang, mimetype names)
LANGUAGES = [
    ("rust", _mimes("text/rust", "text/x-rust")),
    ("python", _mimes("text/x-python", "text/x-python2", "text/x-python3", "application/x-python-code", "text/x-cython")),
    ("javascript", _mimes("text/javascript", "application/javascript", "application/x-javascript", "text/jsx")),
    ("typescript", _mimes("application/typescript", "text/x-typescript", "application/x-typescript", "text/tsx")),
    ("go", _mimes("text/x-go")),
    ("c", _mimes("text/x-csrc", "text/x-chdr", "text/x-c")),
    ("cpp", _mimes("text/x-c++src", "text/x-c++hdr", "text/x-c++")),
    ("csharp", _mimes("text/x-csharp")),
    ("java", _mimes("text/x-java", "application/x-java", "text/x-java-source", "application/java-archive",
                    "application/x-java-archive")),
    ("kotlin", _mimes("text/x-kotlin", "text/x-gradle-kts")),
    ("swift", _mimes("text/x-swift")),
    ("ruby", _mimes("application/x-ruby", "text/x-ruby")),
    ("php", _mimes("application/x-php", "text/x-php")),
    ("lua", _mimes("text/x-lua")),
    ("shell", _mimes("application/x-shellscript", "text/x-shellscript", "text/x-sh", "text/x-csh", "application/x-csh",
                     "text/x-zsh", "application/x-fish")),
    ("html", _mimes("text/html")),
    ("css", _mimes("text/css")),
    ("scss", _mimes("text/x-scss", "text/x-sass")),
    ("json", _mimes("application/json", "application/json5", "application/ld+json", "application/schema+json")),
    ("yaml", _mimes("application/x-yaml", "application/yaml", "text/x-yaml", "text/yaml")),
    ("toml", _mimes("application/toml", "text/x-toml")),
    ("xml", _mimes("application/xml", "text/xml", "application/xslt+xml", "text/x-xslfo")),
    ("markdown", _mimes("text/markdown", "text/x-markdown", "text/x-rst", "text/org")),
    ("sql", _mimes("application/sql", "text/x-sql")),
    ("dart", _mimes("application/vnd.dart", "text/x-dart")),
    ("zig", _mimes("text/x-zig", "text/zig")),
    ("haskell", _mimes("text/x-haskell", "text/x-literate-haskell")),
    ("elixir", _mimes("text/x-elixir")),
    ("erlang", _mimes("text/x-erlang")),
    ("nix", _mimes("text/x-nix")),
    ("makefile", _mimes("text/x-makefile", "text/x-meson")),
    ("cmake", _mimes("text/x-cmake", "application/x-cmakecache")),
    ("perl", _mimes("application/x-perl", "text/x-perl")),
    ("r", _mimes("text/x-r", "text/x-rsrc")),
    ("julia", _mimes("text/julia", "text/x-julia")),
    ("scala", _mimes("text/x-scala")),
    ("vue", _mimes("text/x-vue")),
    ("ocaml", _mimes("text/x-ocaml")),
    ("clojure", _mimes("text/x-clojure")),
    ("fortran", _mimes("text/x-fortran")),
    ("assembly", _mimes("text/x-asm")),
    ("vala", _mimes("text/x-vala", "text/x-genie")),
    ("docker", _mimes("text/x-dockerfile")),
    ("diff", _mimes("text/x-patch", "text/x-diff", "text/x-reject")),
    ("d", _mimes("text/x-dsrc")),
    ("objc", _mimes("text/x-objcsrc", "text/x-objc++src")),
    ("groovy", _mimes("text/x-groovy", "text/x-gradle")),
    ("powershell", _mimes("application/x-powershell")),
    ("tex", _mimes("text/x-tex", "text/x-bibtex")),
    ("gdscript", _mimes("application/x-gdscript")),
]

# ---------- Devices, status and app categories: one glyph on the look's base ----------
# (names, glyph, colour)

DEVICES = [
    (["drive-harddisk", "drive-harddisk-system", "drive-multidisk"], "drive", "graphite"),
    (["drive-harddisk-solidstate", "drive-harddisk-ssd"], "ssd", "graphite"),
    (["drive-removable-media", "drive-removable-media-usb", "drive-harddisk-usb", "media-removable"], "usb", "teal"),
    (["media-flash", "media-flash-sd-mmc", "media-flash-memory-stick"], "sdcard", "teal"),
    (["drive-optical", "media-optical", "media-optical-cd", "media-optical-dvd", "media-optical-bd"], "optical", "violet"),
    (["media-floppy"], "floppy", "graphite"),
    (["computer", "computer-desktop"], "computer", "blue"),
    (["computer-laptop"], "laptop", "blue"),
    (["tablet", "computer-tablet"], "tablet", "blue"),
    (["phone", "phone-android", "phone-apple-iphone"], "phone", "blue"),
    (["watch"], "watch", "blue"),
    (["camera-photo"], "camera", "pink"),
    (["camera-web", "camera-video"], "webcam", "pink"),
    (["printer", "printer-network"], "printer", "graphite"),
    (["scanner"], "scanner", "graphite"),
    (["input-keyboard"], "keyboard", "graphite"),
    (["input-mouse", "input-touchpad"], "mouse", "graphite"),
    (["input-gaming", "input-gamepad"], "gamepad", "coral"),
    (["input-tablet"], "pen-tablet", "violet"),
    (["audio-headphones"], "headphones", "pink"),
    (["audio-headset"], "headset", "pink"),
    (["audio-speakers", "audio-speaker"], "speaker", "pink"),
    (["audio-input-microphone"], "microphone", "pink"),
    (["audio-card"], "audio-card", "pink"),
    (["video-display"], "display", "blue"),
    (["network-wired", "network-card"], "ethernet", "green"),
    (["network-wireless"], "wifi", "green"),
    (["bluetooth"], "bluetooth", "blue"),
    (["battery", "ac-adapter"], "battery", "green"),
    (["multimedia-player"], "media-player", "violet"),
    (["network-workgroup"], "network", "teal"),
    (["network-server"], "server", "teal"),
    (["modem", "network-wireless-router"], "router", "teal"),
    (["cpu"], "cpu", "amber"),
    (["media-memory"], "memory", "amber"),
]

STATUS = [
    (["dialog-information", "help-info"], "info", "blue"),
    (["dialog-warning"], "warning", "amber"),
    (["dialog-error"], "error", "red"),
    (["dialog-question", "help-faq"], "question", "blue"),
    (["dialog-password", "changes-prevent", "system-lock-screen"], "lock", "amber"),
    (["security-high"], "shield", "green"),
    (["security-medium"], "shield-warn", "amber"),
    (["security-low"], "shield-off", "red"),
    (["avatar-default", "system-users", "user-info"], "avatar", "accent"),
    (["image-missing", "gtk-missing-image"], "missing", "red"),
    (["user-trash", "trash-empty"], "trash", "graphite"),
    (["user-trash-full", "trash-full"], "trash-full", "accent"),
    (["starred", "emblem-favorite"], "star", "amber"),
]

# Generic app and category icons, for apps without their own and menu categories.
APPS = [
    (["application-default-icon", "applications-other", "gnome-panel-launcher"], "app", "graphite"),
    (["utilities-terminal"], "terminal", "graphite"),
    (["system-file-manager"], "folder", "accent"),
    (["web-browser", "applications-internet"], "web", "blue"),
    (["accessories-text-editor"], "edit", "teal"),
    (["accessories-calculator"], "calculator", "amber"),
    (["preferences-system", "preferences-desktop", "applications-system", "system-settings"], "gear", "graphite"),
    (["preferences-other", "preferences-desktop-personal"], "sliders", "graphite"),
    (["system-software-install", "system-software-update"], "store", "violet"),
    (["help-browser", "help-contents"], "help", "blue"),
    (["applications-accessories", "applications-utilities", "utilities-system-monitor"], "accessories", "teal"),
    (["applications-development", "applications-engineering"], "code", "amber"),
    (["applications-games"], "games", "coral"),
    (["applications-graphics", "applications-painting"], "graphics", "pink"),
    (["applications-multimedia", "multimedia-video-player"], "film", "violet"),
    (["applications-office"], "doc", "blue"),
    (["applications-science", "applications-education"], "flask", "green"),
    (["start-here", "distributor-logo"], "apps", "accent"),
]


def full_colour():
    """Every full-colour icon as (context, names, spec)."""
    out = []
    for names, mark, colour in FOLDERS:
        out.append(("places", names, {"kind": "folder", "mark": mark, "colour": colour}))
    for names, mark, colour, ext in FILES:
        out.append(("mimetypes", names, {"kind": "file", "mark": mark, "colour": colour, "label": ext}))
    for lang, names in LANGUAGES:
        out.append(("mimetypes", names, {"kind": "file", "mark": f"lang:{lang}", "colour": None, "label": None}))
    for names, glyph, colour in DEVICES:
        out.append(("devices", names, {"kind": "device", "mark": glyph, "colour": colour}))
    for names, glyph, colour in STATUS:
        context = "places" if glyph.startswith("trash") else "status"
        out.append((context, names, {"kind": "device", "mark": glyph, "colour": colour}))
    for names, glyph, colour in APPS:
        out.append(("apps", names, {"kind": "device", "mark": glyph, "colour": colour}))
    return out
