$(document).ready(function(){
    BundleAll()
});

function foldMenu() {
    $('.bullet').on('click', function(){
        var $menu = $(this).parents('.menu');
        $menu.children('ul').toggle('fade', 100, function(){
            if ($menu.hasClass('black')) {
                $menu.removeClass('black');
            } else {
                $menu.addClass('black');
            }
        });
        if ($(this).hasClass('animate')) {
            $(this).removeClass('animate');
        } else {
            $(this).addClass('animate');
        }
    });
};

function modal(){

    $('.add').on('click', function() {
        $('.overlay-container').fadeIn('100', function() {
            $('.window-container.zoomin').addClass('window-container-visible');
        });
    });

    $('.close').click(function() {
        $('.overlay-container').fadeOut().end().find('.window-container').removeClass('window-container-visible');
    });
};

function BundleAll() {
    $('.menu').children('ul').hide()
    foldMenu();
    modal();
}