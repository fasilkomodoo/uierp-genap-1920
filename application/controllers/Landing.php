<?php
defined('BASEPATH') or exit('No direct script access allowed');

class Landing extends CI_Controller
{

    public function index()
    {
        if ($this->session->uid) {
            redirect(base_url("/admin"));
        } else {
            $this->output->set_header('Cache-Control: max-age=31536000');
            $this->load->view('landing/login');
        }
    }

    public function logout()
    {
        $this->session->sess_destroy();
        redirect(base_url());
    }
}
