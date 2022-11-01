const sliders = document.querySelectorAll(".post-img-slider");
sliders.forEach((slider) => {
    const slides = slider.querySelectorAll(".post-img-slides");
    slides.forEach((slide, indx) => {
        slide.style.transform = `translateX(0%)`;
    });
});


function nav_next(elem){
    var parent = elem.parentElement;
    const slides = parent.querySelectorAll(".post-img-slides");
    var length = slides.length;

    parent.classList.add("")
    
    //   move slide by -100%
    slides.forEach((slide, indx) => {
        slide.style.transform = `translateX(${current_X - 100}%)`;
    });
    console.log(current_X);
}