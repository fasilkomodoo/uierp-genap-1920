<?php
defined('BASEPATH') or exit('No direct script access allowed');

class Api extends CI_Controller
{

    public function __construct()
    {
        parent::__construct();
        header('Content-Type: application/json');
        header('Access-Control-Allow-Origin: *');
        header("Access-Control-Allow-Headers: X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Request-Method");
        header("Access-Control-Allow-Methods: GET, POST, OPTIONS, PUT, DELETE");
        $this->load->library("ripcord");
    }

    public function login()
    {
        if (substr($_POST['url'], -1) != "/") {
            $_POST['url'] = $_POST['url'] . "/";
        }
        $common = $this->ripcord->client($_POST['url'] . 'xmlrpc/2/common');
        $uid = $common->authenticate($_POST['dbname'], $_POST['email'], $_POST['password'], array());

        if ($uid) {
            $this->session->set_userdata(array(
                "dbname" => $_POST['dbname'],
                "uid" => $uid,
                "password" => $_POST['password'],
                "url" => $_POST['url']
            ));
            redirect(base_url("/index.php/admin"));
        } else {
            $this->session->set_flashdata("error", "wrong credentials");
        }
    }

    public function get_supplier()
    {
        $models = $this->ripcord->client($this->session->url . "xmlrpc/2/object");
        $ids = $models->execute_kw(
            $this->session->dbname,
            $this->session->uid,
            $this->session->password,
            'res.partner',
            'search',
            array(
                array(
                    array('supplier', '=', true)
                )
            )
        );

        $records = $models->execute_kw(
            $this->session->dbname,
            $this->session->uid,
            $this->session->password,
            'res.partner',
            'read',
            array($ids)
        );

        echo json_encode($records);
    }

    public function insert_supplier()
    {
        $models = $this->ripcord->client($this->session->url . "xmlrpc/2/object");

        $idnew = $models->execute_kw(
            $this->session->dbname,
            $this->session->uid,
            $this->session->password,
            'res.partner',
            'create',
            array(
                array(
                    'name' => $_POST['name'],
                    'email' => $_POST['email'],
                    'website' => $_POST['website'],
                    "supplier" => true
                )
            )
        );

        echo json_encode(array("msg" => $_POST['name'] . " registered successfully"));
    }
}
