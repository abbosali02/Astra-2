let slidehomepage = 1;
showSlides(slidehomepage);

function plusSlides(n) {
  showSlides((slidehomepage += n));
}

function currentSlide(n) {
  showSlides((slidehomepage = n));
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {
    slidehomepage = 1;
  }
  if (n < 1) {
    slidehomepage = slides.length;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slidehomepage - 1].style.display = "block";
  dots[slidehomepage - 1].className += " active";
}
