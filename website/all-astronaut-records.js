$(document).ready(function () {
    var token = sessionStorage.getItem("token");
    if (token != undefined) {
        get_astronaut_records(token);
        $("#astronaut-table").DataTable();
    }
});

function get_astronaut_records(token) {
    var authorization_header = "JWT " + token;
    $.ajax({
        // Show 100 by default
        url: "http://localhost:8000/scientist/health-reports/100",
        type: "GET",
        contentType:"application/json; charset=utf-8",
        headers: { "Authorization" : authorization_header },
        success: function(data) {
            var astronauts = data["results"];
            for (const astronaut of astronauts) {
                // Inline rendering is used here via template syntax, however, this could lead to arbitrary code execution.
                // To prevent this vulnerability, all received text is treated as untrusted (since first and last names come from user inputs)
                // and are therefore stripped of any HTML tags before rendering. DOMParser is used to achieve this due to its speed and functionality (Sabaz, 2017).
                var row = `
                    <tr>
                        <td>${remove_html_tags(astronaut["weight"])}</td>
                        <td>${remove_html_tags(astronaut["blood_type"])}</td>
                        <td>${remove_html_tags(astronaut["blood_pressure"])}</td>
                        <td>${remove_html_tags(astronaut["heart_rate"])}</td>
                        <td>${remove_html_tags(astronaut["feedback"])}</td>
                    </tr>
                `;
                $("table > tbody").append(row);
            }
            console.log(data);
        },
        error: function(error) {
            alert("Error encountered while loading the page, please try refreshing.");
        }
    });
}

function remove_html_tags(text) {
    let doc = new DOMParser().parseFromString(text, 'text/html');
    // If there are only non-text elements, textContent will return an empty string.
    // Display nothing if this is the case, to prevent any chance of a script injection attack. 
    if (doc.body.textContent == "") {
        return "";
    } else {
        return doc.body.textContent; 
    }
}

// References
// Sabaz. (2017) Strip HTML from Text JavaScript. Available from: https://stackoverflow.com/questions/822452/strip-html-from-text-javascript/47140708#47140708 [Accessed 18 October 2021].