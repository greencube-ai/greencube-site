#!/bin/bash
set -e
echo ""
echo "   ╔═╗╦═╗╔═╗╔═╗╔╗╔╔═╗╦ ╦╔╗ ╔═╗"
echo "   ║ ╦╠╦╝║╣ ║╣ ║║║║  ║ ║╠╩╗║╣ "
echo "   ╚═╝╩╚═╚═╝╚═╝╝╚╝╚═╝╚═╝╚═╝╚═╝"
echo "   your agent learns from every task"
echo ""

OS="$(uname -s)"
REPO="greencube-ai/greencube"
VERSION="v1.0.0"

if [ "$OS" = "Darwin" ]; then
  URL="https://github.com/$REPO/releases/download/$VERSION/GreenCube_0.7.0_x64.dmg"
  echo "downloading GreenCube for Mac..."
  curl -sL "$URL" -o /tmp/GreenCube.dmg
  echo "opening installer..."
  open /tmp/GreenCube.dmg
  echo ""
  echo "drag GreenCube to Applications. then run it."
  echo "then add this line before running your agent:"
  echo ""
  echo "  export OPENAI_API_BASE=http://localhost:9000/v1"
  echo ""
  echo "thats it. your agent now learns from every task."
elif [ "$OS" = "Linux" ]; then
  echo "linux build coming soon."
  echo "for now, build from source: github.com/$REPO"
else
  echo "for windows, run this in PowerShell:"
  echo "  irm greencube.world/install.ps1 | iex"
fi
