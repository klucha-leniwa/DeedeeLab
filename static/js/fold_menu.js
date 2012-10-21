$(document).ready(function() {
    $('.toggle > ul').hide()
})

$('.toggle').click(function() {
    var x = function(){
        if($('.toggle').hasClass('hover')) {
            $('.toggle').removeClass('hover')
        } else {
            $('.toggle').addClass('hover')
        }
    }
    x();
    $('.toggle > ul').toggle('fold')
    return false;
})