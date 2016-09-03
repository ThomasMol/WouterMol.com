$(document).ready(function () {
    
    $(".caption").css({"height": "100%","width": $("#albums img").width()});
    
    $(".caption").click(function () {
        var catname = $(this).data("cat");
        var sources = [{}];
        $.getJSON("database/categories/" + catname + ".json", function (data) {
            $.each(data.images, function (index, value) {
                sources.push({
                    "src": "images/" + value.filename
                    , "thumb": "images/" + value.thumbnail
                    , "subHtml": "<h4>" + value.name + "</h4><p>" + value.description + "</p>"
                });
            });
            sources.splice(0, 1);
            $(".caption[data-cat='"+catname+"']").lightGallery({
                dynamic: true
                , download: false
                , dynamicEl: sources
            });
            
            console.log($(".caption[data-catSS='"+catname+"']"));
        });
    });
});
