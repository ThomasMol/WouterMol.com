<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <base href="//192.168.2.86/projects/WouterMol/"/>
    <script src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
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
            <h3 id="sub-message">portfolio</h3>
        </div>
    </div>
    
    <div class="container-fluid categories">
    <ul class="nav navbar-nav">
        <li><a href="gallery/All">All</a></li>
        <?php 
            $dirs = array_filter(glob('images/*'), 'is_dir');
            
            foreach($dirs as $dir){
                $dir = str_replace('images/','',$dir);
                echo "<li><a href='gallery/" . $dir . "'>" . $dir . "</a></li>";
            }
            
            ?>  
    </ol>
    </div>          
    <div class="container images">
    <div class="row">
        <?php 
        
        $category = $_GET['category'];
        
        if(strpos($category, 'All') !== false){
            
            $dirs = array_filter(glob('images/*'), 'is_dir');
            
            foreach($dirs as $dir){
                $imgs = array_filter(glob($dir . '/*'), 'is_file');
                foreach($imgs as $img){
                    echo "<div class='col-md-4'><img src='" . $img . "'></div>";
                }
            }
            
        }else{
            $imgs = array_filter(glob('images/' . $category . '/*'), 'is_file');
            foreach($imgs as $img){
                echo "<div class='col-md-4'><img src='" . $img . "'></div>";
            }
        }
        
        ?>
    </div>
    </div>
    
    </section>

    <footer>
    </footer>
    
</body>
</html>
