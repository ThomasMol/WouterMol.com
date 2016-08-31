$(document).ready(function () {
    
     $(".jumbotron").css("height", $(window).height() * 0.5);
                $(".jumbotron .container").css("padding", 75);
    
    $(window).scroll(function () {
        if ($(this).scrollTop() === 0) {
            $("nav").addClass("atTop");
        }
        else {
            $("nav").removeClass("atTop");
        }
    });
});