<?php
defined('BASEPATH') or exit('No direct script access allowed');

class Supplier extends CI_Controller
{

    public function index()
    {
        $data['page_content'] = $this->load->view('supplier/index', "", true);
        $data['page_js'] = $this->load->view('supplier/index_js', "", true);

        $this->load->view("layout/base", $data);
    }
}
