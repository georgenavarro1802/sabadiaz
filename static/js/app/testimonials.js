// fields
// Testimonial 1
let inputTestimonialName_1 = $("#inputTestimonialName_1");
let textareaTestimonialText_1 = $("#textareaTestimonialText_1");
// Testimonial 2
let inputTestimonialName_2 = $("#inputTestimonialName_2");
let textareaTestimonialText_2 = $("#textareaTestimonialText_2");
// Testimonial 3
let inputTestimonialName_3 = $("#inputTestimonialName_3");
let textareaTestimonialText_3 = $("#textareaTestimonialText_3");
// Testimonial 4
let inputTestimonialName_4 = $("#inputTestimonialName_4");
let textareaTestimonialText_4 = $("#textareaTestimonialText_4");


let TESTIMONIALS = {

    name: 'TESTIMONIALS',

    submit: function (elem) {

        // testimonial 1
        let testimonialname_1 = inputTestimonialName_1.val();
        let testimonialtext_1 = textareaTestimonialText_1.val();

        // testimonial 2
        let testimonialname_2 = inputTestimonialName_2.val();
        let testimonialtext_2 = textareaTestimonialText_2.val();

        // testimonial 3
        let testimonialname_3 = inputTestimonialName_3.val();
        let testimonialtext_3 = textareaTestimonialText_3.val();

        // testimonial 4
        let testimonialname_4 = inputTestimonialName_4.val();
        let testimonialtext_4 = textareaTestimonialText_4.val();

        if (testimonialname_1 && testimonialtext_1 && testimonialname_2 && testimonialtext_2 &&
            testimonialname_3 && testimonialtext_3 && testimonialname_4 && testimonialtext_4){

            let formData = new FormData();
            // testimonial 1
            formData.append('testimonialname_1', testimonialname_1);
            formData.append('testimonialtext_1', testimonialtext_1);
            // testimonial 2
            formData.append('testimonialname_2', testimonialname_2);
            formData.append('testimonialtext_2', testimonialtext_2);
            // testimonial 3
            formData.append('testimonialname_3', testimonialname_3);
            formData.append('testimonialtext_3', testimonialtext_3);
            // testimonial 4
            formData.append('testimonialname_4', testimonialname_4);
            formData.append('testimonialtext_4', testimonialtext_4);

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

        }else{
            alertify.error('Missing required fields');
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
