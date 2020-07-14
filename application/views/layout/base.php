<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>PUR_CHASE</title>
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.11.2/css/all.css">
    <!-- Bootstrap core CSS -->
    <link href="<?= base_url("assets/") ?>css/bootstrap.min.css" rel="stylesheet">
    <!-- Material Design Bootstrap -->
    <link href="<?= base_url("assets/") ?>css/mdb.min.css" rel="stylesheet">
    <!-- Your custom styles (optional) -->
    <link href="<?= base_url("assets/") ?>css/style.min.css" rel="stylesheet">
    <style>
        .map-container {
            overflow: hidden;
            padding-bottom: 56.25%;
            position: relative;
            height: 0;
        }

        .map-container iframe {
            left: 0;
            top: 0;
            height: 100%;
            width: 100%;
            position: absolute;
        }
    </style>
</head>

<body class="grey lighten-3">

    <!--Main Navigation-->
    <header>

        <!-- Navbar -->
        <nav class="navbar fixed-top navbar-expand-lg navbar-light white scrolling-navbar">
            <div class="container-fluid">

                <!-- Brand -->
                <a class="navbar-brand waves-effect" href="<?= base_url() ?>">
                    <strong class="blue-text">PUR-CHASE</strong>
                </a>

                <!-- Collapse -->
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <!-- Links -->
                <div class="collapse navbar-collapse" id="navbarSupportedContent">

                    <!-- Left -->
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item <?= stripos(current_url(), "admin") ? "active" : "" ?>">
                            <a class="nav-link waves-effect" href="<?= base_url() ?>">
                                Home
                            </a>
                        </li>
                        <li class="nav-item <?= stripos(current_url(), "supplier") ? "active" : "" ?>">
                            <a class="nav-link waves-effect" href="<?= base_url("/index.php/supplier") ?>">
                                Supplier
                            </a>
                        </li>
                    </ul>

                    <!-- Right -->
                    <ul class="navbar-nav nav-flex-icons">
                        <li class="nav-item">
                            <a href="<?= base_url("/landing/logout") ?>" class="text-danger nav-link border border-light rounded waves-effect">
                                <i class="fa fa-power-off mr-2"></i> Logout
                            </a>
                        </li>
                    </ul>

                </div>

            </div>
        </nav>
        <!-- Navbar -->

        <!-- Sidebar -->
        <div class="sidebar-fixed position-fixed">

            <a href="<?= base_url() ?>" class="logo-wrapper waves-effect">
                <span class="h4">
                    PUR_CHASE
                </span>
            </a>

            <div class="list-group list-group-flush">
                <a href="<?= base_url() ?>" class="list-group-item list-group-item-action waves-effect <?= stripos(current_url(), "admin") ? "active" : "" ?>">
                    <i class="fas fa-home mr-3"></i>Home
                </a>
                <a href="<?= base_url("/index.php/supplier") ?>" class="list-group-item list-group-item-action waves-effect <?= stripos(current_url(), "supplier") ? "active" : "" ?>">
                    <i class="fas fa-users mr-3"></i>Supplier
                </a>
            </div>

        </div>
        <!-- Sidebar -->

    </header>
    <!--Main Navigation-->

    <!--Main layout-->
    <main class="pt-5 mx-lg-5">
        <div class="container-fluid mt-5">
            <?= $page_content ?>
        </div>
    </main>
    <!--Main layout-->

    <!-- SCRIPTS -->
    <!-- JQuery -->
    <script type="text/javascript" src="<?= base_url("assets/") ?>js/jquery-3.4.1.min.js"></script>
    <!-- Bootstrap tooltips -->
    <script type="text/javascript" src="<?= base_url("assets/") ?>js/popper.min.js"></script>
    <!-- Bootstrap core JavaScript -->
    <script type="text/javascript" src="<?= base_url("assets/") ?>js/bootstrap.min.js"></script>
    <!-- MDB core JavaScript -->
    <script type="text/javascript" src="<?= base_url("assets/") ?>js/mdb.min.js"></script>
    <!-- Initializations -->
    <script type="text/javascript">
        // Animations initialization
        new WOW().init();
    </script>

    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>

    <script src="/upup.sw.min.js"></script>
    <script>
        UpUp.start({
            'content': '<html><body><h1>Top Hotels in Rome</h1><p>Villa Domus</p><p>Hotel Trivelli</p></body></html>'
        });
    </script>

    <?= isset($page_js) ? $page_js : "" ?>
</body>

</html>