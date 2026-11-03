"""Umbra's drawing library: line glyphs, a stroke alphabet, cloud-drive and language marks.

Glyphs live on a 24 px grid and are drawn with 1.6 px round-capped strokes. Marks for
third-party brands are geometric interpretations in the brand's own colours; they are
never recoloured to the theme.
"""

# ---------- Line glyphs (24 px grid) ----------

G = {
    # containers
    "folder": "M3 7.5a2.5 2.5 0 0 1 2.5-2.5H9l2 2.2h7.5A2.5 2.5 0 0 1 21 9.7v7.8a2.5 2.5 0 0 1-2.5 2.5h-13A2.5 2.5 0 0 1 3 17.5z",
    "folder-open": "M3 17.5V7.5A2.5 2.5 0 0 1 5.5 5H9l2 2.2h6A2.5 2.5 0 0 1 19.5 9.7V11 M3 17.5l2.4-5.3A2 2 0 0 1 7.2 11h13.1a1 1 0 0 1 .9 1.4l-2.6 6.1a2.5 2.5 0 0 1-2.3 1.5H5.5A2.5 2.5 0 0 1 3 17.5z",
    "page": "M7.5 3.5H14l4 4V19a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 6 19V5a1.5 1.5 0 0 1 1.5-1.5z M14 3.5V7.5h4",
    # places
    "home": "M4.5 10.5L12 4.5l7.5 6V19a1 1 0 0 1-1 1H14v-5h-4v5H5.5a1 1 0 0 1-1-1z",
    "desktop": "M4 5h16v11H4z M9 20h6 M12 16v4",
    "pictures": "M4.5 5.5h15v13h-15z M4.5 15.5l4.5-4.5 3.5 3.5 2-2 4.5 4.5 M15.5 9.6a1.2 1.2 0 1 0 0-.01",
    "videos": "M4.5 6h15v12h-15z M10.5 9.3v5.4l4.5-2.7z",
    "documents": "M8 8.5h8 M8 12h8 M8 15.5h5",
    "downloads": "M12 4.5v10 M7.5 10.5L12 15l4.5-4.5 M5.5 19.5h13",
    "music": "M9.5 17V6.5l9-2V15 M9.5 17a2 2 0 1 1-4 0 2 2 0 0 1 4 0z M18.5 15a2 2 0 1 1-4 0 2 2 0 0 1 4 0z",
    "games": "M8 8.5h8a4 4 0 0 1 4 4v2a2.5 2.5 0 0 1-4.5 1.5L14.5 15h-5l-1 1A2.5 2.5 0 0 1 4 14.5v-2a4 4 0 0 1 4-4z M8 10.8v3.4 M6.3 12.5h3.4 M15.5 11.5h.01 M17.5 13.5h.01",
    "private": "M4 4l16 16 M10.5 6.2A9 9 0 0 1 12 6c5 0 8.5 6 8.5 6a14 14 0 0 1-2.4 3 M7 7.2C4.8 8.7 3.5 12 3.5 12s3.5 6 8.5 6a8.5 8.5 0 0 0 4-1 M10 10a2.8 2.8 0 0 0 4 4",
    "projects": "M9 8l-4 4 4 4 M15 8l4 4-4 4 M13.2 6.5l-2.4 11",
    "wallpapers": "M4 5h16v11H4z M9 20h6 M12 16v4 M6.5 13.5l3.5-3.5 2.5 2.5 1.5-1.5 3.5 3",
    "work": "M4 8.5h16v10.5H4z M9 8.5V6.5A1.5 1.5 0 0 1 10.5 5h3A1.5 1.5 0 0 1 15 6.5v2 M4 13h16",
    "templates": "M5 4.5h14v15H5z M5 9h14 M10 9v10.5",
    "public": "M9 11a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z M4.5 18.5a4.5 4.5 0 0 1 9 0 M16 11a2 2 0 1 0 0-4 M15.5 13.6a4 4 0 0 1 4 4",
    "remote": "M12 4a8 8 0 1 0 0 16 8 8 0 0 0 0-16z M4 12h16 M12 4c2.2 2.2 3.2 5 3.2 8s-1 5.8-3.2 8 M12 4c-2.2 2.2-3.2 5-3.2 8s1 5.8 3.2 8",
    "recent": "M12 4a8 8 0 1 0 0 16 8 8 0 0 0 0-16z M12 8v4.5l3 2",
    "search": "M11 4.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13z M20 20l-4.4-4.4",
    "bookmark": "M7 4.5h10v15l-5-3.5-5 3.5z",
    "screenshots": "M4.5 8V6a1.5 1.5 0 0 1 1.5-1.5h2 M16 4.5h2A1.5 1.5 0 0 1 19.5 6v2 M19.5 16v2a1.5 1.5 0 0 1-1.5 1.5h-2 M8 19.5H6A1.5 1.5 0 0 1 4.5 18v-2 M12 9.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z",
    "books": "M5 5.5h3.5v13H5z M8.5 7h3.5v11.5H8.5z M13.2 7.4l3.3-.9 3 11.2-3.3.9z",
    "backups": "M4.5 12a7.5 7.5 0 1 0 2.2-5.3 M4.5 4.5v3.5H8 M12 8.5v3.8l2.6 1.6",
    "git": "M7 5.5a1.8 1.8 0 1 0 0 3.6 1.8 1.8 0 0 0 0-3.6z M7 14.9a1.8 1.8 0 1 0 0 3.6 1.8 1.8 0 0 0 0-3.6z M17 9a1.8 1.8 0 1 0 0 3.6A1.8 1.8 0 0 0 17 9z M7 9.1v5.8 M17 12.6c0 2-2 2.6-4.5 2.8L8.8 16",
    "apps": "M5 5h5v5H5z M14 5h5v5h-5z M5 14h5v5H5z M14 14h5v5h-5z",
    "trash": "M5 7h14 M10 7V5h4v2 M6.5 7l1 12.5h9l1-12.5 M10.5 11v5 M13.5 11v5",
    "trash-full": "M5 7h14 M10 7V5h4v2 M6.5 7l1 12.5h9l1-12.5 M9 12.5h6 M9.5 15.5h5",
    "network": "M9 4.5h6v4.5H9z M12 9v3.5 M5.5 12.5h13 M5.5 12.5V15 M18.5 12.5V15 M3 15h5v4.5H3z M16 15h5v4.5h-5z",
    "server": "M5 4.5h14v6H5z M5 13.5h14v6H5z M8 7.5h.01 M8 16.5h.01 M12 7.5h4 M12 16.5h4",
    "star": "M12 4.5l2.3 4.7 5.2.8-3.8 3.6.9 5.2-4.6-2.4-4.6 2.4.9-5.2-3.8-3.6 5.2-.8z",
    # file types
    "doc": "M8 9h8 M8 12.5h8 M8 16h5",
    "image": "M6.5 17l3.5-4 3 3 2-2 2.5 3 M14.8 9.2a1.3 1.3 0 1 0 0 .01",
    "video": "M10 8.5v7l6-3.5z",
    "audio": "M10.5 16V8.5l6-1.5v7 M10.5 16a1.7 1.7 0 1 1-3.4 0 1.7 1.7 0 0 1 3.4 0z M16.5 14a1.7 1.7 0 1 1-3.4 0 1.7 1.7 0 0 1 3.4 0z",
    "archive": "M12 5v1.6 M12 8.6v1.6 M12 12.2v1.6 M10.4 15h3.2v3.3h-3.2z",
    "code": "M9.5 9L6.5 12l3 3 M14.5 9l3 3-3 3",
    "sheet": "M6.5 7h11v10h-11z M6.5 12h11 M11 7v10",
    "slides": "M6 7h12v8H6z M12 15v3 M9.5 18h5",
    "drawing": "M6 18l2.5-.6 9-9a1.6 1.6 0 0 0-2.3-2.3l-9 9z M14 7.4l2.3 2.3",
    "text": "M8 9h8 M8 12.5h8 M8 16h8",
    "exec": "M7.5 9l3 3-3 3 M12.5 15h4",
    "font": "M7 17l5-11 5 11 M8.8 13h6.4",
    "disc": "M12 5a7 7 0 1 0 0 14 7 7 0 0 0 0-14z M12 10a2 2 0 1 0 0 4 2 2 0 0 0 0-4z",
    "package": "M12 4.5l7 3.5v8L12 19.5 5 16V8z M5 8l7 3.5L19 8 M12 11.5v8 M8.5 6.2l7 3.5",
    "calendar": "M5 6.5h14v12.5H5z M5 10.5h14 M9 4.5v4 M15 4.5v4",
    "contact": "M12 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6z M6.5 19a5.5 5.5 0 0 1 11 0",
    "database": "M12 4.5c3.6 0 6.5 1.1 6.5 2.5S15.6 9.5 12 9.5 5.5 8.4 5.5 7 8.4 4.5 12 4.5z M5.5 7v10c0 1.4 2.9 2.5 6.5 2.5s6.5-1.1 6.5-2.5V7 M5.5 12c0 1.4 2.9 2.5 6.5 2.5s6.5-1.1 6.5-2.5",
    "torrent": "M12 4.5v9 M8 9.5l4 4 4-4 M6.5 16a5.5 3 0 0 0 11 0",
    "ebook": "M5 5.5a1.5 1.5 0 0 1 1.5-1.5H19v14H6.5A1.5 1.5 0 0 0 5 19.5z M5 19.5A1.5 1.5 0 0 0 6.5 21H19 M9 8h6",
    "model": "M12 4.5l7 4v7l-7 4-7-4v-7z M5 8.5l7 4 7-4 M12 12.5v7",
    "certificate": "M12 4.5a4.5 4.5 0 1 0 0 9 4.5 4.5 0 0 0 0-9z M9.5 13l-1 6.5 3.5-2 3.5 2-1-6.5",
    "log": "M8 8.5h.01 M11 8.5h5 M8 12h.01 M11 12h5 M8 15.5h.01 M11 15.5h3",
    "diff": "M12 6.5v6 M9 9.5h6 M9 16.5h6",
    "key": "M8.5 15.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z M12 12h8 M17 12v3 M19.5 12v2",
    "web": "M12 4.5a7.5 7.5 0 1 0 0 15 7.5 7.5 0 0 0 0-15z M4.5 12h15 M12 4.5c2 2 3 4.7 3 7.5s-1 5.5-3 7.5 M12 4.5c-2 2-3 4.7-3 7.5s1 5.5 3 7.5",
    "chip": "M7 7h10v10H7z M10 10h4v4h-4z M10 4v3 M14 4v3 M10 17v3 M14 17v3 M4 10h3 M4 14h3 M17 10h3 M17 14h3",
    # devices
    "drive": "M4.5 8.5h15v9h-15z M4.5 12.5h15 M7.5 15h2 M16.5 15h.01",
    "ssd": "M5 5.5h14v13H5z M8 9h8 M8 12h8 M8 15h4",
    "usb": "M9 3.5h6v5H9z M7 8.5h10v8a3 3 0 0 1-3 3h-4a3 3 0 0 1-3-3z M10.5 12.5h3",
    "sdcard": "M8 4h8l3 3v13H5V7z M9 4v3 M12 4v3 M15 4v3",
    "optical": "M12 4.5a7.5 7.5 0 1 0 0 15 7.5 7.5 0 0 0 0-15z M12 10.3a1.7 1.7 0 1 0 0 3.4 1.7 1.7 0 0 0 0-3.4z M15.5 7.5a5 5 0 0 1 1.3 2",
    "floppy": "M5 4.5h11l3 3v12H5z M8 4.5v4h7v-4 M8 19.5v-5h8v5",
    "computer": "M4 5h16v11H4z M9 20h6 M12 16v4",
    "laptop": "M5.5 6h13v9h-13z M3 18.5h18",
    "tablet": "M6.5 3.5h11v17h-11z M11 17.5h2",
    "phone": "M8 3.5h8v17H8z M11 17.5h2",
    "watch": "M8 7h8v10H8z M9.5 7l.7-3h3.6l.7 3 M9.5 17l.7 3h3.6l.7-3",
    "camera": "M4.5 8.5h3l1.5-2h6l1.5 2h3v10h-15z M12 10.5a3 3 0 1 0 0 6 3 3 0 0 0 0-6z",
    "webcam": "M12 4.5a5.5 5.5 0 1 0 0 11 5.5 5.5 0 0 0 0-11z M12 8a2 2 0 1 0 0 4 2 2 0 0 0 0-4z M8.5 15l-1.5 4.5h10L15.5 15",
    "printer": "M7.5 9V4.5h9V9 M5 9h14v7h-2.5 M7.5 16H5V9 M7.5 13.5h9v6h-9z",
    "scanner": "M4.5 12.5h15v5h-15z M6 12.5l12-6 M7.5 15h.01",
    "keyboard": "M3.5 7h17v10h-17z M7 10h.01 M10 10h.01 M13 10h.01 M16 10h.01 M8 14h8",
    "mouse": "M12 3.5a5.5 5.5 0 0 0-5.5 5.5v6a5.5 5.5 0 0 0 11 0V9A5.5 5.5 0 0 0 12 3.5z M12 6.5v3",
    "gamepad": "M8 8.5h8a4 4 0 0 1 4 4v2a2.5 2.5 0 0 1-4.5 1.5L14.5 15h-5l-1 1A2.5 2.5 0 0 1 4 14.5v-2a4 4 0 0 1 4-4z M8 10.8v3.4 M6.3 12.5h3.4 M15.5 11.5h.01 M17.5 13.5h.01",
    "pen-tablet": "M4.5 6.5h15v11h-15z M10 14.5l5-5 M10 14.5l-.6 1.5 1.5-.6",
    "headphones": "M4.5 15v-3a7.5 7.5 0 0 1 15 0v3 M4.5 14h3v5.5h-3z M16.5 14h3v5.5h-3z",
    "headset": "M5 13v-1a7 7 0 0 1 14 0v1 M5 12.5h2.5v5H5z M16.5 12.5H19v5h-2.5z M19 17.5c0 1.5-1.5 2.5-4 2.5h-2",
    "speaker": "M7 3.5h10v17H7z M12 14a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z M12 7h.01",
    "microphone": "M12 4a2.5 2.5 0 0 0-2.5 2.5v5a2.5 2.5 0 0 0 5 0v-5A2.5 2.5 0 0 0 12 4z M6.5 11.5a5.5 5.5 0 0 0 11 0 M12 17v3",
    "audio-card": "M4 7h16v10H4z M7 17v2.5 M11 17v2.5 M15 9.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z M7 10h3",
    "display": "M3.5 5h17v11h-17z M9 20h6 M12 16v4",
    "ethernet": "M6 5.5h12v9H6z M9 14.5v3h6v-3 M9 8.5v3 M12 8.5v3 M15 8.5v3",
    "wifi": "M3.5 9.5a12 12 0 0 1 17 0 M6.5 12.5a8 8 0 0 1 11 0 M9.5 15.5a3.6 3.6 0 0 1 5 0 M12 18.5h.01",
    "bluetooth": "M7.5 8l9 8-4.5 4V4l4.5 4-9 8",
    "battery": "M4 8h14.5v8H4z M20.5 10.5v3 M6.5 10.5h6v3h-6z",
    "media-player": "M7 3.5h10v17H7z M12 12a3 3 0 1 0 0 6 3 3 0 0 0 0-6z M9.5 6.5h5",
    "router": "M4 13.5h16v5H4z M7 16h.01 M10 16h.01 M15 13.5l2-6 M9.5 9a4 4 0 0 1 5 0",
    "cpu": "M7 7h10v10H7z M10 10h4v4h-4z M10 4v3 M14 4v3 M10 17v3 M14 17v3 M4 10h3 M4 14h3 M17 10h3 M17 14h3",
    "memory": "M3.5 8h17v8h-17z M7 8v8 M11 8v8 M15 8v8 M5 16v2.5 M19 16v2.5",
    "terminal": "M4 5.5h16v13H4z M7.5 10l2.5 2-2.5 2 M12 14.5h4",
    # dialogs and status
    "info": "M12 4.5a7.5 7.5 0 1 0 0 15 7.5 7.5 0 0 0 0-15z M12 11v4.5 M12 8.2h.01",
    "warning": "M12 4.5l8.5 15h-17z M12 10v4 M12 16.8h.01",
    "error": "M12 4.5a7.5 7.5 0 1 0 0 15 7.5 7.5 0 0 0 0-15z M9.2 9.2l5.6 5.6 M14.8 9.2l-5.6 5.6",
    "question": "M12 4.5a7.5 7.5 0 1 0 0 15 7.5 7.5 0 0 0 0-15z M9.8 9.8a2.3 2.3 0 0 1 4.4.9c0 1.6-2.2 1.9-2.2 3.3 M12 16.6h.01",
    "lock": "M6.5 10.5h11v9h-11z M9 10.5V8a3 3 0 0 1 6 0v2.5 M12 14v2",
    "shield": "M12 4l6.5 2.5V12c0 3.8-2.8 6.6-6.5 8-3.7-1.4-6.5-4.2-6.5-8V6.5z M9.2 12l2 2 3.6-3.8",
    "shield-warn": "M12 4l6.5 2.5V12c0 3.8-2.8 6.6-6.5 8-3.7-1.4-6.5-4.2-6.5-8V6.5z M12 9v3.5 M12 15.2h.01",
    "shield-off": "M12 4l6.5 2.5V12c0 3.8-2.8 6.6-6.5 8-3.7-1.4-6.5-4.2-6.5-8V6.5z M9.5 9.5l5 5 M14.5 9.5l-5 5",
    "avatar": "M12 4.5a7.5 7.5 0 1 0 0 15 7.5 7.5 0 0 0 0-15z M12 8a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z M7.5 17.3a5 5 0 0 1 9 0",
    "missing": "M5 5h14v14H5z M5 5l14 14 M19 5L5 19",
    "app": "M5 5h14v14H5z M5 9h14 M7.5 7h.01 M10 7h.01",
    "gear": "M12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6z M12 3.5v2.3 M12 18.2v2.3 M3.5 12h2.3 M18.2 12h2.3 M6 6l1.6 1.6 M16.4 16.4L18 18 M6 18l1.6-1.6 M16.4 7.6L18 6",
    "sliders": "M4 7h10 M18 7h2 M4 17h4 M12 17h8 M14 5v4 M8 15v4",
    "store": "M5 8.5h14l-1 11H6z M9 8.5V7a3 3 0 0 1 6 0v1.5",
    "help": "M12 4.5a7.5 7.5 0 1 0 0 15 7.5 7.5 0 0 0 0-15z M9.8 9.8a2.3 2.3 0 0 1 4.4.9c0 1.6-2.2 1.9-2.2 3.3 M12 16.6h.01",
    "calculator": "M6.5 3.5h11v17h-11z M9 7h6v3H9z M9 13h.01 M12 13h.01 M15 13h.01 M9 16.5h.01 M12 16.5h.01 M15 16.5h.01",
    "edit": "M6 18l2.5-.6 9-9a1.6 1.6 0 0 0-2.3-2.3l-9 9z M14 7.4l2.3 2.3",
    "brush": "M14.5 4.5l5 5-6.5 6.5-5-5z M8 11l5 5 M8 11c-2.5 0-4 1.8-4 4 0 1.8-.5 3-1.5 4.5 3 0 7.5-.5 7.5-4",
    "flask": "M10 4.5h4 M10.5 4.5v5L5.5 18a1 1 0 0 0 .9 1.5h11.2a1 1 0 0 0 .9-1.5l-5-8.5v-5 M8 14.5h8",
    "accessories": "M14.5 6.5a3.5 3.5 0 0 0-4.6 4.6l-5.4 5.4a1.6 1.6 0 0 0 2.3 2.3l5.4-5.4a3.5 3.5 0 0 0 4.6-4.6l-2.1 2.1-2.3-2.3z",
    "film": "M5 4.5h14v15H5z M5 9h14 M5 15h14 M8.5 4.5V9 M15.5 4.5V9 M8.5 15v4.5 M15.5 15v4.5",
    "graphics": "M12 4.5a7.5 7.5 0 0 0 0 15c1 0 1.5-.7 1.5-1.5 0-1.2-1-1.4-1-2.5 0-.8.6-1.5 1.5-1.5h2A3.5 3.5 0 0 0 19.5 10.5C19.5 7 16 4.5 12 4.5z M8 11h.01 M10.5 8h.01 M14.5 8h.01",
}

