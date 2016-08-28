<?php 

?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <base href="//localhost/projects/WouterMol/" />
    <script src="https://code.jquery.com/jquery-3.1.0.min.js"></script>
    <script src="http://use.edgefonts.net/basic:n4:all.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0">
    <meta name="mobile-web-app-capable" content="yes" />
    <meta name="theme-color" content="#000" />
    <link rel="shortcut icon" type="image/png" href="img/logo.ico" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
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
                    <!-- change in production!! -->
                    <li><a href="../WouterMol">home</a></li>
                    <li class="active"><a href="">gallery</a></li>
                </ul>
            </div>
        </div>
    </nav>
    <section id="main">
        <div class="jumbotron">
            <div class="container">
                <h1 id="hello-message">Gallery</h1>
                <h3 id="sub-message">portfolio showcase</h3> </div>
        </div>
        <div class="categories container">
            <div class="container">
            <ul class="nav navbar-nav test">
                <li><a href="gallery/all/all/new">all</a></li>
                
                <li><a href="">new to old old to new</a></li>
            </ul>
            </div>
        </div>
        <div class="container images">
            <div class="row">
                <?php 
                    echo $_GET['category'] . ' / ' . $_GET['location'] . ' / ' . $_GET['sort'];
                ?>
            </div>
        </div>
    </section>
    
    <div class="image-viewer">
        
        <img class="enlarged-image" src="">
        <div class="carousel navbar-fixed-bottom">
            <ul>
            </ul>
        </div>
        <button class="btn btn-danger btn-close">x</button>
    </div>
    
    <footer></footer>
    
    <script src="scripts/gallery.js"></script>
</body>

</html>