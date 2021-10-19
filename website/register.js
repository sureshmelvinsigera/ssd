$('#register').click(function() {
    // Registration function- first thing to check is if passwords match.
    // Other validation issues are handled by Django.
    if ($("#password").val() != $("#confirm_password").val()) {
        alert("Passwords do not match.");
    } else {
        var astronaut_selected = $('#astronaut-radio:checked').val() == "on";
        var surgeon_selected = $('#surgeon-radio:checked').val() == "on";

        var credentials = {
            first_name: $("#first_name").val(),
            last_name: $("#last_name").val(),
            username: $("#username").val(),
            email: $("#email").val(),
            password: $("#password").val()
        };

        if (astronaut_selected) {
            register_via_api("http://127.0.0.1:8000/auth/users/astronaut/register/", credentials);
        } else if (surgeon_selected) {
            register_via_api("http://127.0.0.1:8000/auth/users/scientist/register/", credentials);
        } else {
            // Login can't proceed unless the user selects a role
            alert("Please select the role you are trying to register as.");
        }
    }
});

function register_via_api(endpoint, credentials) {
    $.ajax({
        url: endpoint,
        type: "POST",
        data: JSON.stringify(credentials),
        contentType:"application/json; charset=utf-8",
        success: function(data) {
            alert("Account successfully registered.");
            window.location.replace("http://localhost:8002/");    
        },
        error: function(error) {
            display_registration_error_message(error.responseJSON);
        }
    });
}

function display_registration_error_message(errors) {
    var response = "";

    var non_field_errors = errors.non_field_errors; 
    if (non_field_errors != undefined) {
        for (const reason of non_field_errors) {
            response += "\n- " + reason;
        }
        // Delete the corresponding property so this error isn't printed twice.
        // Error data isn't used for anything besides informing the user on why their login failed, so deletion is acceptable.
        delete errors.non_field_errors;
    }

    for (const reason in errors) {
        response += "\n- " + reason + ": " + errors[reason];
    }

    alert("Registration failed due to the following reason(s): " + response);
}

// Functions below ensure that only one radio button can be selected at a time
$("#astronaut-radio").click(function() {
    $("#astronaut-radio").prop("checked", true);
    $("#surgeon-radio").prop("checked", false);
});

$("#surgeon-radio").click(function() {
    $("#surgeon-radio").prop("checked", true);
    $("#astronaut-radio").prop("checked", false);
});