// Mobile Menu Toggle
document.getElementById('mobile-menu-button').addEventListener('click', function () {
    const menu = document.getElementById('mobile-menu');
    menu.classList.toggle('open');
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        // Close mobile menu if open
        const mobileMenu = document.getElementById('mobile-menu');
        if (mobileMenu.classList.contains('open')) {
            mobileMenu.classList.remove('open');
        }

        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 80,
                behavior: 'smooth'
            });
        }
    });
});

// Highlight active nav link on scroll
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', function () {
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= (sectionTop - 100)) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active-nav');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active-nav');
        }
    });
});

// Back to Top Button
const backToTopButton = document.getElementById('back-to-top');
window.addEventListener('scroll', function () {
    if (window.pageYOffset > 300) {
        backToTopButton.classList.add('visible');
    } else {
        backToTopButton.classList.remove('visible');
    }
});
backToTopButton.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Disable parallax on mobile devices
function checkParallax() {
    const parallaxElements = document.querySelectorAll('.parallax');
    if (window.innerWidth < 768) {
        parallaxElements.forEach(el => el.style.backgroundAttachment = 'scroll');
    } else {
        parallaxElements.forEach(el => el.style.backgroundAttachment = 'fixed');
    }
}
window.addEventListener('resize', checkParallax);
checkParallax();

// Initialize Flatpickr
document.querySelectorAll(".flatpickr-input").forEach(input => {
    flatpickr(input, {
        altInput: true,
        altFormat: "d.m.Y",
        dateFormat: "Y-m-d",
        minDate: "today"
    });
});

// Open/Close Booking Modal
document.getElementById("openBookingModal").addEventListener("click", () => {
    document.getElementById("bookingModal").classList.remove("hidden");
});
document.getElementById("openBookingModalMobile").addEventListener("click", () => {
    document.getElementById("bookingModal").classList.remove("hidden");
});
document.getElementById("openBookingModalFromAccommodation").addEventListener("click", () => {
    document.getElementById("bookingModal").classList.remove("hidden");
});
document.getElementById("closeModal").addEventListener("click", () => {
    document.getElementById("bookingModal").classList.add("hidden");
});
window.addEventListener("click", (e) => {
    const modal = document.getElementById("bookingModal");
    if (e.target === modal) {
        modal.classList.add("hidden");
    }
});