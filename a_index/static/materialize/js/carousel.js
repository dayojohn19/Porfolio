console.log('\n\n start ____-js/carousel.js')
// MOVE IT *******
var counter = 0;
// 
var i = setInterval(function () {
    next();
    counter++;
    if (counter % 3 == 0) {
        setTimeout(() => {
            prev();
        }, 3000)
    }
    // if (counter === 3) {
    //     clearInterval(i);
    // }
}, 2500);
// MOVE IT ****

// ////


document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.carousel');
    var Carouselinstances = M.Carousel.init(elems, {
        indicators: false,
        noWrap: true,
        numVisible: 2,

        fullWidth: false

    });
    Carouselinstances

    M.AutoInit();
    window.prev = function () {
        var el = document.querySelector(".carousel");
        var l = M.Carousel.getInstance(el);
        xx = document.querySelector(".active");
        l.prev();
    }
    window.next = function () {
        var el = document.querySelector(".carousel");
        var l = M.Carousel.getInstance(el);
        l.next();
    }
});

console.log('end ____-js/carousel.js \n\n ')
