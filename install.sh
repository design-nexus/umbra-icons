#!/usr/bin/env bash
# Install the Umbra icon themes and use them.
#
#   curl -fsSL https://raw.githubusercontent.com/design-nexus/umbra-icons/main/install.sh | bash
#
# Builds Umbra, Umbra Solid and Umbra Line in your Omarchy theme's colours, switches to
# Umbra (pass --look solid or --look line for another), and rebuilds them whenever the
# theme changes. `umbra-icons remove` goes back to the icon theme you had.
set -euo pipefail

REPO="design-nexus/umbra-icons"
say() { printf '\033[1m==>\033[0m %s\n' "$*"; }
die() { printf '\033[31m==>\033[0m %s\n' "$*" >&2; exit 1; }

command -v python3 >/dev/null || die "Python 3 is needed."
python3 -c 'import sys; sys.exit(sys.version_info < (3, 11))' || die "Python 3.11 or newer is needed."

# This checkout, or a fresh one when piped from curl.
here=""
[[ -n ${BASH_SOURCE[0]:-} && -f ${BASH_SOURCE[0]} ]] && here=$(cd "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
if [[ -n $here && -d $here/umbra && -f $here/bin/umbra-icons ]]; then
  src=$here
else
  say "Fetching Umbra"
  if command -v git >/dev/null; then
    git clone -q --depth 1 "https://github.com/$REPO.git" "$work/src"
  else
    mkdir -p "$work/src"
    curl -fsSL "https://github.com/$REPO/archive/refs/heads/main.tar.gz" | tar -xz -C "$work/src" --strip-components=1
  fi
  src="$work/src"
fi

data=${XDG_DATA_HOME:-$HOME/.local/share}
dest="$data/umbra-icons"
say "Installing to $dest"
rm -rf "$dest.new"
mkdir -p "$dest.new"
cp -a "$src/umbra" "$src/symbolic" "$src/bin" "$src/LICENSE" "$dest.new/"
rm -rf "$dest.new/umbra/__pycache__"
rm -rf "$dest"
mv "$dest.new" "$dest"
mkdir -p "$HOME/.local/bin"
ln -sf "$dest/bin/umbra-icons" "$HOME/.local/bin/umbra-icons"

"$dest/bin/umbra-icons" install "$@"
case ":$PATH:" in *":$HOME/.local/bin:"*) ;; *) say "Add ~/.local/bin to your PATH to run umbra-icons." ;; esac
