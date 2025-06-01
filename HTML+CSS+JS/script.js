 // Кукі функції (дуже просто)
function setCookie(name, value) {
    document.cookie = name + "=" + value;
}

function getCookie(name) {
    let c = document.cookie.split(";");
    for (let i = 0; i < c.length; i++) {
        let part = c[i];
        if (part[0] === " ") {
            part = part.slice(1); 
        }
        if (part.indexOf(name + "=") === 0) {
            return part.split("=")[1];
        }
    }
    return "";
}


// Код після завантаження
window.onload = function () {
    // Кукі-бар
    let bar = document.querySelector("#cookie-bar");
    if (getCookie("cookie_accepted") != "true") {
        bar.style.display = "flex";
    }

    let accept = document.querySelector("#cookie-accept");
    accept.onclick = function () {
        setCookie("cookie_accepted", "true");
        bar.style.display = "none";
    };

    // Мобільне меню
    let btn = document.querySelector(".menu-toggle");
    let nav = document.querySelector("nav ul");
    btn.onclick = function () {
        if (nav.className == "active") {
            nav.className = "";
            btn.className = "menu-toggle";
        } else {
            nav.className = "active";
            btn.className = "menu-toggle active";
        }
    };

    let links = document.querySelectorAll("nav ul a");
    for (let i = 0; i < links.length; i++) {
        links[i].onclick = function () {
            nav.className = "";
            btn.className = "menu-toggle";
        };
    }

    // Слайдер для менторів
    let swiper = new Swiper(".mySwiper", {
        slidesPerView: 1,
        spaceBetween: 20,
        loop: true,
        pagination: {
            el: ".swiper-pagination",
            clickable: true
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev"
        },
        breakpoints: {
            768: { slidesPerView: 2 },
            1024: { slidesPerView: 3 }
        }
    });

    // Анімації
    AOS.init({
        duration: 1000,
        once: true
    })

    // Кнопка вверх
    let up = document.querySelector("#scroll-to-top");
    let header = document.querySelector("header");
    let lastY = window.scrollY;
    let hidden = false;
    let appeared = false;

    window.onscroll = function () {
        if (window.scrollY > 300) {
            up.className = "scroll-to-top visible";
        } else {
            up.className = "scroll-to-top";
        }

        // Приховування/показ хедера
        let nowY = window.scrollY;
        if (nowY > lastY && nowY > 100 && !hidden) {
            header.className = "hidden";
            hidden = true;
        } else if (nowY < lastY && hidden && !appeared) {
            header.className = "";
            appeared = true;
        }
        lastY = nowY;
    };

    up.onclick = function () {
        window.scrollTo(0, 0);
    };

    // Модальне вікно
    let modal = document.querySelector("#modal");
    let open1 = document.querySelector("#open-modal");
    let open2 = document.querySelector("#open-modal-contact");
    let close = document.querySelector("#modal-close");
    let send = document.querySelector("#modal-submit");

    open1.onclick = function () {
        modal.style.display = "flex";
    };
    open2.onclick = function () {
        modal.style.display = "flex";
    };

    close.onclick = function () {
        modal.style.display = "none";
        n.value = "";
        e.value = "";
        p.value = "";
        n.style.border = "";
        e.style.border = "";
        p.style.border = "";
    };

    modal.onclick = function (e) {
        if (e.target == modal) {
            modal.style.display = "none";
            n.value = "";
            e.value = "";
            p.value = "";
            n.style.border = "";
            e.style.border = "";
            p.style.border = "";
        }
    }

    let n = document.querySelector("#modal-name");
    let e = document.querySelector("#modal-email");
    let p = document.querySelector("#modal-phone");
    let nameError = document.querySelector("#name-error");
    let emailError = document.querySelector("#email-error");
    let phoneError = document.querySelector("#phone-error");

    send.onclick = function () {
        let ok = true;

        nameError.style.display = "none";
        emailError.style.display = "none";
        phoneError.style.display = "none";
        n.style.border = "";
        e.style.border = "";
        p.style.border = "";

        if (n.value == "") {
            n.style.border = "1px solid red";
            nameError.textContent = "Введіть ім’я";
            nameError.style.display = "block";
            ok = false;
        }

        let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(e.value)) {
            e.style.border = "1px solid red";
            emailError.textContent = "Введіть коректний email";
            emailError.style.display = "block";
            ok = false;
        }

        if (p.value == "") {
            p.style.border = "1px solid red";
            phoneError.textContent = "Введіть номер телефону";
            phoneError.style.display = "block";
            ok = false;
        }

        if (ok) {
            alert("Форма відправлена");
            modal.style.display = "none";
            n.value = "";
            e.value = "";
            p.value = "";
        }
    }

    // Тема
    let themeBtn = document.querySelector("#theme-toggle");
    let body = document.body;

    if (getCookie("theme") == "dark") {
        body.className = "dark-theme";
        themeBtn.innerHTML = "Світла тема";
    } else {
        themeBtn.innerHTML = "Темна тема";
    }

    themeBtn.onclick = function () {
        if (body.className == "dark-theme") {
            body.className = "";
            themeBtn.innerHTML = "Темна тема";
            setCookie("theme", "light");
        } else {
            body.className = "dark-theme";
            themeBtn.innerHTML = "Світла тема";
            setCookie("theme", "dark");
        }
    };

    // Таймер
    let end = new Date().getTime() + 7 * 24 * 60 * 60 * 1000; // 7 днів

    setInterval(function () {
        let now = new Date().getTime();
        let left = end - now;

        let d = Math.floor(left / (1000 * 60 * 60 * 24));
        let h = Math.floor((left % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        let m = Math.floor((left % (1000 * 60 * 60)) / (1000 * 60));
        let s = Math.floor((left % (1000 * 60)) / 1000);

        if (left < 0) {
            d = 0;
            h = 0;
            m = 0;
            s = 0;
            document.querySelector("#countdown-timer").innerHTML = "Курс розпочався!";
        }

        if (d < 10) {
            d = "0" + d;
        }
        if (h < 10) {
            h = "0" + h;
        }
        if (m < 10) {
            m = "0" + m;
        }
        if (s < 10) {
            s = "0" + s;
        }


        document.querySelector("#days").innerHTML = d;
        document.querySelector("#hours").innerHTML = h;
        document.querySelector("#minutes").innerHTML = m;
        document.querySelector("#seconds").innerHTML = s;
    }, 1000);
}