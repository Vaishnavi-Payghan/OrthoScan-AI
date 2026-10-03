// =============================
// Mobile Menu
// =============================

const menuBtn = document.getElementById("menuBtn");
const mobileMenu = document.getElementById("mobileMenu");


// Open / Close mobile menu

menuBtn.addEventListener("click", function () {

    mobileMenu.classList.toggle("show");

});


// Close menu after clicking a link

const mobileLinks = document.querySelectorAll(".mobile-link");

mobileLinks.forEach(link => {

    link.addEventListener("click", function () {

        mobileMenu.classList.remove("show");

    });

});


// =============================
// Desktop Active Navigation
// =============================

const currentPage = window.location.pathname.split("/").pop();

const desktopLinks = document.querySelectorAll(".nav-links .nav-link");

desktopLinks.forEach(link => {

    const linkPage = link.getAttribute("href").split("/").pop();

    if (linkPage === currentPage) {

        desktopLinks.forEach(item => {
            item.classList.remove("active");
        });

        link.classList.add("active");
    }

});