$('.second-slide').owlCarousel({
    loop:false,
    dots:false,
    items:2,
    autoWidth: true,
    margin:20,
    nav:false,
    autoplay:false,
    autoplayTimeout:2000,
    autoplayHoverPause:false
    })


    $('.product-slide').owlCarousel({
        loop:true,
        nav:true,
        items:1,
        dots:false,
        navText: ["<img src='/static/svg/arrow-left.svg' %}'>", "<img src='/static/svg/arrow-right.svg' %}'>"],
    
    })
    