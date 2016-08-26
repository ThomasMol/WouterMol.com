$(document).ready(function () {
        
    $.getJSON("database.json", function (data) {
        
        //get all categories
        var cats = [];
        $.each(data, function(i){
            cats.push(data[i].category); 
        });
        cats = cats.join(",").split(",");
        var sorted_cats = cats.slice().sort();
        var categories = [];
        for(var i = 0; i <cats.length; i++){
            if (sorted_cats[i + 1] != sorted_cats[i]) {                
                categories.push(sorted_cats[i]);
            }            
        }
        
        $.each(categories, function(i){
            $(".categories ul").append("<li><a href='gallery/"+ categories[i] +"'>"+ categories[i] +"</a></li>");
        });
        
        
        
        //get all thumbnails and display them 
        var thumbs = [];      
        $.each(data, function (i) {
            thumbs.push("<div class='col-md-4'><img id='"+ data[i].filename +"' src='images/" + data[i].filename + "'></div>");
        });        
        $(".images .row").append(thumbs);
        
        
    });
});