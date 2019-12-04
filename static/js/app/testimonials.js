// fields
// Testimonial 1
let inputTestimonialName_1 = $("#inputTestimonialName_1");
let textareaTestimonialTextEN_1 = $("#textareaTestimonialTextEN_1");
let textareaTestimonialTextES_1 = $("#textareaTestimonialTextES_1");
// Testimonial 2
let inputTestimonialName_2 = $("#inputTestimonialName_2");
let textareaTestimonialTextEN_2 = $("#textareaTestimonialTextEN_2");
let textareaTestimonialTextES_2 = $("#textareaTestimonialTextES_2");
// Testimonial 3
let inputTestimonialName_3 = $("#inputTestimonialName_3");
let textareaTestimonialTextEN_3 = $("#textareaTestimonialTextEN_3");
let textareaTestimonialTextES_3 = $("#textareaTestimonialTextES_3");
// Testimonial 4
let inputTestimonialName_4 = $("#inputTestimonialName_4");
let textareaTestimonialTextEN_4 = $("#textareaTestimonialTextEN_4");
let textareaTestimonialTextES_4 = $("#textareaTestimonialTextES_4");


let TESTIMONIALS = {

    name: 'TESTIMONIALS',

    submit: function (elem) {

        // testimonial 1
        let testimonialname_1 = inputTestimonialName_1.val();
        let testimonialtextEN_1 = textareaTestimonialTextEN_1.val();
        let testimonialtextES_1 = textareaTestimonialTextES_1.val();

        // testimonial 2
        let testimonialname_2 = inputTestimonialName_2.val();
        let testimonialtextEN_2 = textareaTestimonialTextEN_2.val();
        let testimonialtextES_2 = textareaTestimonialTextES_2.val();

        // testimonial 3
        let testimonialname_3 = inputTestimonialName_3.val();
        let testimonialtextEN_3 = textareaTestimonialTextEN_3.val();
        let testimonialtextES_3 = textareaTestimonialTextES_3.val();

        // testimonial 4
        let testimonialname_4 = inputTestimonialName_4.val();
        let testimonialtextEN_4 = textareaTestimonialTextEN_4.val();
        let testimonialtextES_4 = textareaTestimonialTextES_4.val();

        // testimonial 1
        if (!testimonialname_1){
            alertify.error('Name in Testimonial 1 is required');
            inputTestimonialName_1.addClass('is-invalid');
            return false;
        }

        else if (!testimonialtextEN_1){
            alertify.error('Testimonial 1 (EN) is required');
            textareaTestimonialTextEN_1.addClass('is-invalid');
            return false;
        }

        else if (!testimonialtextES_1){
            alertify.error('Testimonial 1 (ES) is required');
            textareaTestimonialTextES_1.addClass('is-invalid');
            return false;
        }

        // testimonial 2
        if (!testimonialname_2){
            alertify.error('Name in Testimonial 2 is required');
            inputTestimonialName_2.addClass('is-invalid');
            return false;
        }

        else if (!testimonialtextEN_2){
            alertify.error('Testimonial 2 (EN) is required');
            textareaTestimonialTextEN_2.addClass('is-invalid');
            return false;
        }

        else if (!testimonialtextES_2){
            alertify.error('Testimonial 2 (ES) is required');
            textareaTestimonialTextES_2.addClass('is-invalid');
            return false;
        }

        // testimonial 3
        if (!testimonialname_3){
            alertify.error('Name in Testimonial 3 is required');
            inputTestimonialName_3.addClass('is-invalid');
            return false;
        }

        else if (!testimonialtextEN_3){
            alertify.error('Testimonial 3 (EN) is required');
            textareaTestimonialTextEN_3.addClass('is-invalid');
            return false;
        }

        else if (!testimonialtextES_3){
            alertify.error('Testimonial 3 (ES) is required');
            textareaTestimonialTextES_3.addClass('is-invalid');
            return false;
        }

        else{

            let formData = new FormData();
            // testimonial 1
            formData.append('testimonialname_1', testimonialname_1);
            formData.append('testimonialtext_1_en', testimonialtextEN_1);
            formData.append('testimonialtext_1_es', testimonialtextES_1);
            // testimonial 2
            formData.append('testimonialname_2', testimonialname_2);
            formData.append('testimonialtext_2_en', testimonialtextEN_2);
            formData.append('testimonialtext_2_es', testimonialtextES_2);
            // testimonial 3
            formData.append('testimonialname_3', testimonialname_3);
            formData.append('testimonialtext_3_en', testimonialtextEN_3);
            formData.append('testimonialtext_3_es', testimonialtextES_3);
            // testimonial 4
            formData.append('testimonialname_4', testimonialname_4);
            formData.append('testimonialtext_4_en', testimonialtextEN_4);
            formData.append('testimonialtext_4_es', testimonialtextES_4);

            let spinnerText = "<i class='fa fa-circle-o-notch fa-spin'></i> Saving ...";
            let originalText = elem.html();

            // send to server
            $.ajax({
                type: "POST",
                url: '/administration/website/testimonials',
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

    update_avatar: function (elem, tid) {

        let formData = new FormData();
        formData.append('file', elem[0].files[0]);

        $.ajax({
            url: '/administration/website/testimonials/'+tid+'/update_avatar',
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
