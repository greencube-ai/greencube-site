// Changelog pictures: click one to see it full size; arrows or the keyboard step through the page's pictures,
// Esc, the cross or a click on the dark background closes it. Without JavaScript the link opens the picture itself.
(function () {
  var view = document.querySelector('.cl-view');
  var shots = [].slice.call(document.querySelectorAll('a.cl-shot'));
  if (!view || !shots.length) return;
  var img = view.querySelector('img'), cap = view.querySelector('figcaption'), count = view.querySelector('.cl-count');
  var at = 0;
  function show(i) {
    at = (i + shots.length) % shots.length;
    var a = shots[at], thumb = a.querySelector('img');
    img.src = a.getAttribute('href');
    img.alt = thumb ? thumb.alt : '';
    cap.textContent = a.textContent.trim();
    count.textContent = shots.length > 1 ? (at + 1) + ' / ' + shots.length : '';
  }
  function open(i) {
    show(i);
    view.hidden = false;
    document.documentElement.classList.add('cl-locked');
    view.querySelector('.cl-x').focus();
  }
  function close() {
    view.hidden = true;
    img.removeAttribute('src');
    document.documentElement.classList.remove('cl-locked');
    if (shots[at]) shots[at].focus();
  }
  shots.forEach(function (a, i) {
    a.addEventListener('click', function (e) { e.preventDefault(); open(i); });
  });
  view.addEventListener('click', function (e) {
    var t = e.target;
    if (t.closest('.cl-prev')) show(at - 1);
    else if (t.closest('.cl-next')) show(at + 1);
    else if (t.closest('.cl-x') || !t.closest('img')) close();
  });
  document.addEventListener('keydown', function (e) {
    if (view.hidden) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') show(at - 1);
    else if (e.key === 'ArrowRight') show(at + 1);
  });
  if (shots.length < 2) { view.querySelector('.cl-prev').hidden = true; view.querySelector('.cl-next').hidden = true; }
})();
