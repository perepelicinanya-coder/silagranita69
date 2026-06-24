const toggle = document.querySelector(".menu-toggle");
const nav = document.querySelector(".main-nav");

if (toggle && nav) {
  toggle.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    document.body.classList.toggle("menu-open", open);
    toggle.setAttribute("aria-expanded", String(open));
  });
  nav.querySelectorAll("a").forEach((link) => link.addEventListener("click", () => {
    nav.classList.remove("open");
    document.body.classList.remove("menu-open");
    toggle.setAttribute("aria-expanded", "false");
  }));
}

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });
document.querySelectorAll(".reveal").forEach((element) => observer.observe(element));

document.querySelectorAll("[data-whatsapp-form]").forEach((form) => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const data = new FormData(form);
    const parts = [
      "Здравствуйте! Хочу получить расчёт.",
      `Имя: ${data.get("name") || "не указано"}`,
      `Телефон: ${data.get("phone") || "не указан"}`,
      `Изделие: ${data.get("product") || "не указано"}`,
      `Комментарий: ${data.get("message") || "нет"}`
    ];
    window.open(`https://wa.me/79201557971?text=${encodeURIComponent(parts.join("\n"))}`, "_blank", "noopener");
  });
});

document.querySelectorAll("[data-year]").forEach((node) => {
  node.textContent = new Date().getFullYear();
});

document.querySelectorAll("[data-carousel]").forEach((carousel) => {
  const track = carousel.querySelector(".carousel__track");
  const slides = [...carousel.querySelectorAll(".carousel__slide")];
  const previous = carousel.querySelector("[data-carousel-prev]");
  const next = carousel.querySelector("[data-carousel-next]");
  const current = carousel.querySelector("[data-carousel-current]");
  let index = 0;
  let pointerStart = null;

  const render = () => {
    track.style.transform = `translateX(-${index * 100}%)`;
    if (current) current.textContent = String(index + 1).padStart(2, "0");
  };
  const move = (direction) => {
    index = (index + direction + slides.length) % slides.length;
    render();
  };
  previous?.addEventListener("click", () => move(-1));
  next?.addEventListener("click", () => move(1));
  carousel.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft") move(-1);
    if (event.key === "ArrowRight") move(1);
  });
  carousel.addEventListener("pointerdown", (event) => {
    pointerStart = event.clientX;
  });
  carousel.addEventListener("pointerup", (event) => {
    if (pointerStart === null) return;
    const distance = event.clientX - pointerStart;
    if (Math.abs(distance) > 45) move(distance > 0 ? -1 : 1);
    pointerStart = null;
  });
  carousel.addEventListener("pointercancel", () => {
    pointerStart = null;
  });
  render();
});
