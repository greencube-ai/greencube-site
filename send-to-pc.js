// "Send the link to my PC": GreenCube is a Windows app, but many visitors arrive on a phone.
// Instead of losing them at "Not now", let them send greencube.app to themselves (WhatsApp,
// email, notes...) with the phone's own share menu. Nothing is collected: the phone sends it.
// Used by /buy (the phone step of the fit check) and the homepage (a phones-only line under the CTA).
(() => {
  const es = (document.documentElement.lang || '').toLowerCase().startsWith('es');
  const T = es
    ? {
        text: 'GreenCube, la IA que funciona en tu propio PC. Ábrelo en tu ordenador:',
        url: 'https://greencube.app/es',
        copied: 'Enlace copiado. Pégalo donde lo veas en tu PC.',
        sent: 'Listo. Ábrelo cuando estés en tu PC.',
        line: '¿Estás en el móvil?',
        link: 'Envíalo a tu PC',
      }
    : {
        text: 'GreenCube, the AI that runs on your own PC. Open this on your computer:',
        url: 'https://greencube.app',
        copied: "Link copied. Paste it somewhere you'll see on your PC.",
        sent: "Done. Open it when you're at your PC.",
        line: 'On your phone?',
        link: 'Send it to your PC',
      };

  const isPhone = () => {
    const ua = navigator.userAgentData;
    const h = (((ua && ua.platform) || '') + ' ' + (navigator.platform || '') + ' ' + (navigator.userAgent || '')).toLowerCase();
    const touch = (navigator.maxTouchPoints || 0) > 1;
    return !!((ua && ua.mobile) || /iphone|ipod|android|mobile|ipad/.test(h) || (/mac/.test(h) && touch));
  };

  const toast = (msg) => {
    let t = document.getElementById('stp-toast');
    if (!t) {
      t = document.createElement('div');
      t.id = 'stp-toast';
      t.setAttribute('role', 'status');
      document.body.appendChild(t);
    }
    t.textContent = msg;
    t.classList.add('on');
    clearTimeout(t._h);
    t._h = setTimeout(() => t.classList.remove('on'), 3200);
  };

  // returns true when the link was handed off (shared or copied)
  const sendToPC = async () => {
    if (navigator.share) {
      try {
        await navigator.share({title: 'GreenCube', text: T.text, url: T.url});
        toast(T.sent);
        return true;
      } catch (e) {
        if (e && e.name === 'AbortError') return false; // they closed the share menu
      }
    }
    try {
      await navigator.clipboard.writeText(T.text + ' ' + T.url);
      toast(T.copied);
      return true;
    } catch (e) {
      prompt(T.copied, T.url);
      return true;
    }
  };
  window.gcSendToPC = sendToPC;
  window.gcIsPhone = isPhone;

  const style = document.createElement('style');
  style.textContent = `
    #stp-toast { position: fixed; left: 50%; bottom: 24px; transform: translate(-50%, 20px); opacity: 0; pointer-events: none;
      max-width: calc(100vw - 32px); padding: 12px 18px; border-radius: 14px; background: #1F2418; color: #fff;
      font-size: 14.5px; line-height: 1.4; text-align: center; z-index: 9999; transition: opacity .25s, transform .25s; }
    #stp-toast.on { opacity: 1; transform: translate(-50%, 0); }
    .send-pc { margin: 14px 0 0; text-align: center; font-size: 15px; color: var(--ink-soft, #545454); }
    .send-pc button { background: none; border: none; padding: 4px 2px; font: inherit; color: var(--forest, #1A1A1A);
      font-weight: 600; text-decoration: underline; text-underline-offset: 3px; cursor: pointer; }
  `;
  document.head.appendChild(style);

  // homepage: a phones-only line right under the main buttons
  const row = document.querySelector('.hero .cta-row');
  if (row && isPhone()) {
    const p = document.createElement('p');
    p.className = 'send-pc';
    const b = document.createElement('button');
    b.type = 'button';
    b.textContent = T.link + ' →';
    b.addEventListener('click', sendToPC);
    p.append(T.line + ' ', b);
    row.insertAdjacentElement('afterend', p);
  }
})();
