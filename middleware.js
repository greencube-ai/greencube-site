// Visitors where Stripe charges US$9.99 see the price in dollars; everyone else sees the page as written (€9.99).
// Stripe's payment link has one price, EUR 9.99 with USD 9.99 as an extra currency, and picks the currency from
// the buyer's location. Vercel knows the same thing from the visitor's IP (x-vercel-ip-country), so the page and
// the checkout agree. Nothing is stored and nothing is asked of a third party. Page heads already say both
// prices ("€9.99 (US$9.99)"), and a price written that way is left alone here.

// Where US dollars are the local currency, so Stripe charges USD.
const USD = new Set(['US', 'PR', 'GU', 'VI', 'AS', 'MP', 'UM', 'EC', 'SV', 'TL', 'FM', 'MH', 'PW', 'VG', 'TC', 'BQ']);

const LANGS = 'es|pt|fr|de|it|nl|pl|tr|ru|uk|ar|hi|id|vi|th|ja|ko|zh|zh-tw';
const PAGES = 'buy|what-you-get|download|mission|your-data|ai-environmental-impact|how-much-water-does-ai-use|does-chatgpt-train-on-your-data';
const PRICED = new RegExp(`^/(?:(${LANGS})(?:/|$))?(?:(?:${PAGES})/?)?$`);

const SKIP = 'x-greencube-price';  // marks our own fetch of the page, so it is not swapped twice

export const config = { matcher: ['/((?!blog|.*\\.).*)'] };

export default async function middleware(request) {
  const url = new URL(request.url);
  const page = PRICED.exec(url.pathname);
  if (!page || request.method !== 'GET' || request.headers.get(SKIP)
      || !USD.has(request.headers.get('x-vercel-ip-country') || '')) return next();
  try {
    const res = await fetch(url, { headers: { [SKIP]: '1', 'accept': 'text/html' } });
    if (!res.ok || !(res.headers.get('content-type') || '').includes('text/html')) return next();
    const headers = new Headers(res.headers);
    headers.delete('content-length');
    headers.delete('content-encoding');
    headers.delete('etag');
    headers.set('cache-control', 'private, no-cache');
    return new Response(toDollars(await res.text(), page[1] || 'en'), { status: res.status, headers });
  } catch {
    return next();  // the page as written, in euros
  }
}

function next() {
  return new Response(null, { headers: { 'x-middleware-next': '1' } });
}

// Our price (9.99) and the usual paid plan (20 a month), written in euros, rewritten in dollars in the same spot.
// "$" in English; "US$" in other languages, where "$" alone can mean a local peso. A price followed by "(" already
// has its dollar price next to it.
const AMOUNT = '(?:9[.,]99|20)(?![\\d.,]\\d)';
const SEP = '(&nbsp;|\\u00a0| )?';
const NOT_BOTH = '(?!(?:\\s|&nbsp;)*\\()';
const BEFORE = new RegExp(`(?:€|&euro;)${SEP}(${AMOUNT})${NOT_BOTH}`, 'g');
const AFTER = new RegExp(`(?<![\\d.,])(${AMOUNT})${SEP}(?:€|&euro;)${NOT_BOTH}`, 'g');

export function toDollars(html, lang) {
  const sign = lang === 'en' ? '$' : 'US$';
  return html
    .replace(/<span class="cur">€<\/span>/g, () => `<span class="cur">${sign}</span>`)
    .replace(BEFORE, (_, sep, n) => `${sign}${sep || ''}${n}`)
    .replace(AFTER, (_, n, sep) => `${n}${sep || ''}${sign}`)
    .replace(/currency: 'EUR'/g, "currency: 'USD'");
}
