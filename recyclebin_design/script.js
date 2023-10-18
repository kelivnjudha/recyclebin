alert("JAVASCRIPT IS RUNNING")
var swiper = new Swiper('.swiper-container', {
    pagination: '.swiper-pagination',
    loop: true,
    slidesPerView: 'auto',
    paginationClickable: true,
    spaceBetween: 0,
    effect: "coverflow",
    coverflowEffect: {
        rotate: 50,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: true,
    },
});