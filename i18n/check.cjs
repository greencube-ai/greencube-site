// Parse every inline script and JSON-LD block of every main page in every language; exit 1 on any error.
const fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..');
const dirs = ['.'].concat(fs.readdirSync(root).filter((d) => /^[a-z]{2}(-[a-z]{2})?$/.test(d) && fs.statSync(path.join(root, d)).isDirectory()));
let bad = 0, n = 0;
for (const d of dirs) {
  for (const f of fs.readdirSync(path.join(root, d)).filter((f) => f.endsWith('.html'))) {
    const s = fs.readFileSync(path.join(root, d, f), 'utf8');
    for (const m of s.matchAll(/<script(?![^>]*\bsrc=)([^>]*)>([\s\S]*?)<\/script>/g)) {
      n++;
      try {
        if (/ld\+json/.test(m[1])) JSON.parse(m[2]);
        else if (!/type=['"]module/.test(m[1])) new Function(m[2]);
      } catch (e) { bad++; console.log(path.join(d, f), e.message); }
    }
  }
}
for (const f of ['tier-quiz.js', 'send-to-pc.js']) {
  try { new Function(fs.readFileSync(path.join(root, f), 'utf8')); } catch (e) { bad++; console.log(f, e.message); }
}
console.log(bad ? `${bad} broken of ${n} scripts` : `all ${n} scripts parse`);
process.exit(bad ? 1 : 0);
