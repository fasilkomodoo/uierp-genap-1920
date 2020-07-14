<div class="card">
    <div class="card-header bg-white mb-3">
        <div class="d-flex justify-content-between align-items-center flex-row">
            <h2 class="card-title m-0">
                List of Suppliers
            </h2>
            <button class="btn btn-primary" data-toggle="modal" data-target="#add_supplier_modal">
                Add Supplier
            </button>
        </div>
    </div>
    <div class="card-body">
        <div class="table-repsonsive">
            <table class="table table-hover">
                <thead>
                    <th width="1">No</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Website</th>
                </thead>
                <tbody>
                    <tr>
                        <td colspan="2">
                            Please wait... this might take a while
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>




<div class="modal fade" id="add_supplier_modal" tabindex="-1" role="dialog" aria-labelledby="supplier_add_modal_title" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
            <div class="modal-header border-0">
                <h5 class="modal-title" id="supplier_add_modal_title">Add New Supplier</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body container">
                <div class="md-form">
                    <input type="text" id="add_name" class="form-control" required>
                    <label for="add_name">Name</label>
                </div>
                <div class="md-form">
                    <input type="email" id="add_email" class="form-control" required>
                    <label for="add_email">Email</label>
                </div>
                <div class="md-form">
                    <input type="text" id="add_website" class="form-control" required>
                    <label for="add_website">Website</label>
                </div>
            </div>
            <div class="modal-footer d-flex justify-content-center border-0">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" onclick="submit_new()">Save</button>
            </div>
        </div>
    </div>
</div>