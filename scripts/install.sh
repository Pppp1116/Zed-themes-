#!/usr/bin/env bash
set -euo pipefail

THEMES_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/zed/themes"
mkdir -p "$THEMES_DIR"

cp -f ./themes/*.json "$THEMES_DIR/"
cp -f ./themes/experimental/*.json "$THEMES_DIR/" 2>/dev/null || true

echo "Installed themes into: $THEMES_DIR"
echo "Restart Zed and open the Theme Selector."
