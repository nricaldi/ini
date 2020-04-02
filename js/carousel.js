const track = document.querySelector('.carousel__track');
const slides = Array.from(track.children);
const next = document.querySelector('.carousel__button--right');
const prev = document.querySelector('.carousel__button--left');
const dotsNav = document.querySelector('.carousel__nav');
const dots = Array.from(dotsNav.children);
let slideWidth = slides[0].clientWidth;

window.onresize = () => {
     slideWidth = slides[0].clientWidth;
     console.log(slideWidth);
     slides.forEach(setSlidePosition);
}

// arrange slides next to each other
const setSlidePosition = (slide, index) => {
    slide.style.left = slideWidth * index + 'px';
};
slides.forEach(setSlidePosition);


// function to move slide to the selected slide
const moveSlide = (track, currentSlide, targetSlide) => {
    track.style.transform = 'translateX(-' + targetSlide.style.left; + ')';
    currentSlide.classList.remove('current-slide');
    targetSlide.classList.add('current-slide');
}

const updateDots = (currentDot, targetDot) => {
    currentDot.classList.remove('current-slide');
    targetDot.classList.add('current-slide');
}

const checkNav = (targetSlide) => {
    targetSlide.nextElementSibling ? next.classList.remove('hidden') : next.classList.add('hidden');
    targetSlide.previousElementSibling ? prev.classList.remove('hidden') : prev.classList.add('hidden');
  }

// click next button moves to the next slide
next.addEventListener('click', () => {
    const currentSlide = track.querySelector('.current-slide');
    const nextSlide = currentSlide.nextElementSibling;
    const currentDot = dotsNav.querySelector('.current-slide');
    const nextDot = currentDot.nextElementSibling;

    moveSlide(track, currentSlide, nextSlide);
    updateDots(currentDot, nextDot);
    checkNav(nextSlide);

});

prev.addEventListener('click', () => {
    const currentSlide = track.querySelector('.current-slide');
    const previousSlide = currentSlide.previousElementSibling;
    const currentDot = dotsNav.querySelector('.current-slide');
    const previousDot = currentDot.previousElementSibling;

    moveSlide(track, currentSlide, previousSlide);
    updateDots(currentDot, previousDot);
    checkNav(previousSlide);
});


dotsNav.addEventListener('click', e => {
    const targetDot = e.target.closest('button');

    if(!targetDot) return;

    const currentSlide = track.querySelector('.current-slide');
    const currentDot = dotsNav.querySelector('.current-slide');
    const targetIndex = dots.findIndex(dot => dot === targetDot);
    const targetSlide = slides[targetIndex];

    moveSlide(track, currentSlide, targetSlide);
    updateDots(currentDot, targetDot);
    checkNav(targetSlide);
});