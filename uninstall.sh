#!/usr/bin/env bash
# Remove Umbra and go back to the icon theme used before it.
set -euo pipefail
data=${XDG_DATA_HOME:-$HOME/.local/share}
if [[ -x $data/umbra-icons/bin/umbra-icons ]]; then
  "$data/umbra-icons/bin/umbra-icons" remove
fi
rm -rf "$data/umbra-icons"
rm -f "$HOME/.local/bin/umbra-icons"
printf '\033[1m==>\033[0m %s\n' "Umbra removed."
