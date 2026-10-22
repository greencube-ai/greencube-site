#!/bin/sh
# Rebuild every translated main page, then menus, redirects, sitemap and a parse check of every script.
# Run from the site folder: sh i18n/build_all.sh
set -e
export PYTHONIOENCODING=utf-8
PAGES="index.html buy.html what-you-get.html download.html your-data.html mission.html ai-environmental-impact.html how-much-water-does-ai-use.html"
python i18n/i18n.py scripts
for f in i18n/??.json i18n/??-??.json; do
  [ -f "$f" ] || continue
  lang=$(basename "$f" .json)
  python i18n/i18n.py build "$lang" $PAGES | grep -v ": 0 missing" || true
done
python i18n/i18n.py switcher > /dev/null
python i18n/i18n.py redirects
python i18n/i18n.py sitemap
node i18n/check.cjs
