document.addEventListener("DOMContentLoaded", () => {
  const lightbox = document.getElementById("galleryLightbox");
  const lightboxImg = document.getElementById("galleryLightboxImage");
  const closeBtn = document.getElementById("galleryLightboxClose");
  const triggers = document.querySelectorAll("[data-gallery-image]");

  if (!lightbox || !lightboxImg || !closeBtn || triggers.length === 0) return;

  const openLightbox = (src, title) => {
    lightboxImg.src = src;
    lightboxImg.alt = title ? `Foto ${title}` : "Foto";
    lightbox.classList.add("is-open");
    lightbox.setAttribute("aria-hidden", "false");
    document.body.classList.add("lightbox-open");
  };

  const closeLightbox = () => {
    lightbox.classList.remove("is-open");
    lightbox.setAttribute("aria-hidden", "true");
    document.body.classList.remove("lightbox-open");
    lightboxImg.src = "";
  };

  triggers.forEach((trigger) => {
    trigger.addEventListener("click", () => {
      const src = trigger.getAttribute("data-gallery-image");
      const title = trigger.getAttribute("data-gallery-title");
      if (!src) return;
      openLightbox(src, title);
    });
  });

  closeBtn.addEventListener("click", closeLightbox);

  lightbox.addEventListener("click", (event) => {
    if (event.target === lightbox) closeLightbox();
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && lightbox.classList.contains("is-open")) {
      closeLightbox();
    }
  });
});