# ---------- A stroke alphabet for labels (cap height 10) ----------

FONT = {
    "A": (6, "M0 10L3 0l3 10 M1 6.6h4"),
    "B": (6, "M0 10V0h3.3a2.4 2.4 0 0 1 0 4.8H0 M0 4.8h3.7a2.6 2.6 0 0 1 0 5.2H0"),
    "C": (6, "M5.8 1.8A3.6 5 0 1 0 5.8 8.2"),
    "D": (6, "M0 0v10h2.4c2.2 0 3.6-2.2 3.6-5S4.6 0 2.4 0z"),
    "E": (5.5, "M5.5 0H0v10h5.5 M0 5h4.2"),
    "F": (5.5, "M5.5 0H0v10 M0 5h4.2"),
    "G": (6, "M5.8 1.8A3.6 5 0 1 0 6 6.6V5.4H3.4"),
    "H": (6, "M0 0v10 M6 0v10 M0 5h6"),
    "I": (2, "M1 0v10"),
    "J": (5, "M5 0v7a2.5 3 0 0 1-5 0"),
    "K": (6, "M0 0v10 M6 0L0 6.2 M2.2 4L6 10"),
    "L": (5, "M0 0v10h5"),
    "M": (7, "M0 10V0l3.5 6.5L7 0v10"),
    "N": (6, "M0 10V0l6 10V0"),
    "O": (6.4, "M3.2 0C5 0 6.4 2.2 6.4 5s-1.4 5-3.2 5S0 7.8 0 5s1.4-5 3.2-5z"),
    "P": (6, "M0 10V0h3.4a2.6 2.6 0 0 1 0 5.2H0"),
    "Q": (6.4, "M3.2 0C5 0 6.4 2.2 6.4 5s-1.4 5-3.2 5S0 7.8 0 5s1.4-5 3.2-5z M4 7.4l2.4 2.8"),
    "R": (6, "M0 10V0h3.4a2.6 2.6 0 0 1 0 5.2H0 M3 5.2L6 10"),
    "S": (5.6, "M5.4 1.6C4.9.6 4 0 2.8 0 1.3 0 .3.9.3 2.4.3 5.6 5.6 4.4 5.6 7.6 5.6 9.1 4.4 10 2.8 10 1.4 10 .5 9.3 0 8.3"),
    "T": (6, "M0 0h6 M3 0v10"),
    "U": (6, "M0 0v6.6c0 2 1.3 3.4 3 3.4s3-1.4 3-3.4V0"),
    "V": (6, "M0 0l3 10 3-10"),
    "W": (8, "M0 0l1.8 10L4 2.5 6.2 10 8 0"),
    "X": (6, "M0 0l6 10 M6 0L0 10"),
    "Y": (6, "M0 0l3 5 3-5 M3 5v5"),
    "Z": (6, "M0 0h6L0 10h6"),
    "0": (5.6, "M2.8 0c1.6 0 2.8 2.2 2.8 5s-1.2 5-2.8 5S0 7.8 0 5 1.2 0 2.8 0z"),
    "1": (4, "M0.6 2L3 0v10"),
    "2": (5.6, "M.4 2.2C.8.9 1.7 0 3 0c1.5 0 2.6 1 2.6 2.6C5.6 5.4 0 7.2 0 10h5.6"),
    "3": (5.6, "M.4 1.4C.9.5 1.8 0 2.9 0c1.5 0 2.5 1 2.5 2.4S4.3 4.8 2.8 4.8c1.7 0 2.8 1 2.8 2.6S4.4 10 2.8 10C1.6 10 .6 9.4 0 8.4"),
    "4": (6, "M4.5 10V0L0 7.2h6"),
    "5": (5.6, "M5.3 0H1L.6 4.6C1.1 4.1 1.9 3.8 2.8 3.8c1.7 0 2.8 1.3 2.8 3.1S4.4 10 2.8 10C1.6 10 .6 9.4 0 8.4"),
    "6": (5.6, "M5 .8C4.5.3 3.8 0 3 0 1.2 0 0 2.4 0 6c0 2.4 1.1 4 2.8 4s2.8-1.4 2.8-3.1S4.5 3.8 2.8 3.8C1.6 3.8.6 4.6 0 6"),
    "7": (5.6, "M0 0h5.6L2 10"),
    "8": (5.6, "M2.8 0C4.2 0 5.2.9 5.2 2.3S4.2 4.8 2.8 4.8.4 3.7.4 2.3 1.4 0 2.8 0z M2.8 4.8c1.6 0 2.8 1 2.8 2.6S4.4 10 2.8 10 0 9 0 7.4s1.2-2.6 2.8-2.6z"),
    "9": (5.6, "M.6 9.2c.5.5 1.2.8 2 .8 1.8 0 3-2.4 3-6 0-2.4-1.1-4-2.8-4S0 1.4 0 3.1s1.1 3.1 2.8 3.1c1.2 0 2.2-.8 2.8-2.2"),
    "+": (5, "M2.5 2.5v5 M0 5h5"),
    "#": (6, "M2 1L1.2 9 M5 1l-.8 8 M0 3.6h6 M0 6.4h6"),
    ".": (1, "M.5 9.8h.01"),
    "-": (4, "M0 5.5h4"),
    "_": (5, "M0 10h5"),
    ">": (5, "M0 1.5L5 5 0 8.5"),
    "<": (5, "M5 1.5L0 5l5 3.5"),
    "/": (4, "M4 0L0 10"),
    "{": (4, "M4 0C2.5 0 2 .7 2 2v2c0 .7-.6 1-2 1 1.4 0 2 .3 2 1v2c0 1.3.5 2 2 2"),
    "}": (4, "M0 0c1.5 0 2 .7 2 2v2c0 .7.6 1 2 1-1.4 0-2 .3-2 1v2c0 1.3-.5 2-2 2"),
    "[": (3, "M3 0H0v10h3"),
    "]": (3, "M0 0h3v10H0"),
    " ": (3, ""),
    "λ": (5.4, "M0 0c1.6 0 2.4.8 2.9 2.6L5.4 10 M2.9 3.6L0 10"),
}


