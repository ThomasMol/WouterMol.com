<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <script src="https://code.jquery.com/jquery-3.1.0.min.js"></script>
    <script src="http://use.edgefonts.net/source-sans-pro:n4,n9,n7,i7,i4,n3,i3,n6,i6,i9,n2,i2:all.js"></script> 
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>  
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0">
    <meta name="mobile-web-app-capable" content="yes" />
    <meta name="theme-color" content="#000" />
    <link rel="shortcut icon" type="image/png" href="img/logo.ico" />    
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="style/style.css">
    <title>WouterMol.com | Home</title>
</head>

<body>

    <nav class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">                
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#id-collapse-top-nav" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>                
                <a href="#" class="navbar-brand">WouterMol.com</a>
            </div>            
            <div class="collapse navbar-collapse navbar-right" id="id-collapse-top-nav">      
                <ul class="nav navbar-nav">
                    <li ><a href="index"><span class="glyphicon glyphicon-home"></span></a></li>
                    <li><a href="gallery/All">gallery</a></li>
                    <li class="active"><a href="albums">albums</a></li>
                </ul>
            </div>
        </div>        
    </nav>

    <section id="main">
    <div class="jumbotron albums">
        <div class="container">
            <h1 id="hello-message">Albums</h1>
            <h2 id="sub-message">Gallery of albums</h2>
        </div>
    </div>
        
    <div id="albums" class="container">
        <?php 
        $albums = array_filter(glob('database/albums/*'), 'is_file');
        $album = array();
        foreach($albums as $file) {
            $file = pathinfo($file);
            array_push($album,$file['filename']);
        }
        
        foreach($album as $albumname){
            echo 
            "<h1 >". $albumname ."</h1><a href='#'>view more</a>
            <div class='row' data-albumname='". $albumname ."'>".
            
            
            
            "</div>";
        }
        
        
        
        ?>
    </div>
        
    
    </section>

    <footer>
    </footer>
    <script>
    $(".jumbotron").css("height", $(window).height() * 0.4);
        
    $(document).ready(function(){
        var albumnames = [];
        
        $("#albums div").each(function(){
            albumnames.push($(this).attr("data-albumname"));
        });
        
        $.each(albumnames, function(index, value){            
            $.getJSON("database/albums/" + value +".json", function(data){
                
                $.each(data.slice(0,3), function(index, value2){
                $("div[data-albumname='"+ value +"']").append("<div class='col-sm-4'><img src='images/"+ data[index]['filename'] +"' height='200'></div>");
                   console.log(data[index]['filename']); 
                });
                
            });
        });
    });
    </script>
</body>
</html>
