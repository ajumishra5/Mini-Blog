document.addEventListener("DOMContentLoaded", function () {
  const likeBtn = document.getElementById("like-btn");
  if (!likeBtn) return;

  const likeCount = document.getElementById("like-count");
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  likeBtn.addEventListener("click", () => {
    fetch(likeBtn.dataset.url, {
      method: "POST",
      headers: {
        "X-CSRFToken": csrfToken,
        "X-Requested-With": "XMLHttpRequest"
      }
    })
    .then(res => res.json())
    .then(data => {
      likeCount.textContent = data.likes_count;
      likeBtn.classList.toggle("btn-danger", data.liked);
      likeBtn.classList.toggle("btn-outline-danger", !data.liked);
    });
  });
});