def label(text, cx, cy, height, colour, weight=None):
    """`text` in the stroke alphabet, centred on (cx, cy), `height` tall."""
    s = height / 10
    gap = 2.0
    chars = [FONT.get(ch, FONT.get(ch.upper(), FONT[" "])) for ch in text]
    width = sum(w for w, _ in chars) + gap * (len(chars) - 1)
    x = cx - width * s / 2
    y = cy - height / 2
    sw = (weight or height * 0.17) / s
    parts = []
    for w, d in chars:
        if d:
            parts.append(f'<path transform="translate({x:.2f} {y:.2f}) scale({s:.4f})" d="{d}" fill="none" '
                         f'stroke="{colour}" stroke-width="{sw:.3f}" stroke-linecap="round" stroke-linejoin="round"/>')
        x += (w + gap) * s
    return "".join(parts)


def text_width(text, height):
    s = height / 10
    chars = [FONT.get(ch, FONT.get(ch.upper(), FONT[" "])) for ch in text]
    return (sum(w for w, _ in chars) + 2.0 * (len(chars) - 1)) * s


# ---------- Cloud-drive marks (24 px grid, brand colours) ----------

BRAND = {
    "dropbox": '<g fill="#0061fe"><path d="M7 4.6l4.6 2.9L7 10.4 2.4 7.5z"/><path d="M17 4.6l4.6 2.9-4.6 2.9-4.6-2.9z"/>'
               '<path d="M7 10.9l4.6 2.9L7 16.7l-4.6-2.9z"/><path d="M17 10.9l4.6 2.9-4.6 2.9-4.6-2.9z"/>'
               '<path d="M12 15.4l4.4 2.8-4.4 2.6-4.4-2.6z"/></g>',
    "google-drive": '<path fill="#34a853" d="M8.6 3.8L2 15.2l3.3 5.6L12 9.5z"/><path fill="#fbbc04" d="M8.6 3.8h6.8l6.6 11.4h-6.8z"/>'
                    '<path fill="#4285f4" d="M5.3 20.8h13.4l3.3-5.6H8.7z"/>',
    "onedrive": '<path fill="#0078d4" d="M7 18.5a4.4 4.4 0 0 1-.7-8.8 6 6 0 0 1 11.4 1.7 3.6 3.6 0 0 1 .3 7.1z"/>',
    "nextcloud": '<g fill="none" stroke="#0082c9" stroke-width="2"><circle cx="12" cy="12" r="3.6"/>'
                 '<circle cx="4.8" cy="12" r="2"/><circle cx="19.2" cy="12" r="2"/></g>',
    "mega": '<circle cx="12" cy="12" r="8.6" fill="#d9272e"/><path d="M8.2 15.6V9l3.8 3.9L15.8 9v6.6" fill="none" '
            'stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>',
    "proton-drive": '<rect x="4" y="4" width="16" height="16" rx="5" fill="#6d4aff"/><path d="M10 16.5V8h3a2.6 2.6 0 0 1 0 5.2h-3" '
                    'fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>',
    "icloud": '<path fill="#3693f3" d="M7.2 18a4 4 0 0 1-.5-8 5.6 5.6 0 0 1 10.6 1.4A3.3 3.3 0 0 1 17.4 18z"/>'
              '<path d="M7.2 18a4 4 0 0 1-.5-8 5.6 5.6 0 0 1 10.6 1.4A3.3 3.3 0 0 1 17.4 18z" fill="none" stroke="#fff" '
              'stroke-opacity=".5" stroke-width=".8"/>',
    "box": '<rect x="3" y="6" width="18" height="12" rx="3" fill="#0061d5"/>'
           '<path d="M6.5 9v6 M6.5 12.6a1.9 1.9 0 1 0 3.8 0 1.9 1.9 0 0 0-3.8 0z M13.6 10.7a1.9 1.9 0 1 0 0 3.8 1.9 1.9 0 0 0 0-3.8z '
           'M16.6 10.8l2.4 3.6 M19 10.8l-2.4 3.6" fill="none" stroke="#fff" stroke-width="1.3" stroke-linecap="round"/>',
    "pcloud": '<path fill="#17bed0" d="M7.5 17.5a4 4 0 0 1-.6-8A5.5 5.5 0 0 1 17.4 11a3.3 3.3 0 0 1 .1 6.5z"/>'
              '<path d="M11 15.5v-5h1.8a1.6 1.6 0 0 1 0 3.2H11" fill="none" stroke="#fff" stroke-width="1.4" '
              'stroke-linecap="round" stroke-linejoin="round"/>',
    "syncthing": '<circle cx="12" cy="12" r="8" fill="none" stroke="#0891d1" stroke-width="1.8"/>'
                 '<circle cx="12" cy="12" r="1.6" fill="#0891d1"/><circle cx="18" cy="8.5" r="1.6" fill="#0891d1"/>'
                 '<circle cx="7" cy="16.5" r="1.6" fill="#0891d1"/><circle cx="6.5" cy="8" r="1.6" fill="#0891d1"/>'
                 '<path d="M12 12l6-3.5 M12 12l-5 4.5 M12 12L6.5 8" stroke="#0891d1" stroke-width="1.2"/>',
    "github": '<path fill="#e8e8ea" d="M12 3.5a8.5 8.5 0 0 0-2.7 16.6c.4.1.6-.2.6-.4v-1.5c-2.4.5-2.9-1-2.9-1-.4-1-1-1.3-1-1.3-.8-.5 '
              '0-.5 0-.5.9.1 1.3.9 1.3.9.8 1.3 2 1 2.5.7.1-.6.3-1 .6-1.2-1.9-.2-3.9-1-3.9-4.2 0-.9.3-1.7.9-2.3-.1-.2-.4-1.1.1-2.3 '
              '0 0 .7-.2 2.3.9a8 8 0 0 1 4.2 0c1.6-1.1 2.3-.9 2.3-.9.5 1.2.2 2.1.1 2.3.5.6.9 1.4.9 2.3 0 3.3-2 4-3.9 4.2.3.3.6.8.6 '
              '1.5v2.3c0 .2.2.5.6.4A8.5 8.5 0 0 0 12 3.5z"/>',
}


