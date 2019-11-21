// fields
let inputTitle = $("#inputTitle");
let inputDescription = $("#inputDescription");
let selectCategory = $("#selectCategory");
let selectGender = $("#selectGender");
let inputPrice = $("#inputPrice");
let inputVPrice = $("#inputVPrice");
let inputStock = $("#inputStock");
let inputDiscount = $("#inputDiscount");
let textareaInformation = $("#textareaInformation");
let checkboxIsNew = $("#checkboxIsNew");

let inputFiles = $("#inputFiles");


let PRODUCTS = {

    name: 'PRODUCTS',

    submit: function (elem, pid) {
        // pid = 0 -> Create
        // pid > 0 -> Edit

        let url = '/administration/products/create';
        if (pid){
            url = 'administration/products/'+pid+'/edit';
        }

        // required fields
        let title = inputTitle.val();
        let description = inputDescription.val();
        let category_id = selectCategory.val();
        let gender = selectGender.val();
        let price = parseFloat(inputPrice.val());

        // optional fields
        let stock = inputStock.val();
        let discount = inputDiscount.val();
        let vprice = inputVPrice.val();
        let information = textareaInformation.val();
        let isnew = checkboxIsNew.val();

        let formData = new FormData();
        formData.append('title', title);
        formData.append('description', description);
        formData.append('category_id', category_id);
        formData.append('gender', gender);
        formData.append('price', price);
        formData.append('stock', stock);
        formData.append('discount', discount);
        formData.append('vprice', vprice);
        formData.append('information', information);
        formData.append('isnew', isnew);

        $.each(inputFiles[0].files, function(i, file) {
            formData.append('file['+i+']', file);
        });

        if (title && description && category_id && gender && price > 0){
            let spinnerText = "<i class='fa fa-circle-o-notch fa-spin'></i> Saving ...";
            let originalText = elem.html();

            // send to server
            $.ajax({
                type: "POST",
                url: url,
                data: formData,
                dataType: 'json',
                processData: false,
                contentType: false,
                beforeSend: function () {
                    elem.addClass('disabled').html(spinnerText);
                },
                success: function (response) {
                    if (response.result === 'ok'){

                        Swal.fire(
                            'Good job!',
                            response.message,
                            'success'
                        ).then((result) => {
                            if (result.value) {
                                location.href = response.redirect_url;
                            }
                        });

                    }else{
                        alertify.error(response.message);
                    }
                },
                complete: function () {
                    elem.removeClass('disabled').html(originalText);
                },
                error: function (response) {
                    elem.removeClass('disabled').html(originalText);
                    alertify.error('Server Error');
                },
            });
        }else{
            alertify.error('Missing required fields');
        }

    },

    delete: function (elem, pid) {

        Swal.fire({
            title: 'Are you sure?',
            text: "You won't be able to revert this!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#d33',
            cancelButtonColor: '#3085d6',
            confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
            if (result.value) {

                $.ajax({
                    type: "POST",
                    url: '/administration/products/'+pid+'/delete',
                    data: {},
                    dataType: 'json',
                    processData: false,
                    contentType: false,
                    success: function (response) {
                        if (response.result === 'ok'){

                            Swal.fire(
                                'Deleted!',
                                response.message,
                                'success'
                            ).then((result) => {
                                if (result.value) {
                                    location.href = response.redirect_url;
                                }
                            });

                        }else{
                            alertify.error(response.message);
                        }
                    },
                    error: function (response) {
                        alertify.error('Server Error');
                    },
                });
            }
        })

    }

};

