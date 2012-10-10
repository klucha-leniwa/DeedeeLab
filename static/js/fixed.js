$(document).ready(function() {
    var theLoc = $('#navbar_top').position().top;
     $(window).scroll(function() {
        if(theLoc >= $(window).scrollTop()) {
            if($('#navbar_top').hasClass('fixed')) {
                $('#navbar_top').removeClass('fixed');
            }
        } else {
            if(!$('#navbar_top').hasClass('fixed')) {
                $('#navbar_top').addClass('fixed');
            }
        }
    });
});