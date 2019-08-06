// function move() {
//     var elem = document.getElementById("myBar");
//     var width = 1;
//     var id = setInterval(frame, 10);

//     function frame() {
//         if (width >= 100) {
//             clearInterval(id);
//         } else {
//             width++;
//             elem.style.width = width + '%';
//         }
//     }
// }

$(document).ready(function() {
    $("#update-database").click(function () {
        $.ajax({
            method: "POST",
            url: "/update_database",
            async: "asynchronous",
            success: function () {
                console.log("Database Update - SUCCESS")
            },
            error: function(request, status, error) {
                console.log("Error: " + error)
            }
        })
    });

    // Disables the "Select a Date:"" option in the select field
    $("#sale-date-select-field option:first-child").attr("disabled", true);

    // $("#update-database").click(function () {
    //     document.location.href
    // })
});

