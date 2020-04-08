const controller = new ScrollMagic.Controller();

// Animation for headline
gsap.from(".anim1", {opacity: 0, stagger: .5, y: 50});


// Animation for hero background
const tl = new TimelineMax({repeat:-1}); /* repeat loop forever */
tl.to("#bg", 150,{
  backgroundPosition: "-3840px bottom", /* negative width of background image your animating - left top */
  ease: Linear.easeNone /* make sure you use Linear.easeNone so its smooth */
});

// Animation for Services
const tl2 = new TimelineMax();
tl2.from('.service', {opacity: 0, duration: 1, stagger: .4, y: -200});

const serviceScene = new ScrollMagic.Scene({
    triggerElement: '#services'
})
.setTween(tl2)
.addTo(controller);

// Animation for How we work section
const tl3 = new TimelineMax();

tl3.from(".step", .5, {opacity: 0, stagger: .6, duration: 1, y: 80});

const howScene = new ScrollMagic.Scene({
    triggerElement: '.testimonials form',
})
.setTween(tl3)
.addTo(controller)


// Animation for gallery
gsap.from('.grid-item', {opacity:0, duration: 1, stagger: .5});