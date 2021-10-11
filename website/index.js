$('#login').click(function() {
    var astronaut_selected = $('#astronaut-radio:checked').val() == "on";
    var surgeon_selected = $('#surgeon-radio:checked').val() == "on";

    var credentials = {
        username: $("#username").val(),
        email: $("#email").val(),
        password: $("#password").val()
    };

    if (astronaut_selected) {
        $.post({
            url: "http://127.0.0.1:8000/auth/users/astronaut/login/",
            data: JSON.stringify(credentials),
            success: function(data) {
                console.log(data);
            },
            error: function(error) {
                console.log(error);
            }
        });
    } else if (surgeon_selected) {
        $.post({
            url: "http://127.0.0.1:8000/auth/users/scientist/login/",
            data: JSON.stringify(credentials),
            success: function(data) {
                console.log(data);
            },
            error: function(error) {
                console.log(error);
            }
        });
    } else {
        // Neither selected
        alert("Please select the role you are trying to sign in as.");
    }
});

// Code to reset the radio buttons
$("#astronaut-radio").click(function() {
    $("#astronaut-radio").prop("checked", true);
    $("#surgeon-radio").prop("checked", false);
});

$("#surgeon-radio").click(function() {
    $("#surgeon-radio").prop("checked", true);
    $("#astronaut-radio").prop("checked", false);
});
