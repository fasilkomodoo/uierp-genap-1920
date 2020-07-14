<script>
    function reload_suppliers() {
        $.ajax({
            url: "<?= base_url("/index.php/api/get_supplier") ?>",
            method: "get",
            success: function(response) {
                $("tbody").empty();
                for (let i = 0; i < response.length; i++) {
                    $("tbody").append(
                        $(document.createElement("tr")).append(
                            $(document.createElement("td")).text(i + 1),
                            $(document.createElement("td")).text(response[i].display_name),
                            $(document.createElement("td")).text(response[i].email),
                            $(document.createElement("td")).text(response[i].website ? response[i].website : "-"),
                        )
                    )
                }
            }
        });
    }

    $(document).ready(function() {
        reload_suppliers();
    })

    function submit_new() {
        swal({
            text: "Sending New Supplier to Odoo",
            buttons: false
        });
        if ($("#add_name").val() && $("#add_email").val()) {
            $.ajax({
                url: "<?= base_url("/index.php/api/insert_supplier") ?>",
                method: "post",
                data: {
                    "name": $("#add_name").val(),
                    "email": $("#add_email").val(),
                    "website": $("#add_website").val()
                },
                success: function(response) {
                    swal("Success!", response.msg, "success").then((value) => {
                        $("#add_supplier_modal").modal('hide');
                        swal("Warning!", "Updating local table", "warning");
                        reload_suppliers();
                    });;
                }
            })
        } else {
            swal("Warning!", "Please make sure email and name fields are valid", "warning")
        }
    }
</script>