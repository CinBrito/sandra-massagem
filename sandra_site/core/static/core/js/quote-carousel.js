document.addEventListener("DOMContentLoaded", () => {
  const track = document.getElementById("quoteTrack");
  const wrapper = document.querySelector(".quote-track-wrapper");
  const prevBtn = document.querySelector("[data-quote-prev]");
  const nextBtn = document.querySelector("[data-quote-next]");

  if (!track || !wrapper || !prevBtn || !nextBtn) return;

  const scrollAmount = () => Math.max(wrapper.clientWidth * 0.8, 280);

  prevBtn.addEventListener("click", () => {
    wrapper.scrollBy({ left: -scrollAmount(), behavior: "smooth" });
  });

  nextBtn.addEventListener("click", () => {
    wrapper.scrollBy({ left: scrollAmount(), behavior: "smooth" });
  });
});
