// fields
// slide 1
let inputHomeSliderText1_1 = $("#inputHomeSliderText1_1");
let inputHomeSliderText2_1 = $("#inputHomeSliderText2_1");
let inputHomeSliderDescription_1 = $("#inputHomeSliderDescription_1");
// slide 2
let inputHomeSliderText1_2 = $("#inputHomeSliderText1_2");
let inputHomeSliderText2_2 = $("#inputHomeSliderText2_2");
let inputHomeSliderDescription_2 = $("#inputHomeSliderDescription_2");
// slide 3
let inputHomeSliderText1_3 = $("#inputHomeSliderText1_3");
let inputHomeSliderText2_3 = $("#inputHomeSliderText2_3");
let inputHomeSliderDescription_3 = $("#inputHomeSliderDescription_3");

// // edit images
// let uploadImage_1 = $("#uploadImage_1");
// let uploadImage_2 = $("#uploadImage_2");
// let uploadImage_3 = $("#uploadImage_3");


let WEBSITE = {

    name: 'WEBSITE',

    submit_home_sliders: function (elem) {

        let dataOK = false;

        // slide 1
        let inputHomeSliderText1_1 = inputHomeSliderText1_1.val();
        let inputHomeSliderText2_1 = inputHomeSliderText2_1.val();
        let inputHomeSliderDescription_1 = inputHomeSliderDescription_1.val();
        // slide 2
        let inputHomeSliderText1_2 = inputHomeSliderText1_2.val();
        let inputHomeSliderText2_2 = inputHomeSliderText2_2.val();
        let inputHomeSliderDescription_2 = inputHomeSliderDescription_2.val();
        // slide 3
        let inputHomeSliderText1_3 = inputHomeSliderText1_3.val();
        let inputHomeSliderText2_3 = inputHomeSliderText2_3.val();
        let inputHomeSliderDescription_3 = inputHomeSliderDescription_3.val();

        if (inputHomeSliderText1_1 && inputHomeSliderText2_1 && inputHomeSliderDescription_1 &&
            inputHomeSliderText1_2 && inputHomeSliderText2_2 && inputHomeSliderDescription_2 &&
            inputHomeSliderText1_3 && inputHomeSliderText2_3 && inputHomeSliderDescription_3){
            dataOK = true;
        }

        if (dataOK){
            let formData = new FormData();
            // slide 1
            formData.append('text1_1', inputHomeSliderText1_1);
            formData.append('text2_1', inputHomeSliderText2_1);
            formData.append('desc_1', inputHomeSliderDescription_1);
            // slide 2
            formData.append('text1_2', inputHomeSliderText1_2);
            formData.append('text2_2', inputHomeSliderText2_2);
            formData.append('desc_2', inputHomeSliderDescription_2);
            // slide 3
            formData.append('text1_3', inputHomeSliderText1_3);
            formData.append('text2_3', inputHomeSliderText2_3);
            formData.append('desc_3', inputHomeSliderDescription_3);

            // $.each(inputFiles[0].files, function(i, file) {
            //     formData.append('file['+i+']', file);
            // });

            let spinnerText = "<i class='fa fa-circle-o-notch fa-spin'></i> Saving ...";
            let originalText = elem.html();

            // send to server
            $.ajax({
                type: "POST",
                url: '/administration/website/home_sliders',
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

};
