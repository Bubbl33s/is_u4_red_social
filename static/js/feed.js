document.addEventListener("DOMContentLoaded", function () {
  const toggleUsuarios = document.getElementById("toggle-usuarios");
  const usuariosContainer = document.querySelector(".usuarios-container");

  toggleUsuarios.addEventListener("click", function () {
    usuariosContainer.classList.toggle("active");
  });
});
