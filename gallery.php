<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <script src="https://code.jquery.com/jquery-3.1.0.min.js"></script>
    <script src="scripts/gallery.js"></script>
    <script src="http://use.edgefonts.net/source-sans-pro:n4,n9,n7,i7,i4,n3,i3,n6,i6,i9,n2,i2:all.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lightgallery/1.2.21/js/lightgallery-all.min.js"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0">
    <meta name="mobile-web-app-capable" content="yes" />
    <meta name="theme-color" content="#000" />
    <link rel="shortcut icon" type="image/png" href="img/logo.ico" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightgallery/1.2.21/css/lightgallery.min.css">
    <link rel="stylesheet" href="style/style.css">
    <title>WouterMol.com | Gallery</title>
</head>

<body>
    <nav class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#id-collapse-top-nav" aria-expanded="false"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button> <a href="#" class="navbar-brand">WouterMol.com</a> </div>
            <div class="collapse navbar-collapse navbar-right" id="id-collapse-top-nav">
                <ul class="nav navbar-nav">
                    <li><a href="index"><span class="glyphicon glyphicon-home"></span></a></li>
                    <li class="active"><a href="gallery">gallery</a></li>
                    <li><a href="albums">albums</a></li>
                </ul>
            </div>
        </div>
    </nav>
    <section id="main">
        <div class="jumbotron index">
            <div class="container">
                <h1 id="hello-message">Gallery</h1>
                <h3 id="sub-message">portfolio showcase</h3> </div>
        </div>
        <div id="albums" class="container">
            <div class="row">
                <?php 
            
        $cats = array_filter(glob('database/categories/*'), 'is_file');
        $cat = array();
        foreach($cats as $file) {
            $file = pathinfo($file);
            array_push($cat,$file['filename']);
        }
        
        foreach($cat as $catname){
            
            $jsondata = file_get_contents("database/categories/".$catname.".json");
            $json = json_decode($jsondata, true);            
            echo 
            "<div class='col-md-3'>                
                <img src='images/". $json[0]['filename'] ."'>
                <div class='caption'  data-cat='". $catname ."'>
                    <h2>". $catname ."</h2>
                </div>
            </div>";             
        }
        ?> </div>
        </div>
    </section>
    <?php 
        include("footer.php");
    ?>
</body>

</html>