<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Login - PUR_CHASE</title>
    <!-- Bootstrap core CSS -->
    <link href="<?= base_url("assets/") ?>css/bootstrap.min.css" rel="stylesheet">
    <!-- Material Design Bootstrap -->
    <link href="<?= base_url("assets/") ?>css/mdb.lite.min.css" rel="stylesheet">
</head>

<body class="d-flex justify-content-center align-items-center" style="min-height: 100vh;">

    <form class="card" style="min-width: 400px;" action="<?= base_url("/index.php/api/login") ?>" method="POST">
        <div class="card-header bg-transparent">
            <h1 class="card-title m-0 text-center">
                PUR-CHASE
            </h1>
            <h3 class="card-title m-0 text-center">
                Login
            </h3>
        </div>
        <div class="card-body">
            <div class="md-form">
                <input type="text" id="url" class="form-control" name="url">
                <label for="url">Url</label>
            </div>
            <div class="md-form">
                <input type="text" id="dbname" class="form-control" name="dbname">
                <label for="dbname">Database Name</label>
            </div>
            <div class="md-form">
                <input type="text" id="email" class="form-control" autocomplete="new-password" name="email">
                <label for="email">Email</label>
            </div>
            <div class="md-form">
                <input type="password" id="password" class="form-control" autocomplete="new-password" name="password">
                <label for="password">Password</label>
            </div>
        </div>
        <div class="card-footer text-center bg-transparent">
            <button type="submi" class="btn btn-primary btn-sm">
                Connect
            </button>
        </div>
    </form>


    <!-- SCRIPTS -->
    <!-- JQuery -->
    <script type="text/javascript" src="<?= base_url("assets/") ?>js/jquery-3.4.1.min.js"></script>
    <!-- Bootstrap core JavaScript -->
    <script type="text/javascript" src="<?= base_url("assets/") ?>js/bootstrap.min.js"></script>
    <!-- MDB core JavaScript -->
    <script type="text/javascript" src="<?= base_url("assets/") ?>js/mdb.min.js"></script>

    <script src="/pur_chase/upup.min.js"></script>
    <script>
        UpUp.start({
            'content-url': 'offline.html'
        });
    </script>
</body>

</html>