$('.bullet').click(function(){
    if ($('#navbar_top > ul > li:first-child').hasClass('visible')) {
        $('#navbar_top > ul > li:first-child').removeClass('visible').addClass('hidden')
    } else {
        $('#navbar_top > ul > li:first-child').removeClass('hidden').addClass('visible')
    }
})