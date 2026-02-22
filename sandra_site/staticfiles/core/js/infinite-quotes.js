document.addEventListener("DOMContentLoaded", () => {
  const track = document.getElementById("quoteTrack");
  if (!track) return;

  const speed = 0.3; // menor = mais elegante
  let position = 0;

  // DUPLICAR conteúdo para loop infinito
  track.innerHTML += track.innerHTML;

  function animate() {
    position -= speed;

    if (Math.abs(position) >= track.scrollWidth / 2) {
      position = 0;
    }

    track.style.transform = `translateX(${position}px)`;
    requestAnimationFrame(animate);
  }

  animate();

  // pause no hover (desktop)
  track.addEventListener("mouseenter", () => speedBackup());
  track.addEventListener("mouseleave", () => speedRestore());

  let savedSpeed = speed;

  function speedBackup() {
    savedSpeed = speed;
    speed = 0;
  }

  function speedRestore() {
    speed = savedSpeed;
  }
});
