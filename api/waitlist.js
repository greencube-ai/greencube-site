// Waitlist signup endpoint. Lives on greencube.world itself (Vercel
// serverless), so Spanish ISPs that block Cloudflare ranges during
// LaLiga windows still let signups through.
//
// Forwards the email to WAITLIST_INBOX (defaults to fathector7@gmail.com)
// via Resend (https://resend.com — free 3K/mo, AWS SES under the hood,
// not on Cloudflare).
//
// If RESEND_API_KEY is not configured, the function still returns ok:true
// and prints the signup to Vercel logs — so leads aren't lost while the
// inbox gets wired.

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ ok: false, error: 'method_not_allowed' });
  }

  let body = req.body;
  if (typeof body === 'string') {
    try { body = JSON.parse(body); } catch { body = {}; }
  }
  body = body || {};

  // honeypot — silent ok if a bot filled it
  if (body.hp) return res.status(200).json({ ok: true });

  const email = String(body.email || '').trim().toLowerCase();
  if (!EMAIL_RE.test(email)) {
    return res.status(400).json({ ok: false, error: 'invalid_email' });
  }

  const referrer = String(body.referrer || '(direct)').slice(0, 200);
  const ua       = String(req.headers['user-agent'] || '?').slice(0, 200);
  const ip       = req.headers['x-forwarded-for'] || req.headers['x-real-ip'] || '';

  const apiKey = process.env.RESEND_API_KEY;
  const inbox  = process.env.WAITLIST_INBOX || 'fathector7@gmail.com';

  // Always log so signups aren't lost if email delivery fails or isn't wired.
  console.log('[waitlist]', JSON.stringify({ email, referrer, ip, ua }));

  if (!apiKey) {
    return res.status(200).json({ ok: true, logged: true });
  }

  // 1) Notification to the inbox owner — same as before.
  try {
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + apiKey,
      },
      body: JSON.stringify({
        from: 'GreenCube waitlist <onboarding@resend.dev>',
        to: [inbox],
        reply_to: email,
        subject: 'Waitlist — ' + email,
        text:
          'New GreenCube waitlist signup\n\n' +
          'Email: ' + email + '\n' +
          'From:  ' + referrer + '\n' +
          'IP:    ' + ip + '\n' +
          'UA:    ' + ua + '\n',
      }),
    });
    if (!r.ok) {
      const err = await r.text().catch(() => '');
      console.error('[waitlist] resend failed', r.status, err);
      // Still return ok:true — we've logged the signup, don't show the user an error.
      return res.status(200).json({ ok: true, logged: true });
    }
  } catch (e) {
    console.error('[waitlist] resend exception', String(e));
    return res.status(200).json({ ok: true, logged: true });
  }

  // 2) Confirmation to the user. Fire-and-best-effort — if this fails, the
  //    signup is still considered successful and we still got our notification.
  try {
    const confirm = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + apiKey,
      },
      body: JSON.stringify({
        from: 'GreenCube <onboarding@resend.dev>',
        to: [email],
        reply_to: inbox,
        subject: "You're on the list.",
        text:
          "Hey,\n\n" +
          "Thanks for joining the GreenCube early access list.\n\n" +
          "GreenCube is a personal AI that runs entirely on your computer. " +
          "It knows you, helps you, and your data never leaves your machine.\n\n" +
          "It's not ready yet, but it's getting close. " +
          "When it is, you'll be the first to hear from me.\n\n" +
          "Until then,\n" +
          "The GreenCube team\n\n" +
          "—\n" +
          "greencube.app\n",
      }),
    });
    if (!confirm.ok) {
      const err = await confirm.text().catch(() => '');
      console.error('[waitlist] confirmation send failed', confirm.status, err);
    }
  } catch (e) {
    console.error('[waitlist] confirmation send exception', String(e));
  }

  return res.status(200).json({ ok: true });
}
