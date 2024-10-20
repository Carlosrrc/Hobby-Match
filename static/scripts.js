document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.getElementById("menu-toggle");
    const nav = document.getElementById("main-nav");

    menuToggle.addEventListener("click", function() {
        nav.classList.toggle("hidden");
    });
});
