// form
let formProduct = $("#formProduct");

// fields
let inputTitleEN = $("#inputTitleEN");
let inputTitleES = $("#inputTitleES");
let inputDescriptionEN = $("#inputDescriptionEN");
let inputDescriptionES = $("#inputDescriptionES");
let selectCategory = $("#selectCategory");
let selectGender = $("#selectGender");
let selectMaterial = $("#selectMaterial");
let inputPrice = $("#inputPrice");
let inputVPrice = $("#inputVPrice");
let inputStock = $("#inputStock");
let inputDiscount = $("#inputDiscount");
let inputFiles = $("#inputFiles");
let checkboxIsNew = $("#checkboxIsNew");
let checkboxIsFeatured = $("#checkboxIsFeatured");
let checkboxIsBestSeller = $("#checkboxIsBestSeller");

// edit images
let uploadImage_1 = $("#uploadImage_1");
let uploadImage_2 = $("#uploadImage_2");
let uploadImage_3 = $("#uploadImage_3");
let uploadImage_4 = $("#uploadImage_4");
let uploadImage_5 = $("#uploadImage_5");
let uploadImage_6 = $("#uploadImage_6");


let PRODUCTS = {

    name: 'PRODUCTS',

    submit: function (elem, pid) {
        // pid = 0 -> Create
        // pid > 0 -> Edit

        formProduct.find('input').removeClass('is-invalid');

        let url = '/administration/products/create';
        if (pid){
            url = '/administration/products/'+pid+'/edit';
        }

        // required fields
        let title_en = inputTitleEN.val();
        let description_en = inputDescriptionEN.val();
        let title_es = inputTitleES.val();
        let description_es = inputDescriptionES.val();
        let category_id = selectCategory.val();
        let gender_id = selectGender.val();
        let material_id = selectMaterial.val();
        let price = parseFloat(inputPrice.val());

        // optional fields
        let stock = inputStock.val();
        let discount = inputDiscount.val();
        let vprice = inputVPrice.val();
        let is_new = checkboxIsNew.is(':checked');
        let is_featured = checkboxIsFeatured.is(':checked');
        let is_bestseller = checkboxIsBestSeller.is(':checked');

        // validations
        if (!title_en){
            alertify.error('Title (EN) is required');
            inputTitleEN.addClass('is-invalid');
            return false;
        }

        else if (!title_es){
            alertify.error('Title (ES) is required');
            inputTitleES.addClass('is-invalid');
            return false;
        }

        else if (!description_en){
            alertify.error('Description (EN) is required');
            inputDescriptionEN.addClass('is-invalid');
            return false;
        }

        else if (!description_es){
            alertify.error('Description (ES) is required');
            inputDescriptionES.addClass('is-invalid');
            return false;
        }

        else if (!price){
            alertify.error('Price has to be greater than zero');
            inputPrice.addClass('is-invalid');
            return false;
        }

        else{

            let formData = new FormData();
            formData.append('title_en', title_en);
            formData.append('description_en', description_en);
            formData.append('title_es', title_es);
            formData.append('description_es', description_es);
            formData.append('category_id', category_id);
            formData.append('material_id', material_id);
            formData.append('gender_id', gender_id);
            formData.append('price', price.toString());
            formData.append('stock', stock);
            formData.append('discount', discount);
            formData.append('vprice', vprice);
            formData.append('is_new', is_new);
            formData.append('is_featured', is_featured);
            formData.append('is_bestseller', is_bestseller);

            if (!pid){
                $.each(inputFiles[0].files, function(i, file) {
                    formData.append('file['+i+']', file);
                });
            }

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
                    error: function () {
                        alertify.error('Server Error');
                    },
                });
            }
        })

    },

    remove_image: function (iid, pid) {

        Swal.fire({
            title: 'Are you sure to delete this image?',
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
                    url: '/administration/products/'+pid+'/images/'+iid+'/delete',
                    data: {},
                    dataType: 'json',
                    success: function (response) {
                        if (response.result === 'ok'){

                            Swal.fire(
                                'Image Deleted!',
                                response.message,
                                'success'
                            ).then((result) => {
                                if (result.value) {
                                    location.reload();
                                }
                            });

                        }else{
                            alertify.error(response.message);
                        }
                    },
                    error: function () {
                        alertify.error('Server Error');
                    },
                });
            }
        })

    },

    update_image: function (iid, pid) {

        let formData = new FormData();
        if (iid === '1'){
            formData.append('file', uploadImage_1[0].files[0]);
        }
        else if (iid === '2'){
            formData.append('file', uploadImage_2[0].files[0]);
        }
        else if (iid === '3'){
            formData.append('file', uploadImage_3[0].files[0]);
        }
        else if (iid === '4'){
            formData.append('file', uploadImage_4[0].files[0]);
        }
        else if (iid === '5'){
            formData.append('file', uploadImage_5[0].files[0]);
        }
        else if (iid === '6'){
            formData.append('file', uploadImage_6[0].files[0]);
        }

        $.ajax({
            url: '/administration/products/'+pid+'/images/'+iid+'/edit',
            type: 'POST',
            data: formData,
            dataType: 'json',
            processData: false,
            contentType: false,
            success: function (response) {
                if (response.result === 'ok'){
                    alertify.success(response.message);
                    location.reload();
                }else{
                    alertify.error(response.message);
                }
            },
            error: function (response) {
                alertify.error('Server Error');
            },
        });

    }

};
