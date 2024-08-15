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
});
