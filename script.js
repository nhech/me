// mobile nav
const toggle = document.querySelector('.nav__toggle');
const sheet = document.getElementById('menu');

if (toggle && sheet) {
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!open));
    sheet.dataset.open = String(!open);
  });

  sheet.addEventListener('click', (e) => {
    if (e.target.tagName !== 'A') return;
    toggle.setAttribute('aria-expanded', 'false');
    sheet.dataset.open = 'false';
  });

  // reset when we cross into desktop so the sheet never sticks open
  const desktop = window.matchMedia('(min-width: 768px)');
  desktop.addEventListener('change', (e) => {
    if (!e.matches) return;
    toggle.setAttribute('aria-expanded', 'false');
    sheet.dataset.open = 'false';
  });
}