# ---------- Language marks (24 px grid) ----------
#
# Each returns an SVG fragment: the language's own colours, read at a glance.

def _badge(fill, text, fg="#ffffff", shape="square", h=7.0):
    """A coloured shape with letters on it, the common form for letter marks."""
    if shape == "square":
        base = f'<rect x="4" y="4" width="16" height="16" rx="3.5" fill="{fill}"/>'
        return base + label(text, 12, 12.6 if text in ("JS", "TS") else 12, h, fg)
    if shape == "hex":
        base = f'<path fill="{fill}" d="M12 2.8l8 4.6v9.2l-8 4.6-8-4.6V7.4z"/>'
        return base + label(text, 12, 12, h, fg)
    if shape == "circle":
        base = f'<circle cx="12" cy="12" r="8.6" fill="{fill}"/>'
        return base + label(text, 12, 12, h, fg)
    if shape == "shield":
        base = f'<path fill="{fill}" d="M4.5 3.5h15l-1.4 15L12 20.8l-6.1-2.3z"/>'
        return base + label(text, 12, 11.4, h, fg)
    raise ValueError(shape)


def _rust():
    teeth = "".join(
        f'<rect x="11.1" y="2.6" width="1.8" height="2.6" rx=".5" fill="#ce422b" transform="rotate({a} 12 12)"/>'
        for a in range(0, 360, 30))
    return (teeth + '<circle cx="12" cy="12" r="7.2" fill="#ce422b"/>'
            '<circle cx="12" cy="12" r="5.6" fill="none" stroke="#fff" stroke-opacity=".25" stroke-width=".6"/>'
            + label("R", 12, 12, 7.4, "#ffffff"))


