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
        login_via_api("http://127.0.0.1:8000/auth/users/astronaut/login/", credentials, "astronaut");
    } else if (surgeon_selected) {
        login_via_api("http://127.0.0.1:8000/auth/users/scientist/login/", credentials, "scientist");
    } else {
        // Login can't proceed unless the user selects a role
        alert("Please select the role you are trying to sign in as.");
    }
});

function login_via_api(endpoint, credentials, usertype) {
    $.ajax({
        url: endpoint,
        type: "POST",
        data: JSON.stringify(credentials),
        contentType:"application/json; charset=utf-8",
        success: function(data) {
            // The token is stored using HTML5 session storage and JavaScript. This ensures that token storage is short-term only (Mozilla, 2021).
            // XSS can be used to compromise the token if these technologies are used (OWASP, 2021).
            // To minimize this risk, untrusted inputs are sanitized before rendering them- see in-space.js for details.
            window.sessionStorage.setItem("token", data["token"]);
            if (usertype == "astronaut") {
                window.location.replace("http://localhost:8002/astronaut-details.html");
            } else {
                // If a scientist was authenticated, load this page
                window.location.replace("http://localhost:8002/all-astronaut-records.html");
            }
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
// OWASP. (2021) Cross Site Scripting (XSS). Available from: https://owasp.org/www-community/attacks/xss/ [Accessed 16 October 2021].