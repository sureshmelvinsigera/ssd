$(document).ready(function () {
    load_astronaut_details();
});

function load_astronaut_details() {
    var token = sessionStorage.getItem("token");
    if (token != undefined) {
        get_astronaut_records(token);
    }    
}

function get_astronaut_records(token) {
    var authorization_header = "JWT" + token;
    $.ajax({
        url: "http://localhost:8000/astronauts/in-space/",
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
                        <td>${remove_html_tags(astronaut["username"])}</td>
                        <td>${remove_html_tags(astronaut["email"])}</td>
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
    // Strings are "truthy" in Javascript. They have an innate boolean representation, which can be used as shorthand. If a string is empty, it is false. 
    // A string can be empty after sending it to DOMParser because it might not be valid HTML.
    // Any code wrapped inside a <script> tag, for instance, would result in an empty String. This therefore prevents script injection.
    if (!doc) {
        return "";
    } else {
        return doc.body.textContent;
    }
}

// References
// Sabaz. (2017) Strip HTML from Text JavaScript. Available from: https://stackoverflow.com/questions/822452/strip-html-from-text-javascript/47140708#47140708 [Accessed 18 October 2021].