def _python():
    return ('<path fill="#3776ab" d="M11.9 3c-4.4 0-4.1 1.9-4.1 1.9V7h4.2v.6H6.1S3 7.3 3 11.9s2.7 4.4 2.7 4.4h1.6v-2.2s-.1-2.7 '
            '2.7-2.7h4.2s2.6 0 2.6-2.5V5.6S17.2 3 11.9 3zM9.6 4.4a.8.8 0 1 1 0 1.6.8.8 0 0 1 0-1.6z"/>'
            '<path fill="#ffd43b" d="M12.1 21c4.4 0 4.1-1.9 4.1-1.9V17h-4.2v-.6h5.9s3.1.3 3.1-4.3-2.7-4.4-2.7-4.4h-1.6v2.2s.1 2.7-2.7 '
            '2.7h-4.2s-2.6 0-2.6 2.5v3.3S6.8 21 12.1 21zm2.3-1.4a.8.8 0 1 1 0-1.6.8.8 0 0 1 0 1.6z"/>')


def _go():
    return ('<path d="M2.5 10h4 M1.5 12.5h4 M3 15h3" stroke="#00add8" stroke-width="1.4" stroke-linecap="round"/>'
            + label("GO", 14.2, 12.4, 8, "#00add8", weight=2))


def _java():
    return ('<path d="M7 11h9v4.5a3.5 3.5 0 0 1-3.5 3.5h-2A3.5 3.5 0 0 1 7 15.5z M16 12h1a2 2 0 0 1 0 4h-1.2 M5.5 20.5h12" '
            'fill="none" stroke="#e76f00" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'
            '<path d="M10 9c-1-1.2 1-2-.2-3.6 M13 9c-1-1.2 1-2-.2-3.6" fill="none" stroke="#5382a1" stroke-width="1.4" '
            'stroke-linecap="round"/>')


