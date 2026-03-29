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
echo -e "${DIM}   your agent learns from every task${RESET}"
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

  echo ""
  echo -e "${GREEN}${BOLD}done.${RESET} drag GreenCube to Applications, then launch it."
  echo ""
  echo -e "then add this line before running your agent:"
  echo ""
  echo -e "  ${GREEN}export OPENAI_API_BASE=http://localhost:9000/v1${RESET}"
  echo ""
  echo -e "${DIM}that's it. your agent now learns from every task.${RESET}"

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

  echo ""
  echo -e "${GREEN}${BOLD}done.${RESET} launch GreenCube from your app menu or run ${BOLD}greencube${RESET}."
  echo ""
  echo -e "then add this line before running your agent:"
  echo ""
  echo -e "  ${GREEN}export OPENAI_API_BASE=http://localhost:9000/v1${RESET}"
  echo ""
  echo -e "${DIM}that's it. your agent now learns from every task.${RESET}"

# --- Windows (git bash / WSL / MSYS) ---
else
  echo ""
  echo -e "looks like you're on Windows. run this instead:"
  echo ""
  echo -e "  ${GREEN}powershell -c \"irm https://greencube.world/install.ps1 | iex\"${RESET}"
  echo ""
fi
