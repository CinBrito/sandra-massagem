// Header hide/show on scroll (mobile only)

let lastScrollY = window.scrollY;

const header = document.querySelector('.site-header');

window.addEventListener('scroll', () => {
  // só aplica no mobile
  if (window.innerWidth > 768 || !header) return;

  const currentScrollY = window.scrollY;

  // rolando para baixo e já passou do hero
  if (currentScrollY > lastScrollY && currentScrollY > 80) {
    header.classList.add('is-hidden');
  } else {
    header.classList.remove('is-hidden');
  }

  lastScrollY = currentScrollY;
});

// MOBILE MENU TOGGLE
const toggle = document.getElementById("menuToggle");
const menu = document.getElementById("mobileMenu");

if (toggle && menu) {
  toggle.addEventListener("click", () => {
    toggle.classList.toggle("active");
    menu.classList.toggle("open");
  });
}
