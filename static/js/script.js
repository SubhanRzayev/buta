
let scroollButtonVisibilite = () => {
    let windowpos = $(window).scrollTop();
    let scrollLink = $('.scroll-to-top');
    if (windowpos > 300) {
        scrollLink.fadeIn(300);
    } else {
        scrollLink.fadeOut(300);
    }
}

scroollButtonVisibilite();

$(window).on('scroll', function () {
    scroollButtonVisibilite();
});


$(".scroll-to-top").on('click', function () {

    $('html, body').animate({
        scrollTop: $('body').offset().top
    }, 100);

});


