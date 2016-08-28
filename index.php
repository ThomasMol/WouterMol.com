<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
<!--    <base href="//localhost/projects/WouterMol/"/>-->
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
                    <li class="active"><a href="home"><span class="glyphicon glyphicon-home"></span></a></li>
                    <li><a href="gallery/All">gallery</a></li>
                    <li><a href="gallery/All">albums</a></li>
                </ul>
            </div>
        </div>        
    </nav>

    <section id="main">
    <div class="jumbotron index">
        <div class="container">
            <h1 id="hello-message">Wouter Mol</h1>
            <h2 id="sub-message">Photography</h2>
        </div>
    </div>
        
    
    </section>

    <footer>
    </footer>
    <script>
    $(".jumbotron").css("height", $(window).height() * 0.6);
    </script>
</body>
</html>
