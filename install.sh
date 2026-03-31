#!/bin/bash
set -e

# Colors
GREEN='\033[0;32m'
DIM='\033[2m'
BOLD='\033[1m'
RESET='\033[0m'

echo ""
echo -e "${GREEN}${BOLD}   ╔═╗╦═╗╔═╗╔═╗╔╗╔╔═╗╦ ╦╔╗ ╔═╗${RESET}"
echo -e "${GREEN}${BOLD}   ║ ╦╠╦╝║╣ ║╣ ║║║║  ║ ║╠╩╗║╣ ${RESET}"
echo -e "${GREEN}${BOLD}   ╚═╝╩╚═╚═╝╚═╝╝╚╝╚═╝╚═╝╚═╝╚═╝${RESET}"
echo -e "${DIM}   your agent stops repeating mistakes${RESET}"
echo ""

REPO="greencube-ai/greencube"
VERSION="latest"

# Detect OS
OS="$(uname -s)"
ARCH="$(uname -m)"

get_latest_version() {
  curl -fsSL "https://api.github.com/repos/$REPO/releases/latest" | grep '"tag_name"' | sed -E 's/.*"([^"]+)".*/\1/'
}

fail() {
  echo -e "\n${BOLD}error:${RESET} $1" >&2
  exit 1
}

# Add gc alias to shell config
add_alias() {
  local ALIAS_LINE='gc() { for p in $(seq 9000 9010); do curl -s "localhost:$p/health" >/dev/null 2>&1 && curl -s "localhost:$p/b" && return; done; echo "GreenCube is not running. Open the app first."; }'
  for rc in "$HOME/.bashrc" "$HOME/.zshrc"; do
    if [ -f "$rc" ]; then
      if ! grep -q 'alias gc=' "$rc" 2>/dev/null; then
        echo "" >> "$rc"
        echo "# GreenCube — check your agent's brain" >> "$rc"
        echo "$ALIAS_LINE" >> "$rc"
      fi
    fi
  done
  # Also add to .zshrc if zsh exists but file doesn't yet
  if command -v zsh &>/dev/null && [ ! -f "$HOME/.zshrc" ]; then
    echo "# GreenCube — check your agent's brain" > "$HOME/.zshrc"
    echo "$ALIAS_LINE" >> "$HOME/.zshrc"
  fi
}

# --- macOS ---
if [ "$OS" = "Darwin" ]; then
  echo "detecting latest release..."
  VERSION=$(get_latest_version) || fail "could not reach GitHub. check your internet connection."

  if [ "$ARCH" = "arm64" ]; then
    ASSET="GreenCube_${VERSION#v}_aarch64.dmg"
  else
    ASSET="GreenCube_${VERSION#v}_x64.dmg"
  fi

  URL="https://github.com/$REPO/releases/download/$VERSION/$ASSET"
  echo "downloading GreenCube $VERSION for macOS ($ARCH)..."
  curl -fSL --progress-bar "$URL" -o /tmp/GreenCube.dmg || fail "download failed. release may not exist yet — check github.com/$REPO/releases"

  echo "opening installer..."
  open /tmp/GreenCube.dmg

  add_alias

  echo ""
  echo -e "${GREEN}${BOLD}done.${RESET} drag GreenCube to Applications, then launch it."
  echo ""
  echo -e "  type ${GREEN}${BOLD}gc${RESET} anytime to see what your agent learned."
  echo ""
  echo -e "${DIM}  (restart your terminal or run: source ~/.zshrc)${RESET}"
  echo ""

# --- Linux ---
elif [ "$OS" = "Linux" ]; then
  echo "detecting latest release..."
  VERSION=$(get_latest_version) || fail "could not reach GitHub. check your internet connection."

  if [ "$ARCH" = "x86_64" ]; then
    ASSET="green-cube_${VERSION#v}_amd64.deb"
  elif [ "$ARCH" = "aarch64" ]; then
    ASSET="green-cube_${VERSION#v}_arm64.deb"
  else
    fail "unsupported architecture: $ARCH"
  fi

  URL="https://github.com/$REPO/releases/download/$VERSION/$ASSET"
  echo "downloading GreenCube $VERSION for Linux ($ARCH)..."
  curl -fSL --progress-bar "$URL" -o /tmp/greencube.deb || fail "download failed. release may not exist yet — check github.com/$REPO/releases"

  echo "installing..."
  if command -v sudo &>/dev/null; then
    sudo dpkg -i /tmp/greencube.deb || sudo apt-get install -f -y
  else
    dpkg -i /tmp/greencube.deb || apt-get install -f -y
  fi
  rm -f /tmp/greencube.deb

  add_alias

  echo ""
  echo -e "${GREEN}${BOLD}done.${RESET} launch GreenCube from your app menu or run ${BOLD}greencube${RESET}."
  echo ""
  echo -e "  type ${GREEN}${BOLD}gc${RESET} anytime to see what your agent learned."
  echo ""
  echo -e "${DIM}  (restart your terminal or run: source ~/.bashrc)${RESET}"
  echo ""

# --- Windows (git bash / WSL / MSYS) ---
else
  echo ""
  echo -e "looks like you're on Windows. run this instead:"
  echo ""
  echo -e "  ${GREEN}powershell -c \"irm https://greencube.world/install.ps1 | iex\"${RESET}"
  echo ""
fi