def _kotlin():
    return ('<defs><linearGradient id="kt" x1="0" y1="1" x2="1" y2="0"><stop stop-color="#e44857"/><stop offset=".5" '
            'stop-color="#c711e1"/><stop offset="1" stop-color="#7f52ff"/></linearGradient></defs>'
            '<path fill="url(#kt)" d="M4 4h16L12 12l8 8H4z"/>')


def _swift():
    return ('<rect x="3.5" y="3.5" width="17" height="17" rx="4.5" fill="#f05138"/>'
            '<path fill="#fff" d="M16.8 15.4c.9-2.9-.4-6-2.9-8 1.4 2 2 4.4 1.3 6.2C12.8 12 9.8 9.9 7.6 7.6c1.5 1.7 3.2 3.2 4.6 4.2-1.8-1-4-2.5-5.6-4 '
            '1.5 2.2 4 4.6 6.3 5.8-2.3 1-5 .4-7.2-.9 2 2.3 5.6 3.5 8.8 2.2 1-.4 1.8-.3 2.3.4.2-.6 0-1.4-.4-1.9z"/>')


def _ruby():
    return ('<path fill="#cc342d" d="M7 4.5h10l3.5 5L12 20 3.5 9.5z"/>'
            '<path d="M3.5 9.5h17 M7 4.5l2 5 3 10.5 3-10.5 2-5 M9 9.5L12 4.5l3 5" fill="none" stroke="#fff" stroke-opacity=".45" '
            'stroke-width=".9" stroke-linejoin="round"/>')


