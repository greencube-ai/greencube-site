// "Send the link to my PC": GreenCube is a Windows app, but many visitors arrive on a phone.
// Instead of losing them at "Not now", let them send greencube.app to themselves (WhatsApp,
// email, notes...) with the phone's own share menu. Nothing is collected: the phone sends it.
// Used by /buy (the phone step of the fit check) and the homepage (a phones-only line under the CTA).
(() => {
  // i18n:begin (generated: python i18n/i18n.py scripts, words in i18n/scripts.json)
  const TT = {"en":{"text":"GreenCube, the AI that runs on your own PC. Open this on your computer:","url":"https://greencube.app","copied":"Link copied. Paste it somewhere you'll see on your PC.","sent":"Done. Open it when you're at your PC.","line":"On your phone?","link":"Send it to your PC"},"es":{"text":"GreenCube, la IA que funciona en tu propio PC. Ábrelo en tu ordenador:","url":"https://greencube.app/es","copied":"Enlace copiado. Pégalo donde lo veas en tu PC.","sent":"Listo. Ábrelo cuando estés en tu PC.","line":"¿Estás en el móvil?","link":"Envíalo a tu PC"},"pt-br":{"text":"GreenCube, a IA que roda no seu próprio PC. Abra isto no seu computador:","url":"https://greencube.app/pt/","copied":"Link copiado. Cole em algum lugar que você veja no seu PC.","sent":"Pronto. Abra quando estiver no seu PC.","line":"Está no celular?","link":"Envie para o seu PC"},"fr":{"text":"GreenCube, l'IA qui tourne sur votre propre PC. Ouvrez ceci sur votre ordinateur :","url":"https://greencube.app/fr/","copied":"Lien copié. Collez-le là où vous le verrez sur votre PC.","sent":"C'est fait. Ouvrez-le quand vous serez sur votre PC.","line":"Sur votre téléphone ?","link":"Envoyez-le sur votre PC"},"de":{"text":"GreenCube, die KI, die auf deinem eigenen PC läuft. Öffne das auf deinem Computer:","url":"https://greencube.app/de/","copied":"Link kopiert. Füg ihn irgendwo ein, wo du ihn am PC siehst.","sent":"Erledigt. Öffne ihn, wenn du am PC bist.","line":"Am Handy?","link":"Schick es an deinen PC"},"it":{"text":"GreenCube, l'IA che funziona sul tuo PC. Aprilo sul tuo computer:","url":"https://greencube.app/it/","copied":"Link copiato. Incollalo dove lo vedrai sul tuo PC.","sent":"Fatto. Aprilo quando sei al PC.","line":"Sei sul telefono?","link":"Invialo al tuo PC"},"nl":{"text":"GreenCube, de AI die op je eigen pc draait. Open dit op je computer:","url":"https://greencube.app/nl/","copied":"Link gekopieerd. Plak hem ergens waar je hem op je pc ziet.","sent":"Klaar. Open hem als je achter je pc zit.","line":"Op je telefoon?","link":"Stuur het naar je pc"},"pl":{"text":"GreenCube, AI, które działa na twoim PC. Otwórz to na komputerze:","url":"https://greencube.app/pl/","copied":"Link skopiowany. Wklej go tam, gdzie zobaczysz go na PC.","sent":"Gotowe. Otwórz, gdy będziesz przy PC.","line":"Jesteś na telefonie?","link":"Wyślij na swój PC"},"tr":{"text":"GreenCube, kendi bilgisayarında çalışan yapay zekâ. Bunu bilgisayarında aç:","url":"https://greencube.app/tr/","copied":"Bağlantı kopyalandı. Bilgisayarında göreceğin bir yere yapıştır.","sent":"Tamam. Bilgisayarının başına geçince aç.","line":"Telefonda mısın?","link":"Bilgisayarına gönder"},"ru":{"text":"GreenCube — ИИ, который работает на вашем ПК. Откройте это на компьютере:","url":"https://greencube.app/ru/","copied":"Ссылка скопирована. Вставьте её туда, где увидите на ПК.","sent":"Готово. Откройте, когда будете за ПК.","line":"Вы с телефона?","link":"Отправить на ПК"},"uk":{"text":"GreenCube — ШІ, який працює на вашому ПК. Відкрийте це на комп'ютері:","url":"https://greencube.app/uk/","copied":"Посилання скопійовано. Вставте його туди, де побачите на ПК.","sent":"Готово. Відкрийте, коли будете за ПК.","line":"Ви з телефона?","link":"Надіслати на ПК"},"id":{"text":"GreenCube, AI yang berjalan di PC-mu sendiri. Buka ini di komputermu:","url":"https://greencube.app/id/","copied":"Link disalin. Tempel di tempat yang akan kamu lihat di PC.","sent":"Beres. Buka saat kamu di depan PC.","line":"Lagi pakai ponsel?","link":"Kirim ke PC-mu"},"vi":{"text":"GreenCube, AI chạy trên PC của bạn. Mở link này trên máy tính:","url":"https://greencube.app/vi/","copied":"Đã sao chép link. Dán vào chỗ bạn sẽ thấy trên PC.","sent":"Xong. Mở khi bạn ngồi vào PC.","line":"Đang dùng điện thoại?","link":"Gửi sang PC của bạn"},"th":{"text":"GreenCube AI ที่ทำงานบนพีซีของคุณเอง เปิดลิงก์นี้บนคอมพิวเตอร์:","url":"https://greencube.app/th/","copied":"คัดลอกลิงก์แล้ว วางไว้ที่ที่คุณจะเห็นบนพีซี","sent":"เรียบร้อย เปิดเมื่อคุณอยู่หน้าพีซี","line":"ใช้โทรศัพท์อยู่?","link":"ส่งไปที่พีซีของคุณ"},"ja":{"text":"GreenCube、自分のPCで動くAI。パソコンでこのリンクを開いてください：","url":"https://greencube.app/ja/","copied":"リンクをコピーしました。PCで見られる場所に貼り付けてください。","sent":"送りました。PCの前で開いてください。","line":"スマホで見ていますか？","link":"PCに送る"},"ko":{"text":"GreenCube, 내 PC에서 돌아가는 AI. 컴퓨터에서 이 링크를 여세요:","url":"https://greencube.app/ko/","copied":"링크를 복사했어요. PC에서 볼 수 있는 곳에 붙여 넣으세요.","sent":"보냈어요. PC 앞에서 열어 보세요.","line":"휴대폰으로 보고 계세요?","link":"PC로 보내기"},"zh-cn":{"text":"GreenCube，在你自己电脑上运行的 AI。在电脑上打开这个链接：","url":"https://greencube.app/zh/","copied":"链接已复制。贴到你在电脑上能看到的地方。","sent":"好了。到电脑前再打开。","line":"在用手机？","link":"发到你的电脑"},"zh-tw":{"text":"GreenCube，在你自己電腦上執行的 AI。在電腦上開啟這個連結：","url":"https://greencube.app/zh-tw/","copied":"連結已複製。貼到你在電腦上能看到的地方。","sent":"好了。到電腦前再開啟。","line":"在用手機？","link":"發到你的電腦"},"hi":{"text":"GreenCube, वह AI जो आपके अपने PC पर चलता है. इसे अपने कंप्यूटर पर खोलें:","url":"https://greencube.app/hi/","copied":"लिंक कॉपी हो गया. इसे वहाँ पेस्ट करें जहाँ PC पर दिखे.","sent":"हो गया. PC पर पहुँचकर खोलें.","line":"फ़ोन पर हैं?","link":"अपने PC पर भेजें"},"ar":{"text":"GreenCube، الذكاء الاصطناعي الذي يعمل على حاسوبك. افتح هذا على حاسوبك:","url":"https://greencube.app/ar/","copied":"تم نسخ الرابط. الصقه حيث ستراه على حاسوبك.","sent":"تم. افتحه حين تكون أمام حاسوبك.","line":"على الهاتف؟","link":"أرسله إلى حاسوبك"}};
  const L = (document.documentElement.lang || 'en').toLowerCase(); const S = TT[L] || TT[L.slice(0, 2)] || TT.en;
  const T = S;
  // i18n:end

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
