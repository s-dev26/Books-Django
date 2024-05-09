const expandButton = document.getElementById("button_review");
const expandableForm = document.getElementById("form_review");

expandButton.addEventListener("click", function () {
  expandableForm.style.display =
    expandableForm.style.display === "none" ? "block" : "none";
});

const stars = document.querySelectorAll(".star-label");

stars.forEach((star) => {
  star.addEventListener("click", function () {
    const clickedStarValue = parseInt(
      this.getAttribute("for").replace("star", "")
    );
    const ratingInput = document.querySelector("#rating");

    stars.forEach((s) => s.classList.remove("selected"));
    for (let i = 1; i <= clickedStarValue; i++) {
      const starInput = document.getElementById("star" + i + "_review");
      starInput.checked = true;
      document
        .querySelector(`label[for="star${i}_review"]`)
        .classList.add("selected");
    }
    ratingInput.value = clickedStarValue;
  });
});

let loginForm = document.querySelector(".login-form-container");

document.querySelector("#login-btn").onclick = () => {
  loginForm.classList.toggle("active");
};

document.querySelector("#close-login-btn").onclick = () => {
  loginForm.classList.remove("active");
};

window.onscroll = () => {
  const headerElement = document.querySelector(".header .header_2");

  if (window.scrollY > 80) {
    headerElement.classList.add("active");
  } else {
    headerElement.classList.remove("active");
  }
};
var swiper = new Swiper(".books-slider", {
  loop: true,
  centeredSlides: true,
  autoplay: {
    delay: 9500,
    disableOnInteraction: false,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});

var swiper = new Swiper(".ourselection-slider", {
  loop: true,
  centeredSlides: true,
  autoplay: {
    delay: 9500,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    450: {
      slidesPerView: 2,
    },
    768: {
      slidesPerView: 3,
    },
    1024: {
      slidesPerView: 4,
    },
  },
});

var swiper = new Swiper(".novelty-slider", {
  loop: true,
  centeredSlides: true,
  autoplay: {
    delay: 9500,
    disableOnInteraction: false,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});

var swiper = new Swiper(".reviews-slider", {
  spaceBetween: 10,
  grabCursor: true,
  loop: true,
  centeredSlides: true,
  autoplay: {
    delay: 9500,
    disableOnInteraction: false,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});
