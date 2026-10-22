// The two-question tier check, as it runs on the home page (every language in TT below).
// Same cards, same rule and same reveal as what-you-get.html; the words follow
// <html lang>. The tier rule mirrors perf_tier_from in the app (docs/TIERS.md).
(() => {
  const game = document.getElementById('game');
  if (!game) return;
  // i18n:begin (generated: python i18n/i18n.py scripts, words in i18n/scripts.json)
  const TT = {"en":{"about":"about {v} GB","builtIn":"built in","miss":"Not on our list. How much memory does it have?","noIdea":"No idea","guessedRam":"RAM we had to guess at","ram":"{n} GB of RAM","withMem":"<b>{card}</b>{extra}, with <b>{mem}</b>.","sized":", about {v} GB","none":"<b>No separate graphics card</b>, with <b>{mem}</b>.","guessed":"We assumed <b>no graphics card</b>, with <b>{mem}</b>. If you do have one, it is better than this.","builtInSpec":"<b>Built-in graphics</b>, with <b>{mem}</b>.","mac":"That is what a Mac of yours would be. GreenCube is Windows only today, and the Mac version is on the way.","feels":{"seed":"Slow, but it gets there.","sprout":"Works well. Not fast.","bloom":"You stop noticing the wait.","thrive":"Your computer is the only limit."}},"es":{"about":"unos {v} GB","builtIn":"integrada","miss":"No está en nuestra lista. ¿Cuánta memoria tiene?","noIdea":"Ni idea","guessedRam":"RAM que tuvimos que adivinar","ram":"{n} GB de RAM","withMem":"<b>{card}</b>{extra}, con <b>{mem}</b>.","sized":", unos {v} GB","none":"<b>Sin tarjeta gráfica aparte</b>, con <b>{mem}</b>.","guessed":"Supusimos <b>sin tarjeta gráfica</b>, con <b>{mem}</b>. Si tienes una, irá mejor que esto.","builtInSpec":"<b>Gráficos integrados</b>, con <b>{mem}</b>.","mac":"Eso es lo que sería tu Mac. Hoy GreenCube es solo para Windows; la versión para Mac está en camino.","feels":{"seed":"Lenta, pero llega.","sprout":"Va bien. No es rápida.","bloom":"Dejas de notar la espera.","thrive":"El único límite es tu ordenador."}},"pt-br":{"about":"cerca de {v} GB","builtIn":"integrada","miss":"Não está na nossa lista. Quanta memória ela tem?","noIdea":"Não faço ideia","guessedRam":"RAM que tivemos que adivinhar","ram":"{n} GB de RAM","withMem":"<b>{card}</b>{extra}, com <b>{mem}</b>.","sized":", cerca de {v} GB","none":"<b>Sem placa de vídeo separada</b>, com <b>{mem}</b>.","guessed":"Supomos <b>sem placa de vídeo</b>, com <b>{mem}</b>. Se você tiver uma, vai ser melhor do que isso.","builtInSpec":"<b>Gráficos integrados</b>, com <b>{mem}</b>.","mac":"É isso que o seu Mac seria. Hoje o GreenCube é só para Windows; a versão para Mac está a caminho.","feels":{"seed":"Lenta, mas chega lá.","sprout":"Funciona bem. Não é rápida.","bloom":"Você para de notar a espera.","thrive":"O único limite é o seu computador."}},"fr":{"about":"environ {v} Go","builtIn":"intégrée","miss":"Pas dans notre liste. Combien de mémoire a-t-elle ?","noIdea":"Aucune idée","guessedRam":"RAM que nous avons dû deviner","ram":"{n} Go de RAM","withMem":"<b>{card}</b>{extra}, avec <b>{mem}</b>.","sized":", environ {v} Go","none":"<b>Pas de carte graphique séparée</b>, avec <b>{mem}</b>.","guessed":"Nous avons supposé <b>sans carte graphique</b>, avec <b>{mem}</b>. Si vous en avez une, ce sera mieux que ça.","builtInSpec":"<b>Graphismes intégrés</b>, avec <b>{mem}</b>.","mac":"Voilà ce que serait votre Mac. GreenCube n'existe que sur Windows aujourd'hui ; la version Mac arrive.","feels":{"seed":"Lente, mais elle y arrive.","sprout":"Ça marche bien. Pas rapide.","bloom":"Vous ne remarquez plus l'attente.","thrive":"Votre ordinateur est la seule limite."}},"de":{"about":"etwa {v} GB","builtIn":"integriert","miss":"Nicht in unserer Liste. Wie viel Speicher hat sie?","noIdea":"Keine Ahnung","guessedRam":"RAM, den wir schätzen mussten","ram":"{n} GB RAM","withMem":"<b>{card}</b>{extra}, mit <b>{mem}</b>.","sized":", etwa {v} GB","none":"<b>Keine eigene Grafikkarte</b>, mit <b>{mem}</b>.","guessed":"Wir sind von <b>keiner Grafikkarte</b> ausgegangen, mit <b>{mem}</b>. Wenn du eine hast, wird es besser als das.","builtInSpec":"<b>Integrierte Grafik</b>, mit <b>{mem}</b>.","mac":"So wäre dein Mac. GreenCube gibt es heute nur für Windows; die Mac-Version ist unterwegs.","feels":{"seed":"Langsam, aber sie kommt an.","sprout":"Läuft gut. Nicht schnell.","bloom":"Du merkst das Warten nicht mehr.","thrive":"Dein Computer ist die einzige Grenze."}},"it":{"about":"circa {v} GB","builtIn":"integrata","miss":"Non è nella nostra lista. Quanta memoria ha?","noIdea":"Non ne ho idea","guessedRam":"RAM che abbiamo dovuto indovinare","ram":"{n} GB di RAM","withMem":"<b>{card}</b>{extra}, con <b>{mem}</b>.","sized":", circa {v} GB","none":"<b>Nessuna scheda grafica separata</b>, con <b>{mem}</b>.","guessed":"Abbiamo supposto <b>nessuna scheda grafica</b>, con <b>{mem}</b>. Se ne hai una, andrà meglio di così.","builtInSpec":"<b>Grafica integrata</b>, con <b>{mem}</b>.","mac":"Ecco cosa sarebbe il tuo Mac. Oggi GreenCube è solo per Windows; la versione per Mac è in arrivo.","feels":{"seed":"Lenta, ma ci arriva.","sprout":"Funziona bene. Non è veloce.","bloom":"Smetti di notare l'attesa.","thrive":"L'unico limite è il tuo computer."}},"nl":{"about":"ongeveer {v} GB","builtIn":"ingebouwd","miss":"Niet in onze lijst. Hoeveel geheugen heeft hij?","noIdea":"Geen idee","guessedRam":"RAM die we moesten gokken","ram":"{n} GB RAM","withMem":"<b>{card}</b>{extra}, met <b>{mem}</b>.","sized":", ongeveer {v} GB","none":"<b>Geen aparte videokaart</b>, met <b>{mem}</b>.","guessed":"We gingen uit van <b>geen videokaart</b>, met <b>{mem}</b>. Als je er wel een hebt, is het beter dan dit.","builtInSpec":"<b>Ingebouwde graphics</b>, met <b>{mem}</b>.","mac":"Zo zou je Mac uitkomen. GreenCube is nu alleen voor Windows; de Mac-versie komt eraan.","feels":{"seed":"Traag, maar hij komt er wel.","sprout":"Werkt goed. Niet snel.","bloom":"Je merkt het wachten niet meer.","thrive":"Je computer is de enige grens."}},"pl":{"about":"około {v} GB","builtIn":"zintegrowana","miss":"Nie ma jej na naszej liście. Ile ma pamięci?","noIdea":"Nie mam pojęcia","guessedRam":"RAM, który musieliśmy zgadnąć","ram":"{n} GB RAM","withMem":"<b>{card}</b>{extra}, z <b>{mem}</b>.","sized":", około {v} GB","none":"<b>Bez osobnej karty graficznej</b>, z <b>{mem}</b>.","guessed":"Założyliśmy <b>brak karty graficznej</b>, z <b>{mem}</b>. Jeśli ją masz, będzie lepiej niż to.","builtInSpec":"<b>Zintegrowana grafika</b>, z <b>{mem}</b>.","mac":"Tak wyszedłby twój Mac. Dziś GreenCube jest tylko na Windows; wersja na Maca jest w drodze.","feels":{"seed":"Wolno, ale dociera.","sprout":"Działa dobrze. Nie szybko.","bloom":"Przestajesz zauważać czekanie.","thrive":"Jedynym limitem jest twój komputer."}},"tr":{"about":"yaklaşık {v} GB","builtIn":"dahili","miss":"Listemizde yok. Ne kadar belleği var?","noIdea":"Hiç bilmiyorum","guessedRam":"Tahmin etmek zorunda kaldığımız RAM","ram":"{n} GB RAM","withMem":"<b>{card}</b>{extra}, <b>{mem}</b> ile.","sized":", yaklaşık {v} GB","none":"<b>Ayrı ekran kartı yok</b>, <b>{mem}</b> ile.","guessed":"<b>Ekran kartı olmadığını</b> varsaydık, <b>{mem}</b> ile. Kartın varsa bundan daha iyi olur.","builtInSpec":"<b>Dahili grafik</b>, <b>{mem}</b> ile.","mac":"Mac'in böyle olurdu. GreenCube bugün yalnızca Windows için; Mac sürümü yolda.","feels":{"seed":"Yavaş ama varıyor.","sprout":"İyi çalışıyor. Hızlı değil.","bloom":"Beklemeyi fark etmiyorsun.","thrive":"Tek sınır bilgisayarın."}},"ru":{"about":"около {v} ГБ","builtIn":"встроенная","miss":"Её нет в нашем списке. Сколько у неё памяти?","noIdea":"Без понятия","guessedRam":"ОЗУ, которую пришлось угадать","ram":"{n} ГБ ОЗУ","withMem":"<b>{card}</b>{extra}, с <b>{mem}</b>.","sized":", около {v} ГБ","none":"<b>Нет отдельной видеокарты</b>, с <b>{mem}</b>.","guessed":"Мы предположили, что <b>видеокарты нет</b>, с <b>{mem}</b>. Если она есть, будет лучше.","builtInSpec":"<b>Встроенная графика</b>, с <b>{mem}</b>.","mac":"Так получился бы ваш Mac. Сейчас GreenCube только для Windows; версия для Mac в пути.","feels":{"seed":"Медленно, но доходит.","sprout":"Работает хорошо. Не быстро.","bloom":"Ожидание перестаёт замечаться.","thrive":"Предел — только ваш компьютер."}},"uk":{"about":"близько {v} ГБ","builtIn":"вбудована","miss":"Її немає в нашому списку. Скільки в неї пам'яті?","noIdea":"Без поняття","guessedRam":"ОЗП, яку довелося вгадати","ram":"{n} ГБ ОЗП","withMem":"<b>{card}</b>{extra}, з <b>{mem}</b>.","sized":", близько {v} ГБ","none":"<b>Немає окремої відеокарти</b>, з <b>{mem}</b>.","guessed":"Ми припустили, що <b>відеокарти немає</b>, з <b>{mem}</b>. Якщо вона є, буде краще.","builtInSpec":"<b>Вбудована графіка</b>, з <b>{mem}</b>.","mac":"Таким вийшов би ваш Mac. Зараз GreenCube лише для Windows; версія для Mac уже в дорозі.","feels":{"seed":"Повільно, але доходить.","sprout":"Працює добре. Не швидко.","bloom":"Очікування перестаєш помічати.","thrive":"Межа — лише ваш комп'ютер."}},"id":{"about":"sekitar {v} GB","builtIn":"bawaan","miss":"Tidak ada di daftar kami. Berapa memorinya?","noIdea":"Tidak tahu","guessedRam":"RAM yang terpaksa kami tebak","ram":"RAM {n} GB","withMem":"<b>{card}</b>{extra}, dengan <b>{mem}</b>.","sized":", sekitar {v} GB","none":"<b>Tanpa kartu grafis terpisah</b>, dengan <b>{mem}</b>.","guessed":"Kami anggap <b>tanpa kartu grafis</b>, dengan <b>{mem}</b>. Kalau kamu punya, hasilnya lebih baik dari ini.","builtInSpec":"<b>Grafis bawaan</b>, dengan <b>{mem}</b>.","mac":"Begitulah Mac-mu. GreenCube saat ini hanya untuk Windows; versi Mac sedang dibuat.","feels":{"seed":"Lambat, tapi sampai.","sprout":"Lancar. Tidak cepat.","bloom":"Kamu tidak lagi merasa menunggu.","thrive":"Batasnya hanya komputermu."}},"vi":{"about":"khoảng {v} GB","builtIn":"tích hợp","miss":"Không có trong danh sách. Nó có bao nhiêu bộ nhớ?","noIdea":"Không biết","guessedRam":"RAM chúng tôi phải đoán","ram":"RAM {n} GB","withMem":"<b>{card}</b>{extra}, với <b>{mem}</b>.","sized":", khoảng {v} GB","none":"<b>Không có card đồ họa rời</b>, với <b>{mem}</b>.","guessed":"Chúng tôi giả định <b>không có card đồ họa</b>, với <b>{mem}</b>. Nếu bạn có, sẽ tốt hơn thế này.","builtInSpec":"<b>Đồ họa tích hợp</b>, với <b>{mem}</b>.","mac":"Đó là máy Mac của bạn. Hiện GreenCube chỉ có cho Windows; bản Mac đang được làm.","feels":{"seed":"Chậm, nhưng vẫn tới.","sprout":"Chạy tốt. Không nhanh.","bloom":"Bạn không còn thấy phải chờ.","thrive":"Giới hạn duy nhất là máy của bạn."}},"th":{"about":"ราว {v} GB","builtIn":"ออนบอร์ด","miss":"ไม่อยู่ในรายการของเรา มีหน่วยความจำเท่าไร?","noIdea":"ไม่รู้เลย","guessedRam":"RAM ที่เราต้องเดา","ram":"RAM {n} GB","withMem":"<b>{card}</b>{extra} พร้อม <b>{mem}</b>","sized":" ราว {v} GB","none":"<b>ไม่มีการ์ดจอแยก</b> พร้อม <b>{mem}</b>","guessed":"เราสันนิษฐานว่า<b>ไม่มีการ์ดจอ</b> พร้อม <b>{mem}</b> ถ้าคุณมี จะดีกว่านี้","builtInSpec":"<b>กราฟิกออนบอร์ด</b> พร้อม <b>{mem}</b>","mac":"Mac ของคุณจะเป็นแบบนี้ ตอนนี้ GreenCube มีแค่บน Windows เวอร์ชัน Mac กำลังมา","feels":{"seed":"ช้า แต่ก็ถึง","sprout":"ใช้ได้ดี ไม่เร็ว","bloom":"แทบไม่รู้สึกว่าต้องรอ","thrive":"ขีดจำกัดเดียวคือคอมพิวเตอร์ของคุณ"}},"ja":{"about":"約{v} GB","builtIn":"内蔵","miss":"リストにありません。メモリはどれくらい？","noIdea":"わからない","guessedRam":"推測したRAM","ram":"RAM {n} GB","withMem":"<b>{card}</b>{extra}、<b>{mem}</b>。","sized":"、約{v} GB","none":"<b>独立したグラフィックカードなし</b>、<b>{mem}</b>。","guessed":"<b>グラフィックカードなし</b>と仮定しました（<b>{mem}</b>）。お持ちなら、これより良くなります。","builtInSpec":"<b>内蔵グラフィックス</b>、<b>{mem}</b>。","mac":"Macならこうなります。GreenCubeは現在Windows専用で、Mac版は準備中です。","feels":{"seed":"遅いけれど、ちゃんと届く。","sprout":"快適。速くはない。","bloom":"待ち時間が気にならなくなる。","thrive":"限界はあなたのパソコンだけ。"}},"ko":{"about":"약 {v} GB","builtIn":"내장","miss":"목록에 없어요. 메모리가 얼마나 되나요?","noIdea":"모르겠어요","guessedRam":"추정한 RAM","ram":"RAM {n} GB","withMem":"<b>{card}</b>{extra}, <b>{mem}</b>.","sized":", 약 {v} GB","none":"<b>별도 그래픽카드 없음</b>, <b>{mem}</b>.","guessed":"<b>그래픽카드가 없다고</b> 가정했어요, <b>{mem}</b>. 있다면 이보다 좋아요.","builtInSpec":"<b>내장 그래픽</b>, <b>{mem}</b>.","mac":"Mac이라면 이렇습니다. GreenCube는 현재 Windows 전용이고, Mac 버전은 준비 중이에요.","feels":{"seed":"느리지만 결국 해냅니다.","sprout":"잘 돌아가요. 빠르진 않아요.","bloom":"기다림이 느껴지지 않아요.","thrive":"한계는 내 컴퓨터뿐."}},"zh-cn":{"about":"约 {v} GB","builtIn":"集成","miss":"不在我们的列表里。它有多少显存？","noIdea":"不知道","guessedRam":"我们只能猜的内存","ram":"{n} GB 内存","withMem":"<b>{card}</b>{extra}，配 <b>{mem}</b>。","sized":"，约 {v} GB","none":"<b>没有独立显卡</b>，配 <b>{mem}</b>。","guessed":"我们按<b>没有显卡</b>来估算，配 <b>{mem}</b>。如果你有显卡，会比这更好。","builtInSpec":"<b>集成显卡</b>，配 <b>{mem}</b>。","mac":"这就是你的 Mac 的情况。GreenCube 目前只支持 Windows，Mac 版正在开发中。","feels":{"seed":"慢，但能跑完。","sprout":"挺好用，不算快。","bloom":"你不再觉得在等。","thrive":"唯一的限制是你的电脑。"}},"zh-tw":{"about":"約 {v} GB","builtIn":"整合","miss":"不在我們的列表裡。它有多少視訊記憶體？","noIdea":"不知道","guessedRam":"我們只能猜的記憶體","ram":"{n} GB 記憶體","withMem":"<b>{card}</b>{extra}，配 <b>{mem}</b>。","sized":"，約 {v} GB","none":"<b>沒有獨立顯示卡</b>，配 <b>{mem}</b>。","guessed":"我們按<b>沒有顯示卡</b>來估算，配 <b>{mem}</b>。如果你有顯示卡，會比這更好。","builtInSpec":"<b>整合顯示卡</b>，配 <b>{mem}</b>。","mac":"這就是你的 Mac 的情況。GreenCube 目前只支援 Windows，Mac 版正在開發中。","feels":{"seed":"慢，但能跑完。","sprout":"挺好用，不算快。","bloom":"你不再覺得在等。","thrive":"唯一的限制是你的電腦。"}},"hi":{"about":"लगभग {v} GB","builtIn":"बिल्ट-इन","miss":"हमारी लिस्ट में नहीं है. इसमें कितनी मेमोरी है?","noIdea":"पता नहीं","guessedRam":"RAM जिसका हमें अंदाज़ा लगाना पड़ा","ram":"{n} GB RAM","withMem":"<b>{card}</b>{extra}, <b>{mem}</b> के साथ.","sized":", लगभग {v} GB","none":"<b>कोई अलग ग्राफ़िक्स कार्ड नहीं</b>, <b>{mem}</b> के साथ.","guessed":"हमने मान लिया <b>कोई ग्राफ़िक्स कार्ड नहीं</b>, <b>{mem}</b> के साथ. अगर आपके पास है, तो इससे बेहतर होगा.","builtInSpec":"<b>बिल्ट-इन ग्राफ़िक्स</b>, <b>{mem}</b> के साथ.","mac":"आपका Mac ऐसा होता. GreenCube अभी सिर्फ़ Windows के लिए है; Mac वर्ज़न आ रहा है.","feels":{"seed":"धीमा, पर पहुँच जाता है.","sprout":"अच्छा चलता है. तेज़ नहीं.","bloom":"इंतज़ार महसूस होना बंद.","thrive":"सीमा सिर्फ़ आपका कंप्यूटर है."}},"ar":{"about":"نحو {v} GB","builtIn":"مدمجة","miss":"ليست في قائمتنا. كم فيها من الذاكرة؟","noIdea":"لا أعرف","guessedRam":"ذاكرة RAM اضطررنا لتخمينها","ram":"{n} GB RAM","withMem":"<b>{card}</b>{extra}، مع <b>{mem}</b>.","sized":"، نحو {v} GB","none":"<b>بلا بطاقة رسومات منفصلة</b>، مع <b>{mem}</b>.","guessed":"افترضنا <b>عدم وجود بطاقة رسومات</b>، مع <b>{mem}</b>. إن كانت لديك فالنتيجة أفضل.","builtInSpec":"<b>رسومات مدمجة</b>، مع <b>{mem}</b>.","mac":"هكذا سيكون جهاز Mac لديك. GreenCube متاح اليوم لنظام Windows فقط، ونسخة Mac قادمة.","feels":{"seed":"بطيء، لكنه يصل.","sprout":"يعمل جيدًا. ليس سريعًا.","bloom":"لن تشعر بالانتظار.","thrive":"الحد الوحيد هو حاسوبك."}}};
  const L = (document.documentElement.lang || 'en').toLowerCase(); const S = TT[L] || TT[L.slice(0, 2)] || TT.en;
  const f = (t, o) => t.replace(/\{(\w+)\}/g, (_, k) => o[k]);
  const T = { about: (v) => f(S.about, { v }), builtIn: S.builtIn, miss: S.miss, noIdea: S.noIdea,
    guessedRam: S.guessedRam, ram: (n) => f(S.ram, { n }),
    withMem: (card, extra, mem) => f(S.withMem, { card, extra, mem }), sized: (v) => f(S.sized, { v }),
    none: (mem) => f(S.none, { mem }), guessed: (mem) => f(S.guessed, { mem }),
    builtInSpec: (mem) => f(S.builtInSpec, { mem }), mac: S.mac, feels: S.feels };
  // i18n:end

  // Graphics cards with their memory. Coarse buckets are all the tier needs
  // (under 4 GB, 4 to 7, 8 and up); anything missing can be entered by size.
  const CARDS = [
    ['GeForce GT 1030', 2], ['GeForce GTX 750 Ti', 2], ['GeForce GTX 950', 2],
    ['GeForce GTX 960', 2], ['GeForce GTX 970', 4], ['GeForce GTX 980', 4],
    ['GeForce GTX 980 Ti', 6], ['GeForce GTX 1050', 2], ['GeForce GTX 1050 Ti', 4],
    ['GeForce GTX 1060', 6], ['GeForce GTX 1070', 8], ['GeForce GTX 1070 Ti', 8],
    ['GeForce GTX 1080', 8], ['GeForce GTX 1080 Ti', 11],
    ['GeForce GTX 1630', 4], ['GeForce GTX 1650', 4], ['GeForce GTX 1650 Super', 4],
    ['GeForce GTX 1660', 6], ['GeForce GTX 1660 Super', 6], ['GeForce GTX 1660 Ti', 6],
    ['Titan Xp', 12], ['Titan V', 12], ['Titan RTX', 24],
    ['GeForce RTX 2050', 4], ['GeForce RTX 2060', 6], ['GeForce RTX 2060 Super', 8],
    ['GeForce RTX 2070', 8], ['GeForce RTX 2070 Super', 8], ['GeForce RTX 2080', 8],
    ['GeForce RTX 2080 Super', 8], ['GeForce RTX 2080 Ti', 11],
    ['GeForce RTX 2060 Laptop', 6], ['GeForce RTX 2070 Laptop', 8], ['GeForce RTX 2080 Laptop', 8],
    ['GeForce RTX 3050', 8], ['GeForce RTX 3050 Laptop', 4], ['GeForce RTX 3050 Ti Laptop', 4],
    ['GeForce RTX 3060', 12], ['GeForce RTX 3060 Laptop', 6], ['GeForce RTX 3060 Ti', 8],
    ['GeForce RTX 3070', 8], ['GeForce RTX 3070 Laptop', 8], ['GeForce RTX 3070 Ti', 8],
    ['GeForce RTX 3080', 10], ['GeForce RTX 3080 Laptop', 8], ['GeForce RTX 3080 Ti', 12],
    ['GeForce RTX 3080 Ti Laptop', 16], ['GeForce RTX 3090', 24], ['GeForce RTX 3090 Ti', 24],
    ['GeForce RTX 4050 Laptop', 6], ['GeForce RTX 4060', 8], ['GeForce RTX 4060 Laptop', 8],
    ['GeForce RTX 4060 Ti', 8], ['GeForce RTX 4070', 12], ['GeForce RTX 4070 Laptop', 8],
    ['GeForce RTX 4070 Super', 12], ['GeForce RTX 4070 Ti', 12], ['GeForce RTX 4070 Ti Super', 16],
    ['GeForce RTX 4080', 16], ['GeForce RTX 4080 Laptop', 12], ['GeForce RTX 4080 Super', 16],
    ['GeForce RTX 4090', 24], ['GeForce RTX 4090 Laptop', 16],
    ['GeForce RTX 5050', 8], ['GeForce RTX 5060', 8], ['GeForce RTX 5060 Ti', 16],
    ['GeForce RTX 5070', 12], ['GeForce RTX 5070 Ti', 16], ['GeForce RTX 5080', 16],
    ['GeForce RTX 5090', 32],
    ['Quadro P1000', 4], ['Quadro P2000', 5], ['Quadro RTX 4000', 8], ['Quadro RTX 5000', 16],
    ['NVIDIA T600', 4], ['NVIDIA T1000', 8], ['NVIDIA RTX A2000', 12], ['NVIDIA RTX A4000', 16],
    ['NVIDIA RTX A5000', 24], ['NVIDIA RTX A6000', 48], ['NVIDIA RTX 4000 Ada', 20],
    ['NVIDIA RTX 5000 Ada', 32], ['NVIDIA RTX 6000 Ada', 48],
    ['Radeon R9 380', 4], ['Radeon R9 390', 8], ['Radeon RX 550', 4], ['Radeon RX 560', 4],
    ['Radeon RX 570', 8], ['Radeon RX 580', 8], ['Radeon RX 590', 8],
    ['Radeon RX Vega 56', 8], ['Radeon RX Vega 64', 8], ['Radeon VII', 16],
    ['Radeon RX 5500 XT', 8], ['Radeon RX 5600 XT', 6], ['Radeon RX 5700', 8], ['Radeon RX 5700 XT', 8],
    ['Radeon RX 6400', 4], ['Radeon RX 6500 XT', 4], ['Radeon RX 6600', 8], ['Radeon RX 6600 XT', 8],
    ['Radeon RX 6650 XT', 8], ['Radeon RX 6700', 10], ['Radeon RX 6700 XT', 12],
    ['Radeon RX 6750 XT', 12], ['Radeon RX 6800', 16], ['Radeon RX 6800 XT', 16],
    ['Radeon RX 6900 XT', 16], ['Radeon RX 6950 XT', 16],
    ['Radeon RX 7600', 8], ['Radeon RX 7600 XT', 16], ['Radeon RX 7700 XT', 12],
    ['Radeon RX 7800 XT', 16], ['Radeon RX 7900 GRE', 16], ['Radeon RX 7900 XT', 20],
    ['Radeon RX 7900 XTX', 24],
    ['Radeon RX 9060 XT', 8], ['Radeon RX 9070', 16], ['Radeon RX 9070 XT', 16],
    ['Radeon RX 6600M', 8], ['Radeon RX 6700M', 10], ['Radeon RX 6800M', 12],
    ['Radeon RX 7600M XT', 8], ['Radeon RX 7700S', 8],
    ['Intel Arc A310', 4], ['Intel Arc A380', 6], ['Intel Arc A550M', 8], ['Intel Arc A580', 8],
    ['Intel Arc A750', 8], ['Intel Arc A770', 16], ['Intel Arc B570', 10], ['Intel Arc B580', 12],
    ['Intel HD Graphics (built in)', 0], ['Intel UHD Graphics (built in)', 0],
    ['Intel Iris Plus (built in)', 0], ['Intel Iris Xe (built in)', 0],
    ['Intel Arc Graphics, laptop chip (built in)', 0],
    ['AMD Radeon Vega, in a Ryzen chip (built in)', 0],
    ['AMD Radeon 660M / 680M (built in)', 0], ['AMD Radeon 760M / 780M (built in)', 0],
    ['AMD Radeon 860M / 890M (built in)', 0],
    // Apple silicon is tiered on total RAM only (-1 marks it): a Mac reports 75%
    // of its memory as graphics memory, which would call an 8 GB MacBook fast.
    ['Apple M1', -1], ['Apple M1 Pro', -1], ['Apple M1 Max', -1], ['Apple M1 Ultra', -1],
    ['Apple M2', -1], ['Apple M2 Pro', -1], ['Apple M2 Max', -1], ['Apple M2 Ultra', -1],
    ['Apple M3', -1], ['Apple M3 Pro', -1], ['Apple M3 Max', -1], ['Apple M3 Ultra', -1],
    ['Apple M4', -1], ['Apple M4 Pro', -1], ['Apple M4 Max', -1],
    ['Apple silicon, M5 or newer', -1]
  ].map(([name, vram]) => ({ name, vram, key: name.toLowerCase() }));

  const TIERS = {
    seed:   { name: 'Seed',   mk: '#FAE289' },
    sprout: { name: 'Sprout', mk: '#8EA674' },
    bloom:  { name: 'Bloom',  mk: '#FA9F75' },
    thrive: { name: 'Thrive', mk: '#8EABE1' }
  };

  const $ = (id) => document.getElementById(id);
  const steps = { ram: $('s-ram'), gpu: $('s-gpu'), rev: $('s-rev') };
  const state = { ram: null, card: null, vram: 0, guessed: false };

  function show(key) {
    Object.values(steps).forEach((s) => s.classList.remove('on'));
    steps[key].classList.add('on');
  }

  function ramGb() {
    if (state.ram === '8') return 8;
    if (state.ram === '16') return 16;
    if (state.ram === '32') return 32;
    // "No idea": the browser only glimpses this, so it never lands on the top tier.
    const dm = navigator.deviceMemory || 0;
    const cores = navigator.hardwareConcurrency || 0;
    return (dm >= 8 || cores >= 8) ? 16 : 8;
  }

  function tierFor(gb, vram) {
    if (vram === -1) {
      if (gb >= 24) return 'thrive';
      if (gb >= 12) return 'bloom';
      return 'seed';
    }
    if (vram >= 8 && gb >= 24) return 'thrive';
    if (vram >= 8 && gb >= 8) return 'bloom';
    if (vram >= 4 && gb >= 16) return 'bloom';
    if (gb >= 12 || (vram >= 4 && gb >= 8)) return 'sprout';
    return 'seed';
  }

  const input = $('gpu-in');
  const hits = $('hits');
  let cursor = -1, shown = [];

  function search(q) {
    const words = q.toLowerCase().split(/\s+/).filter(Boolean);
    if (!words.length) return [];
    return CARDS.filter((c) => words.every((w) => c.key.includes(w))).slice(0, 7);
  }

  function paint() {
    if (shown.length) {
      hits.innerHTML = shown.map((c, i) =>
        '<button class="hit' + (i === cursor ? ' cursor' : '') + '" type="button" data-i="' + i + '">' +
        '<span class="h-n">' + c.name + '</span>' +
        '<span class="h-v">' + (c.vram > 0 ? T.about(c.vram) : c.vram === 0 ? T.builtIn : '') + '</span>' +
        '</button>').join('');
    } else if (input.value.trim().length >= 2) {
      hits.innerHTML = '<div class="miss"><b>' + T.miss + '</b><div class="sizes">' +
        [2, 4, 6, 8, 12, 16, 24].map((v) => '<button type="button" data-v="' + v + '">' + v + ' GB</button>').join('') +
        '<button type="button" data-v="0">' + T.noIdea + '</button></div></div>';
    } else {
      hits.innerHTML = '';
    }
    input.setAttribute('aria-expanded', String(hits.innerHTML !== ''));
  }

  function escapeHtml(s) { return s.replace(/[&<>"']/g, (c) => '&#' + c.charCodeAt(0) + ';'); }

  function choose(c) { state.card = c.name; state.vram = c.vram; state.guessed = false; reveal(); }

  input.addEventListener('input', () => { shown = search(input.value); cursor = shown.length ? 0 : -1; paint(); });
  input.addEventListener('keydown', (e) => {
    if (!shown.length) return;
    if (e.key === 'ArrowDown') { e.preventDefault(); cursor = (cursor + 1) % shown.length; paint(); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); cursor = (cursor - 1 + shown.length) % shown.length; paint(); }
    else if (e.key === 'Enter') { e.preventDefault(); if (shown[cursor]) choose(shown[cursor]); }
  });
  hits.addEventListener('click', (e) => {
    const hit = e.target.closest('.hit');
    if (hit) { choose(shown[+hit.getAttribute('data-i')]); return; }
    const size = e.target.closest('[data-v]');
    if (size) {
      const v = +size.getAttribute('data-v');
      state.card = escapeHtml(input.value.trim());
      state.vram = v;
      state.guessed = v === 0;
      reveal();
    }
  });

  $('gpu-none').addEventListener('click', () => { state.card = 'none'; state.vram = 0; state.guessed = false; reveal(); });
  $('gpu-dunno').addEventListener('click', () => { state.card = null; state.vram = 0; state.guessed = true; reveal(); });

  function reveal() {
    const gb = ramGb();
    const key = tierFor(gb, state.vram);
    const t = TIERS[key];

    game.style.setProperty('--mk', t.mk);
    game.classList.add('lit');
    $('r-name').textContent = t.name;
    $('r-feels').textContent = T.feels[key];

    const mem = state.ram === 'unsure' ? T.guessedRam : T.ram(state.ram);
    let spec;
    if (state.vram === -1) spec = T.withMem(state.card, '', mem);
    else if (state.vram > 0) spec = T.withMem(state.card, T.sized(state.vram), mem);
    else if (state.card === 'none') spec = T.none(mem);
    else if (state.guessed) spec = T.guessed(mem);
    else spec = T.builtInSpec(mem);
    $('r-spec').innerHTML = spec;

    const note = $('r-note');
    note.textContent = T.mac;
    note.hidden = state.vram !== -1;

    // light up the matching tier card just below
    document.querySelectorAll('.tier-card, .flat-tier').forEach((c) => {
      const h = c.querySelector('h3');
      c.classList.toggle('yours', !!h && h.textContent.trim() === t.name);
    });

    show('rev');
    const n = $('r-name');
    n.style.animation = 'none'; void n.offsetWidth; n.style.animation = '';
  }

  $('back-ram').addEventListener('click', () => show('ram'));
  $('again').addEventListener('click', () => {
    state.ram = null; state.card = null; state.vram = 0; state.guessed = false;
    input.value = ''; shown = []; paint();
    game.classList.remove('lit');
    document.querySelectorAll('.tier-card.yours, .flat-tier.yours').forEach((c) => c.classList.remove('yours'));
    game.style.setProperty('--mk', '#8EA674');
    show('ram');
  });

  document.querySelectorAll('#game [data-ram]').forEach((b) => {
    b.addEventListener('click', () => {
      state.ram = b.getAttribute('data-ram');
      show('gpu');
      setTimeout(() => input.focus({ preventScroll: true }), 240);
    });
  });
})();
