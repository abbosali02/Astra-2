var swiper = new Swiper(".slide-content", {
    slidesPerView: 3,
    spaceBetween: 25,
    loop: true,
    centerSlide: 'true',
    fade: 'true',
    grabCursor: 'true',
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },

    breakpoints:{
        0: {
            slidesPerView: 1,
        },
        520: {
            slidesPerView: 2,
        },
        950: {
            slidesPerView: 3,
        },
    },
  });

  /*======================================================
                      FAQ
======================================================*/
const questions = document.querySelectorAll(".faq-section-text-main");

questions.forEach(function (question) {
	const btn = question.querySelector(".question-btn");
	btn.addEventListener("click", function () {
		questions.forEach(function (item) {
			if (item !== question) {
				item.classList.remove("show-text");
			}
		});
		question.classList.toggle("show-text");
	});
});