def _lua():
    return ('<circle cx="11" cy="13" r="7.5" fill="#000080"/><circle cx="13.6" cy="10.4" r="2.2" fill="#fff"/>'
            '<circle cx="19" cy="5" r="2.2" fill="#000080"/>' + label("L", 9.6, 14.6, 5.2, "#ffffff", weight=1.3))


def _shell():
    return ('<rect x="3" y="4.5" width="18" height="15" rx="3" fill="#2b2b30"/>'
            '<path d="M7 9.5l3 2.5-3 2.5 M12 15h5" fill="none" stroke="#89e051" stroke-width="1.8" stroke-linecap="round" '
            'stroke-linejoin="round"/>')


def _markdown():
    return ('<rect x="2.5" y="6" width="19" height="12" rx="2.5" fill="none" stroke="#a3a3ab" stroke-width="1.5"/>'
            '<path d="M5.8 15V9l2.4 3 2.4-3v6 M15.8 9v5.6 M13.6 12.6l2.2 2.4 2.2-2.4" fill="none" stroke="#a3a3ab" stroke-width="1.5" '
            'stroke-linecap="round" stroke-linejoin="round"/>')


def _sql():
    return ('<path fill="#e38c00" d="M12 4c3.8 0 6.8 1.2 6.8 2.7v10.6c0 1.5-3 2.7-6.8 2.7s-6.8-1.2-6.8-2.7V6.7C5.2 5.2 8.2 4 12 4z"/>'
            '<path d="M5.2 6.7c0 1.5 3 2.7 6.8 2.7s6.8-1.2 6.8-2.7 M5.2 12c0 1.5 3 2.7 6.8 2.7s6.8-1.2 6.8-2.7" fill="none" '
            'stroke="#fff" stroke-opacity=".7" stroke-width="1"/>')


def _dart():
    return ('<path fill="#0175c2" d="M5.5 15.5L4 8.5 8.5 4l9.5 1.5 2.5 2.5v9l-3 3h-9z"/>'
            '<path fill="#13b9fd" d="M5.5 15.5L15 6l5.5 2v8.5h-8.5z"/>')


def _haskell():
    return ('<path d="M3 19l4.5-7L3 5h3l4.5 7L6 19z" fill="#453a62"/><path d="M7.5 19L12 12 7.5 5h3l9 14h-3l-2.8-4.4L10.5 19z" '
            'fill="#5e5086"/><path d="M15.5 10.2h5.5v2h-4.2z M16.8 13.4H21v2h-2.9z" fill="#8f4e8b"/>')


def _elixir():
    return ('<path fill="#6e4a7e" d="M12.5 3.5c-3 3.6-6.5 8.2-6.5 11.4a6 6 0 0 0 12 0c0-3.7-3-5.3-3.3-8.5-.9 1.4-.9 3.3 0 5-1.9-1.5-2.5-4.7-2.2-7.9z"/>'
            '<path fill="#fff" fill-opacity=".35" d="M9.5 15.5c.2 1.8 1.3 3 3 3.3-2.6.8-4.5-1.3-3-3.3z"/>')


def _nix():
    arms = "".join(
        f'<path d="M12 12l0-7.5 M10.2 6.2l1.8-1.7 1.8 1.7" fill="none" stroke="{c}" stroke-width="1.8" stroke-linecap="round" '
        f'stroke-linejoin="round" transform="rotate({a} 12 12)"/>'
        for a, c in zip(range(0, 360, 60), ["#5277c3", "#7ebae4"] * 3))
    return arms


def _cmake():
    return ('<path fill="#064f8c" d="M12 3.5l8.5 16.5H12z"/><path fill="#e8e8ea" fill-opacity=".9" d="M12 3.5L3.5 20 12 14z"/>'
            '<path fill="#e72a2b" d="M3.5 20H20.5l-8.5-6z"/>')


def _vue():
    return '<path fill="#41b883" d="M2.5 4.5h4l5.5 9.5 5.5-9.5h4L12 20.5z"/><path fill="#35495e" d="M6.5 4.5h3L12 9l2.5-4.5h3L12 14z"/>'


def _julia():
    return ('<circle cx="12" cy="7" r="3.4" fill="#389826"/><circle cx="7" cy="15.5" r="3.4" fill="#cb3c33"/>'
            '<circle cx="17" cy="15.5" r="3.4" fill="#9558b2"/>')


def _scala():
    return ''.join(f'<path fill="#dc322f" d="M6 {y}c4 .8 9 1.5 12 3.2v2.8c-3-1.7-8-2.4-12-3.2z"/>' for y in (4.5, 10, 15.5))


