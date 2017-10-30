'use strict';

$(document).ready(function () {

  $('.header').swiper({
    pagination: '.swiper-pagination',
    autoplay: 3000,
    loop: true
  });

  $('.st-container').swiper({
    slidesPerView: 'auto',
    paginationClickable: true,
    freeMode: true
  });

  $('.st-vertical').swiper({
    slidesPerView: 'auto',
    autoplay: 5000,
    direction: 'vertical',
    loop: true
  });
});