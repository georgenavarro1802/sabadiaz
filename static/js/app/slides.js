// form
let formSlides = $("#formSlides");

// slide 1
let inputHomeSliderText1EN_1 = $("#inputHomeSliderText1EN_1");
let inputHomeSliderText2EN_1 = $("#inputHomeSliderText2EN_1");
let inputHomeSliderDescriptionEN_1 = $("#inputHomeSliderDescriptionEN_1");

let inputHomeSliderText1ES_1 = $("#inputHomeSliderText1ES_1");
let inputHomeSliderText2ES_1 = $("#inputHomeSliderText2ES_1");
let inputHomeSliderDescriptionES_1 = $("#inputHomeSliderDescriptionES_1");

// slide 2
let inputHomeSliderText1EN_2 = $("#inputHomeSliderText1EN_2");
let inputHomeSliderText2EN_2 = $("#inputHomeSliderText2EN_2");
let inputHomeSliderDescriptionEN_2 = $("#inputHomeSliderDescriptionEN_2");

let inputHomeSliderText1ES_2 = $("#inputHomeSliderText1ES_2");
let inputHomeSliderText2ES_2 = $("#inputHomeSliderText2ES_2");
let inputHomeSliderDescriptionES_2 = $("#inputHomeSliderDescriptionES_2");

// slide 3
let inputHomeSliderText1EN_3 = $("#inputHomeSliderText1EN_3");
let inputHomeSliderText2EN_3 = $("#inputHomeSliderText2EN_3");
let inputHomeSliderDescriptionEN_3 = $("#inputHomeSliderDescriptionEN_3");

let inputHomeSliderText1ES_3 = $("#inputHomeSliderText1ES_3");
let inputHomeSliderText2ES_3 = $("#inputHomeSliderText2ES_3");
let inputHomeSliderDescriptionES_3 = $("#inputHomeSliderDescriptionES_3");


