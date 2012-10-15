$('#navbar_top > ul > li:not(:first-child)').click(function(){
    $('.active').removeClass('active');
    $(this).addClass('active')
});
