document.addEventListener("DOMContentLoaded", function () {
  const toggleUsuarios = document.getElementById("toggle-usuarios");
  const usuariosContainer = document.querySelector(".usuarios-container");
  const closeUsuarios = document.getElementById("close-usuarios");

  toggleUsuarios.addEventListener("click", function () {
    usuariosContainer.classList.toggle("active");
  });

  closeUsuarios.addEventListener("click", function () {
    usuariosContainer.classList.remove("active");
  });

  document.addEventListener("click", function (event) {
    if (
      usuariosContainer.classList.contains("active") &&
      !usuariosContainer.contains(event.target) &&
      !toggleUsuarios.contains(event.target)
    ) {
      usuariosContainer.classList.remove("active");
    }
  });

  // Modales
  const editButtons = document.querySelectorAll(".btn-edit");
  const editPostModal = new bootstrap.Modal(
    document.getElementById("editPostModal")
  );

  editButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const postId = this.dataset.postId;
      const postContent = this.dataset.postContent;
      const postImage = this.dataset.postImage;

      // Actualizar la URL del formulario con el post_id
      var form = document.getElementById("editPostForm");
      var actionUrl = form.getAttribute("action").replace("0", postId);
      form.setAttribute("action", actionUrl);

      document.getElementById("editContent").value = postContent;
      // Si quieres manejar la imagen, considera cómo mostrarla o actualizarla.
      if (postImage !== "") {
        document.getElementById("edit-img-container").style.display = "block";
        document.getElementById("edit-noimg-container").style.display = "none";
        document.getElementById("img-edit").src = postImage;
      } else {
        document.getElementById("edit-img-container").style.display = "none";
        document.getElementById("edit-noimg-container").style.display = "block";
      }

      editPostModal.show();
    });
  });

  const deleteButtons = document.querySelectorAll(".btn-delete");
  deleteButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const postId = this.dataset.postId;

      // Actualizar la URL del formulario con el post_id
      var form = document.getElementById("deletePostForm");
      var actionUrl = form.getAttribute("action").replace("0", postId);
      form.setAttribute("action", actionUrl);
    });
  });

  let csrfToken = document
    .querySelector('meta[name="csrf-token"]')
    .getAttribute("content");

  const match = csrfToken.match(/value="([^"]+)"/);

  if (match) {
    csrfToken = match[1];
  }

  console.log(csrfToken);

  document.querySelectorAll(".likes").forEach((likeDiv) => {
    likeDiv.addEventListener("click", () => {
      const postId = likeDiv.dataset.postId;

      fetch(`/social/like/${postId}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken,
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          if (data.liked) {
            likeDiv.classList.add("liked");
          } else {
            likeDiv.classList.remove("liked");
          }
          likeDiv.querySelector("span").textContent = data.likes_count;
        })
        .catch((error) => {
          console.error("There was a problem with the fetch operation:", error);
        });
    });
  });
});
