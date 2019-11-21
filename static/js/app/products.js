// ref https://github.com/promosis/file-upload-with-preview
let upload = new FileUploadWithPreview('divUploadID');

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


let PRODUCTS = {

    name: 'PRODUCTS',

    submit: function(elem, pid) {
        // pid = 0 -> Create
        // pid > 0 -> Edit

        let url = '/administration/products/create';
        if (pid){
            url = 'administration/products/'+pid+'/edit';
        }

        if (inputTitle.val() && inputDescription.val()){
            let spinnerText = "<i class='fa fa-circle-o-notch fa-spin'></i>";
            let originalText = elem.html();

            // define alertify
            alertify.set('notifier','position', 'top-right');

            // send to server
            $.ajax({
                type: "POST",
                url: url,
                data: {
                    'title': inputTitle.val(),
                    'description': inputDescription.val()
                },
                dataType: 'json',
                beforeSend: function () {
                    elem.css("pointer-events", "none").attr("disabled", true).html(spinnerText);
                },
                success: function (response) {
                    if (response.result === 'ok'){

                        // succes message
                        alertify.success(response.message);

                        // // reload
                        // setTimeout(function () {
                        //     location.href = response.redirect_url;
                        // }, 500);

                    }else{
                        elem.css("pointer-events", "auto").attr("disabled", false).html(originalText);
                        alertify.error(response.message);
                    }
                },
                complete: function () {
                    elem.css("pointer-events", "auto").attr("disabled", false).html(originalText);
                },
                error: function (response) {
                    elem.css("pointer-events", "auto").attr("disabled", false).html(originalText);
                    alertify.error(response.message);
                },
            });
        }

    }

};


