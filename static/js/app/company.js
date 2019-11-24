// fields
// required
let inputCompanyDataName = $("#inputCompanyDataName");
let inputCompanyDataDescription = $("#inputCompanyDataDescription");
let inputCompanyDataAddress = $("#inputCompanyDataAddress");
let inputCompanyDataEmail = $("#inputCompanyDataEmail");
let inputCompanyDataPhone = $("#inputCompanyDataPhone");
// optionals
let inputCompanyDataFacebook = $("#inputCompanyDataFacebook");
let inputCompanyDataTwitter = $("#inputCompanyDataTwitter");
let inputCompanyDataInstagram = $("#inputCompanyDataInstagram");
let inputCompanyDataYoutube = $("#inputCompanyDataYoutube");


let COMPANY = {

    name: 'COMPANY',

    update: function (elem) {

        // required fields
        let c_name = inputCompanyDataName.val();
        let c_description = inputCompanyDataDescription.val();
        let c_address = inputCompanyDataAddress.val();
        let c_email = inputCompanyDataEmail.val();
        let c_phone = inputCompanyDataPhone.val();
        // optional
        let c_facebook = inputCompanyDataFacebook.val();
        let c_twitter = inputCompanyDataTwitter.val();
        let c_instagram = inputCompanyDataInstagram.val();
        let c_youtube = inputCompanyDataYoutube.val();

        if (c_name && c_description && c_address && c_email && c_phone){

            let formData = new FormData();
            formData.append('c_name', c_name);
            formData.append('c_description', c_description);
            formData.append('c_address', c_address);
            formData.append('c_email', c_email);
            formData.append('c_phone', c_phone);
            formData.append('c_facebook', c_facebook);
            formData.append('c_twitter', c_twitter);
            formData.append('c_instagram', c_instagram);
            formData.append('c_youtube', c_youtube);

            let spinnerText = "<i class='fa fa-circle-o-notch fa-spin'></i> Saving ...";
            let originalText = elem.html();

            // send to server
            $.ajax({
                type: "POST",
                url: '/administration/website/company/update',
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
                                location.reload();
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

    update_logo: function () {

        let formData = new FormData();
        formData.append('file', $("#inputCompanyDataLogo")[0].files[0]);

        $.ajax({
            url: '/administration/website/company/logo',
            type: 'POST',
            data: formData,
            dataType: 'json',
            processData: false,
            contentType: false,
            success: function (response) {
                if (response.result === 'ok'){
                    alertify.success(response.message);
                    setTimeout(function () {
                      location.reload();
                    }, 600);
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
