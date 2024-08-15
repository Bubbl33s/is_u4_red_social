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

  const deleteButtons = document.querySelectorAll(".delete-button");
  deleteButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const postId = this.dataset.postId;
      const confirmation = confirm(
        "¿Estás seguro de que deseas eliminar este post?"
      );

      if (confirmation) {
        window.location.href = `/eliminar_post/${postId}/`; // Asegúrate de que esta URL esté definida en tu URLconf
      }
    });
  });
});
