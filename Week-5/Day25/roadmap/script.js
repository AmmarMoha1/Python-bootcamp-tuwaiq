document.addEventListener("DOMContentLoaded", function () {

    // =========================
    // 1) Fade-in Sections
    // =========================

    const sections = document.querySelectorAll(
        ".topic, .intro-banner, .summary-section"
    );

    if ("IntersectionObserver" in window) {

        const observer = new IntersectionObserver(
            function (entries) {

                entries.forEach(function (entry) {

                    if (entry.isIntersecting) {
                        entry.target.classList.add("visible");

                        observer.unobserve(entry.target);
                    }

                });

            },
            {
                threshold: 0.12
            }
        );

        sections.forEach(function (section) {

            section.classList.add("fade-in");

            observer.observe(section);

        });

    } else {

        sections.forEach(function (section) {

            section.classList.add("visible");

        });

    }


    // =========================
    // 2) Smooth Scrolling
    // =========================

    const navLinks = document.querySelectorAll(
        'nav a[href^="#"]'
    );

    navLinks.forEach(function (link) {

        link.addEventListener("click", function (event) {

            const targetId = link.getAttribute("href");

            const target = document.querySelector(targetId);

            if (target) {

                event.preventDefault();

                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });

            }

        });

    });


    // =========================
    // 3) Card Hover Effect
    // =========================

    const cards = document.querySelectorAll(".card");

    cards.forEach(function (card) {

        card.addEventListener("mouseenter", function () {

            card.style.transform = "translateY(-5px)";

        });

        card.addEventListener("mouseleave", function () {

            card.style.transform = "translateY(0)";

        });

    });


    // =========================
    // 4) Demo Button
    // =========================

    const demoButton = document.querySelector(".demo-button");

    if (demoButton) {

        demoButton.addEventListener("click", function () {

            demoButton.textContent = "Clicked!";

            setTimeout(function () {

                demoButton.textContent = "Hover Me";

            }, 1200);

        });

    }


    // =========================
    // 5) Console Check
    // =========================

    console.log(
        "Week 5 Roadmap JavaScript loaded successfully."
    );

});