let SLIDES = {

    name: 'SLIDES',

    submit: function (elem) {

        formSlides.find('input').removeClass('is-invalid');

        // slide 1
        let HomeSliderText1EN_1 = inputHomeSliderText1EN_1.val();
        let HomeSliderText2EN_1 = inputHomeSliderText2EN_1.val();
        let HomeSliderDescriptionEN_1 = inputHomeSliderDescriptionEN_1.val();

        let HomeSliderText1ES_1 = inputHomeSliderText1ES_1.val();
        let HomeSliderText2ES_1 = inputHomeSliderText2ES_1.val();
        let HomeSliderDescriptionES_1 = inputHomeSliderDescriptionES_1.val();

        // slide 2
        let HomeSliderText1EN_2 = inputHomeSliderText1EN_2.val();
        let HomeSliderText2EN_2 = inputHomeSliderText2EN_2.val();
        let HomeSliderDescriptionEN_2 = inputHomeSliderDescriptionEN_2.val();

        let HomeSliderText1ES_2 = inputHomeSliderText1ES_2.val();
        let HomeSliderText2ES_2 = inputHomeSliderText2ES_2.val();
        let HomeSliderDescriptionES_2 = inputHomeSliderDescriptionES_2.val();

        // slide 3
        let HomeSliderText1EN_3 = inputHomeSliderText1EN_3.val();
        let HomeSliderText2EN_3 = inputHomeSliderText2EN_3.val();
        let HomeSliderDescriptionEN_3 = inputHomeSliderDescriptionEN_3.val();

        let HomeSliderText1ES_3 = inputHomeSliderText1ES_3.val();
        let HomeSliderText2ES_3 = inputHomeSliderText2ES_3.val();
        let HomeSliderDescriptionES_3 = inputHomeSliderDescriptionES_3.val();

        // slide 1
        if (!HomeSliderText1EN_1){
            alertify.error('Text 1 (EN) in Slide 1 is required');
            inputHomeSliderText1EN_1.addClass('is-invalid');
            return false;
        }

        else if (!HomeSliderText1ES_1){
            alertify.error('Text 1 (ES) in Slide 1 is required');
            inputHomeSliderText1ES_1.addClass('is-invalid');
            return false;
        }

        else if (!HomeSliderText2EN_1){
            alertify.error('Text 2 (EN) in Slide 1 is required');
            inputHomeSliderText2EN_1.addClass('is-invalid');
            return false;
        }

        else if (!HomeSliderText2ES_1){
            alertify.error('Text 2 (ES) in Slide 1 is required');
            inputHomeSliderText2ES_1.addClass('is-invalid');
            return false;
        }

        else if (!HomeSliderDescriptionEN_1){
            alertify.error('Description (EN) in Slide 1 is required');
            inputHomeSliderDescriptionEN_1.addClass('is-invalid');
            return false;
        }

        // slide 2
        else if (!HomeSliderText1EN_2){
            alertify.error('Text 1 (EN) in Slide 2 is required');
            inputHomeSliderText1EN_1.addClass('is-invalid');
            return false;
        }

        else if (!HomeSliderText1ES_2){
            alertify.error('Text 1 (ES) in Slide 2 is required');
            inputHomeSliderText1ES_1.addClass('is-invalid');
            return false;
        }

        else if (!HomeSliderText2EN_2){
            alertify.error('Text 2 (EN) in Slide 2 is required');
            inputHomeSliderText2EN_1.addClass('is-invalid');
            return false;
        }

        else if (!HomeSliderText2ES_2){
            alertify.error('Text 2 (ES) in Slide 2 is required');
            inputHomeSliderText2ES_1.addClass('is-invalid');
            return false;
        }

        else if (!HomeSliderDescriptionEN_2){
            alertify.error('Description (EN) in Slide 2 is required');
            inputHomeSliderDescriptionEN_1.addClass('is-invalid');
            return false;
        }

        // slide 3
        else if (!HomeSliderText1EN_3){
            alertify.error('Text 1 (EN) in Slide 3 is required');
            inputHomeSliderText1EN_1.addClass('is-invalid');
            return false;
        }

        else if (!HomeSliderText1ES_3){
            alertify.error('Text 1 (ES) in Slide 3 is required');
            inputHomeSliderText1ES_1.addClass('is-invalid');
            return false;
        }

        else if (!HomeSliderText2EN_3){
            alertify.error('Text 2 (EN) in Slide 3 is required');
            inputHomeSliderText2EN_1.addClass('is-invalid');
            return false;
        }

        else if (!HomeSliderText2ES_3){
            alertify.error('Text 2 (ES) in Slide 3 is required');
            inputHomeSliderText2ES_1.addClass('is-invalid');
            return false;
        }

        else if (!HomeSliderDescriptionEN_3){
            alertify.error('Description (EN) in Slide 3 is required');
            inputHomeSliderDescriptionEN_1.addClass('is-invalid');
            return false;
        }

        else {

            let formData = new FormData();
            // slide 1
            formData.append('text1_1_en', HomeSliderText1EN_1);
            formData.append('text2_1_en', HomeSliderText2EN_1);
            formData.append('desc_1_en', HomeSliderDescriptionEN_1);
            formData.append('text1_1_es', HomeSliderText1ES_1);
            formData.append('text2_1_es', HomeSliderText2ES_1);
            formData.append('desc_1_es', HomeSliderDescriptionES_1);

            // slide 2
            formData.append('text1_2_en', HomeSliderText1EN_2);
            formData.append('text2_2_en', HomeSliderText2EN_2);
            formData.append('desc_2_en', HomeSliderDescriptionEN_2);
            formData.append('text1_2_es', HomeSliderText1ES_2);
            formData.append('text2_2_es', HomeSliderText2ES_2);
            formData.append('desc_2_es', HomeSliderDescriptionES_2);

            // slide 3
            formData.append('text1_3_en', HomeSliderText1EN_3);
            formData.append('text2_3_en', HomeSliderText2EN_3);
            formData.append('desc_3_en', HomeSliderDescriptionEN_3);
            formData.append('text1_3_es', HomeSliderText1ES_3);
            formData.append('text2_3_es', HomeSliderText2ES_3);
            formData.append('desc_3_es', HomeSliderDescriptionES_3);

            let spinnerText = "<i class='fa fa-circle-o-notch fa-spin'></i> Saving ...";
            let originalText = elem.html();

            // send to server
            $.ajax({
                type: "POST",
                url: '/administration/website/slides',
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
                error: function () {
                    elem.removeClass('disabled').html(originalText);
                    alertify.error('Server Error');
                },
            });
        }

    },

    update_image: function (hsid) {

        let formData = new FormData();
        formData.append('file', $("#inputHomeSlideUploadImage_"+hsid)[0].files[0]);

        $.ajax({
            url: '/administration/website/slides/'+hsid+'/update_image',
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
            error: function () {
                alertify.error('Server Error');
            },
        });

    }

};
