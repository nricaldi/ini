const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
const links = document.querySelectorAll('.nav-links li');
const lines = document.querySelectorAll('.hamburger div.line');
const navheight = document.getElementById('nav').offsetHeight;

hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    lines.forEach(line => {
        line.classList.toggle('open-line');
    })

});


links.forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.toggle('open');
        lines.forEach(line => {
            line.classList.remove('open-line');
        });
    });
});


// function smoothscroll(target, duration) {
//     var target = document.querySelector(target);
//     var targetPosition = target.getBoundingClientRect();
//     console.log(targetPosition);
// }

var scroll = new SmoothScroll('a[href*="#"]', {
    speed: 600,
    offset: navheight,
    updateURL: false
});



console.log('navbar activated');