def _clojure():
    return ('<circle cx="12" cy="12" r="8.6" fill="#5881d8"/><path d="M12 3.4a8.6 8.6 0 0 1 0 17.2z" fill="#63b132"/>'
            + label("λ", 12, 12, 7, "#ffffff"))


def _docker():
    blocks = "".join(f'<rect x="{x}" y="{y}" width="2.6" height="2.4" rx=".3" fill="#1d63ed"/>'
                     for x, y in [(5, 10.5), (8, 10.5), (11, 10.5), (14, 10.5), (8, 7.7), (11, 7.7), (14, 7.7), (11, 4.9)])
    return blocks + ('<path fill="#1d63ed" d="M3 13.6h16.5c.6-1 1.6-1.4 2.5-1.3-.4 1.6-1.4 2.6-2.6 2.8C17.8 18.6 14.6 20 11 20 '
                     '6.3 20 3.6 17.5 3 13.6z"/>')


def _diff():
    return ('<rect x="4" y="4" width="16" height="16" rx="3.5" fill="#2b2b30"/>'
            '<path d="M12 7v5 M9.5 9.5h5" stroke="#46d08a" stroke-width="1.8" stroke-linecap="round"/>'
            '<path d="M9.5 16h5" stroke="#ff6b6b" stroke-width="1.8" stroke-linecap="round"/>')


LANG = {
    # key: (mark, linguist-ish colour used for page outlines and badges, short label)
    "rust": (_rust, "#ce422b", "RS"),
    "python": (_python, "#3776ab", "PY"),
    "javascript": (lambda: _badge("#f7df1e", "JS", "#1d1d1f"), "#e5c800", "JS"),
    "typescript": (lambda: _badge("#3178c6", "TS"), "#3178c6", "TS"),
    "go": (_go, "#00add8", "GO"),
    "c": (lambda: _badge("#659bd3", "C", shape="hex", h=8), "#659bd3", "C"),
    "cpp": (lambda: _badge("#00599c", "C++", shape="hex", h=6), "#3a87d1", "CPP"),
    "csharp": (lambda: _badge("#68217a", "C#", shape="hex", h=6.4), "#9b4fb4", "CS"),
    "java": (_java, "#e76f00", "JAVA"),
    "kotlin": (_kotlin, "#7f52ff", "KT"),
    "swift": (_swift, "#f05138", "SWIFT"),
    "ruby": (_ruby, "#cc342d", "RB"),
    "php": (lambda: _badge("#777bb3", "PHP", shape="circle", h=5.4), "#777bb3", "PHP"),
    "lua": (_lua, "#4a4ad8", "LUA"),
    "shell": (_shell, "#89e051", "SH"),
    "html": (lambda: _badge("#e34f26", "<>", shape="shield", h=6.4), "#e34f26", "HTML"),
    "css": (lambda: _badge("#663399", "{}", shape="shield", h=6.4), "#8d5fd3", "CSS"),
    "scss": (lambda: _badge("#cd6799", "S", shape="circle", h=8), "#cd6799", "SCSS"),
    "json": (lambda: _badge("#2b2b30", "{}", "#f2b545", h=8), "#f2b545", "JSON"),
    "yaml": (lambda: _badge("#cb171e", "Y", h=8), "#e0484e", "YAML"),
    "toml": (lambda: _badge("#9c4221", "[]", h=8), "#c2622f", "TOML"),
    "xml": (lambda: _badge("#2b2b30", "</>", "#4cc9d6", h=6), "#4cc9d6", "XML"),
    "markdown": (_markdown, "#a3a3ab", "MD"),
    "sql": (_sql, "#e38c00", "SQL"),
    "dart": (_dart, "#0175c2", "DART"),
    "zig": (lambda: _badge("#f7a41d", "Z", "#1d1d1f", h=9), "#f7a41d", "ZIG"),
    "haskell": (_haskell, "#5e5086", "HS"),
    "elixir": (_elixir, "#6e4a7e", "EX"),
    "erlang": (lambda: _badge("#a90533", "E", shape="circle", h=8), "#c4224a", "ERL"),
    "nix": (_nix, "#7ebae4", "NIX"),
    "makefile": (lambda: _badge("#427819", "M", h=8), "#6aa83a", "MAKE"),
    "cmake": (_cmake, "#3a87d1", "CMAKE"),
    "perl": (lambda: _badge("#39457e", "PL", shape="circle", h=6.4), "#5868b0", "PL"),
    "r": (lambda: _badge("#276dc3", "R", shape="circle", h=8), "#276dc3", "R"),
    "julia": (_julia, "#9558b2", "JL"),
    "scala": (_scala, "#dc322f", "SCALA"),
    "vue": (_vue, "#41b883", "VUE"),
    "ocaml": (lambda: _badge("#ec6813", "ML", h=6.4), "#ec6813", "ML"),
    "clojure": (_clojure, "#5881d8", "CLJ"),
    "fortran": (lambda: _badge("#4d41b1", "F", h=8), "#7a6fe0", "F90"),
    "assembly": (lambda: _badge("#6e4c13", "ASM", h=5.4), "#b5893a", "ASM"),
    "vala": (lambda: _badge("#a56de2", "V", shape="circle", h=8), "#a56de2", "VALA"),
    "docker": (_docker, "#1d63ed", "DOCK"),
    "diff": (_diff, "#46d08a", "DIFF"),
    "d": (lambda: _badge("#b03931", "D", h=8), "#c9504a", "D"),
    "objc": (lambda: _badge("#438eff", "OC", shape="hex", h=6.4), "#438eff", "M"),
    "groovy": (lambda: _badge("#4298b8", "G", shape="circle", h=8), "#4298b8", "GVY"),
    "powershell": (lambda: _badge("#012456", ">_", "#ffffff", h=6.4), "#3c6fb4", "PS1"),
    "tex": (lambda: _badge("#3d6117", "TEX", h=5.4), "#5f9636", "TEX"),
    "gdscript": (lambda: _badge("#478cbf", "GD", h=6.4), "#478cbf", "GD"),
}
