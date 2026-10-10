// Phones: the menu is one row you can swipe (see mobile.css). Scroll it so
// the page you're on is in view instead of hidden past the right edge.
(() => {
  const a = document.querySelector('header > .nav a.on, header > .header-nav a.on');
  if (!a || innerWidth > 640) return;
  const nav = a.parentElement;
  nav.scrollLeft += a.getBoundingClientRect().left - nav.getBoundingClientRect().left - (nav.clientWidth - a.offsetWidth) / 2;
})();
