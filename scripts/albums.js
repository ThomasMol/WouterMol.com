$(document).ready(function () {
    
    $(".caption").css({"height": $("#albums img").height() ,"width": $("#albums img").width()});
    
    $(".caption").click(function () {
        var albumname = $(this).data("album");
        var sources = [{}];
        $.getJSON("database/albums/" + albumname + ".json", function (data) {
            $.each(data, function (index, value) {
                sources.push({
                    "src": "images/" + value.filename
                    , "thumb": "images/" + value.thumbnail
                    , "subHtml": "<h4>" + value.name + "</h4><p>" + value.description + "</p>"
                });
            });
            sources.splice(0, 1);
            $(".caption[data-album='"+albumname+"']").lightGallery({
                dynamic: true
                , download: false
                , dynamicEl: sources
            });
            
            console.log($(".caption[data-album='"+albumname+"']"));
        });
    });
});
