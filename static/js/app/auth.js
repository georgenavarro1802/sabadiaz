// Login vars
let login_email = $("#inputLoginEmail");
let login_password = $("#inputLoginPassword");

// Register vars
let register_firstname = $("#inputRegisterFirstName");
let register_lastname = $("#inputRegisterLastName");
let register_email = $("#inputRegisterEmail");
let register_password1 = $("#inputRegisterPassword1");
let register_password2 = $("#inputRegisterPassword2");


let AUTHENTICATION = {

    name: 'AUTHENTICATION',

    login: function() {

        if (login_email.val() && login_password.val()){

            // define alertify
            alertify.set('notifier','position', 'top-right');

            // send to server
            $.ajax({
                type: "POST",
                url: "/login",
                data: {
                    'email': login_email.val(),
                    'password': login_password.val()
                },
                dataType: 'json',
                success: function (response) {
                    if (response.result === 'ok'){

                        // succes message
                        alertify.success(response.message);

                        // reload
                        setTimeout(function () {
                            location.href = response.redirect_url;
                        }, 500);
                    }else{
                        alertify.error(response.message);
                    }
                },
                error: function (response) {
                    alertify.error(response.message);
                },
            });
        }

    },

    register: function() {

        // define alertify
        alertify.set('notifier','position', 'top-right');

        if (register_firstname.val() && register_lastname.val() && register_email.val() && register_password1.val() && register_password2.val() ){

            if (register_password1.val() !== register_password2.val()){
                alertify.error('Passwords do not match');
            } else{
                // send to server
                $.ajax({
                    type: "POST",
                    url: "/register",
                    data: {
                        'first_name': register_firstname.val(),
                        'last_name': register_lastname.val(),
                        'email': register_email.val(),
                        'password1': register_password1.val(),
                        'password2': register_password2.val(),
                    },
                    dataType: 'json',
                    beforeSend: function () {

                    },
                    success: function (response) {
                        if (response.result === 'ok'){

                            // succes message
                            alertify.success(response.message);

                            // reload
                            setTimeout(function () {
                                location.href = response.redirect_url;
                            }, 500);
                        }
                    },
                    error: function (response) {
                        alertify.error(response.message);
                    },
                });
            }

        }

    }

};

$(function () {
   $(document).keypress(function(e) {
        if(e.which === 13) {
            AUTHENTICATION.login();
        }
    });
});
