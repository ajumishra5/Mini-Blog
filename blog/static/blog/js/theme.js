document.addEventListener("DOMContentLoaded", function () {
  const body = document.getElementById("site-body");
  const toggleBtn = document.getElementById("theme-toggle");
  

  if (localStorage.getItem("theme") === "dark") {
    body.classList.add("dark-mode");
    toggleBtn.innerText = "☀️ Light";
  }

  toggleBtn.addEventListener("click", () => {
    body.classList.toggle("dark-mode");

    if (body.classList.contains("dark-mode")) {
      localStorage.setItem("theme", "dark");
      toggleBtn.innerText = "☀️ Light";
    } else {
      localStorage.setItem("theme", "light");
      toggleBtn.innerText = "🌙 Dark";
    }
  });
});