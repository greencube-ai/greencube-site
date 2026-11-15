// Visitors where Stripe charges US$9.99 see the price in dollars; everyone else sees the page as written (€9.99).
// Stripe's payment link has one price, EUR 9.99 with USD 9.99 as an extra currency, and picks the currency from
// the buyer's location. Vercel knows the same thing from the visitor's IP (x-vercel-ip-country), so the page and
// the checkout agree. Nothing is stored and nothing is asked of a third party. Page heads already say both
// prices ("€9.99 (US$9.99)"), and a price written that way is left alone here.

// Where US dollars are the local currency, so Stripe charges USD.
const USD = new Set(['US', 'PR', 'GU', 'VI', 'AS', 'MP', 'UM', 'EC', 'SV', 'TL', 'FM', 'MH', 'PW', 'VG', 'TC', 'BQ']);

// Everywhere else outside the euro: the page keeps €9.99 and adds an approximate price in the visitor's own currency
// under the big price. Stripe Adaptive Pricing shows the exact amount in that currency at checkout, so ours says "≈".
// Rates: EUR -> currency, snapshot 15 Nov 2026 (open.er-api.com). Refresh about once a month. Russia is left out
// (Stripe does not take payments there).
const EUR_RATE = { GBP: 0.8348, CAD: 1.5734, AUD: 1.6281, NZD: 1.9962, INR: 104.03, BRL: 6.238, MXN: 20.46, COP: 3642, CLP: 1097.7, PEN: 3.762, ARS: 1707.6, PLN: 4.406, TRY: 55.58, UAH: 50.25, JPY: 176.3, KRW: 1475.7, CNY: 7.384, TWD: 36.35, HKD: 8.662, THB: 37.42, VND: 28440, IDR: 20125, MYR: 4.514, PHP: 70.47, SGD: 1.421, SAR: 4.139, AED: 4.054, EGP: 59.02, MAD: 10.95, CHF: 0.925, SEK: 11.11, NOK: 10.56, DKK: 7.476, CZK: 24.41, HUF: 365.0, RON: 5.349, ZAR: 18.68, ILS: 3.545, PKR: 305.3, BDT: 137.6, NGN: 1472, KES: 143.9, QAR: 4.018, KWD: 0.3428 };
const LOCAL_CURRENCY = { GB: 'GBP', CA: 'CAD', AU: 'AUD', NZ: 'NZD', IN: 'INR', BR: 'BRL', MX: 'MXN', CO: 'COP', CL: 'CLP', PE: 'PEN', AR: 'ARS', PL: 'PLN', TR: 'TRY', UA: 'UAH', JP: 'JPY', KR: 'KRW', CN: 'CNY', TW: 'TWD', HK: 'HKD', TH: 'THB', VN: 'VND', ID: 'IDR', MY: 'MYR', PH: 'PHP', SG: 'SGD', SA: 'SAR', AE: 'AED', EG: 'EGP', MA: 'MAD', CH: 'CHF', LI: 'CHF', SE: 'SEK', NO: 'NOK', DK: 'DKK', CZ: 'CZK', HU: 'HUF', RO: 'RON', ZA: 'ZAR', IL: 'ILS', PK: 'PKR', BD: 'BDT', NG: 'NGN', KE: 'KES', QA: 'QAR', KW: 'KWD' };

const LANGS = 'es|pt|fr|de|it|nl|pl|tr|ru|uk|ar|hi|id|vi|th|ja|ko|zh|zh-tw';
const PAGES = 'buy|get|what-you-get|download|mission|your-data|ai-environmental-impact|how-much-water-does-ai-use|does-chatgpt-train-on-your-data';
const PRICED = new RegExp(`^/(?:(${LANGS})(?:/|$))?(?:(?:${PAGES})/?)?$`);

const SKIP = 'x-greencube-price';  // marks our own fetch of the page, so it is not swapped twice

export const config = { matcher: ['/((?!blog|.*\\.).*)'] };

export default async function middleware(request) {
  const url = new URL(request.url);
  const page = PRICED.exec(url.pathname);
  const country = request.headers.get('x-vercel-ip-country') || '';
  const local = LOCAL_CURRENCY[country];
  if (!page || request.method !== 'GET' || request.headers.get(SKIP) || !(USD.has(country) || local)) return next();
  try {
    const res = await fetch(url, { headers: { [SKIP]: '1', 'accept': 'text/html' } });
    if (!res.ok || !(res.headers.get('content-type') || '').includes('text/html')) return next();
    const headers = new Headers(res.headers);
    headers.delete('content-length');
    headers.delete('content-encoding');
    headers.delete('etag');
    headers.set('cache-control', 'private, no-cache');
    const html = await res.text(), lang = page[1] || 'en';
    return new Response(USD.has(country) ? toDollars(html, lang) : withLocal(html, lang, local), { status: res.status, headers });
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

// "≈ £8.34", "≈ ₹1,040", "≈ ¥1,760": 9.99 euros in the visitor's currency, rounded so it reads as an estimate.
export function approx(lang, currency) {
  const v = 9.99 * EUR_RATE[currency];
  const n = v >= 1000 ? Math.round(v / 10 ** (Math.floor(Math.log10(v)) - 2)) * 10 ** (Math.floor(Math.log10(v)) - 2)
          : v >= 100 ? Math.round(v) : Math.round(v * 100) / 100;
  const fmt = (loc) => new Intl.NumberFormat(loc, {
    style: 'currency', currency, maximumFractionDigits: n >= 100 ? 0 : 2, minimumFractionDigits: n >= 100 ? 0 : 2,
  }).format(n);
  try {
    const t = fmt(lang === 'en' ? 'en' : lang);
    // a bare "$" (Taiwan dollars on a Chinese page) or the raw code ("204 MXN") reads badly: use the English form (NT$, MX$)
    return /(^|[^A-Za-z])\$/.test(t) || t.includes(currency) ? fmt('en') : t;
  } catch {
    return `${n} ${currency}`;
  }
}

export function withLocal(html, lang, currency) {
  const text = approx(lang, currency);
  const note = 'Approximate. Stripe shows the exact amount in your currency at checkout.';
  return html.replace(/(<span class="amount"><span class="cur">€<\/span>9[.,]99<\/span>)/g, (m) =>
    `${m}<span class="approx" title="${note}" style="display:block;font-size:.34em;font-weight:500;letter-spacing:0;opacity:.72;margin-top:.15em;white-space:nowrap">≈ ${text}</span>`);
}
