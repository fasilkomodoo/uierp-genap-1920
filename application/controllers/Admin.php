<?php
defined('BASEPATH') or exit('No direct script access allowed');

class Admin extends CI_Controller
{

	public function index()
	{
		$data['page_content'] = $this->load->view('admin/admin', "", true);

		$this->load->view("layout/base", $data);
	}
}
