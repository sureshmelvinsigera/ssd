$('#login').click(function() {
    // Main login function- collects details and sends it to the corresponding endpoint
    var astronaut_selected = $('#astronaut-radio:checked').val() == "on";
    var surgeon_selected = $('#surgeon-radio:checked').val() == "on";

    var credentials = {
        username: $("#username").val(),
        email: $("#email").val(),
        password: $("#password").val()
    };

    if (astronaut_selected) {
        login_via_api("http://127.0.0.1:8000/auth/users/astronaut/login/", credentials);
    } else if (surgeon_selected) {
        login_via_api("http://127.0.0.1:8000/auth/users/scientist/login/", credentials);
    } else {
        // Login can't proceed unless the user selects a role
        alert("Please select the role you are trying to sign in as.");
    }
});

function login_via_api(endpoint, credentials) {
    $.ajax({
        url: endpoint,
        type: "POST",
        data: JSON.stringify(credentials),
        contentType:"application/json; charset=utf-8",
        success: function(data) {
            // TODO: set JWT and redirect
            console.log(data);
        },
        error: function(error) {
            display_login_error_message(error.responseJSON)
        }
    });
}

/*
    Note: in the case that a login fails, the error message does not tell the user 
    if the login failed because the username was invalid, or the password. Instead,
    it gives an ambiguous message- this prevents enumeration attacks, a kind of brute force attack
    that relies on finding all possible usernames (Laverty, 2017).
*/
function display_login_error_message(errors) {
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

    alert("Login failed due to the following reason(s): " + response);
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


// References
// Laverty, P. (2017) What is Username Enumeration? Available from: https://www.rapid7.com/blog/post/2017/06/15/about-user-enumeration/ [Accessed 14 October 2021].