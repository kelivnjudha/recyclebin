alert("JAVASCRIPT IS RUNNING")

$(document).ready(function(){
    $.ajaxSetup({
        headers: { "X-CSRFToken": '{{ csrf_token }}' }
    });

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

    $('.content').click(function(){
        $('.content').toggleClass("heart-active")
        $('.text').toggleClass("heart-active")
        $('.numb').toggleClass("heart-active")
        $('.heart').toggleClass("heart-active")
    });
});

    
var clicks = 0;

function onClick(info_object_id) {
    $.ajax({
        url: `/like/${info_object_id}/`,
        method: 'POST',
        success: function(response) {
            document.getElementById(`clicks_${info_object_id}`).innerHTML = response.like_count;
        }
    });
}

// Call this function on page load to set the initial like counts
function setInitialLikeCounts() {
    {% for info_object in info_objects %}
    $.ajax({
        url: `/get_like_count/${info_object.id}/`,
        method: 'GET',
        success: function(response) {
            document.getElementById(`clicks_${info_object.id}`).innerHTML = response.like_count;
        }
    });
    {% endfor %}
}

$(document).ready(function() {
    setInitialLikeCounts();
});

