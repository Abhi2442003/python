/* static/js/scripts.js */

// Function to add or remove 'navbar-transparent' and 'navbar-scrolled' classes based on scroll position
window.onscroll = function() {
    var navbar = document.querySelector('.navbar');
    if (window.pageYOffset > 50) { // Adjust this value based on when you want the effect to trigger
        navbar.classList.add('navbar-scrolled');
        navbar.classList.remove('navbar-transparent');
    } else {
        navbar.classList.add('navbar-transparent');
        navbar.classList.remove('navbar-scrolled');
    }
};
