document.addEventListener("DOMContentLoaded", function () {
  const editPerfilModal = new bootstrap.Modal(
    document.getElementById("editPerfilModal")
  );

  document
    .getElementById("editar-pfp-button")
    .addEventListener("click", function () {
      const perfilId = this.dataset.perfilId;
      const perfilBio = this.dataset.perfilBio;
      const perfilImage = this.dataset.perfilImage;

      // Actualizar la URL del formulario con el perfil_id
      var form = document.getElementById("editPerfilForm");
      var actionUrl = form.getAttribute("action").replace("0", perfilId);
      form.setAttribute("action", actionUrl);

      document.getElementById("editBio").value = perfilBio;
      document.getElementById("PFP-edit").src = perfilImage;

      editPerfilModal.show();
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
});
