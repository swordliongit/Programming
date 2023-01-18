$("input[name=time]").clockpicker({
    placement: 'bottom',
    align: 'left',
    autoclose: true,
    default: 'now',
    donetext: "Select",
    init: function () {
        console.log("colorpicker initiated");
    },
    beforeShow: function () {
        console.log("before show");
    },
    afterShow: function () {
        console.log("after show");
    },
    beforeHide: function () {
        console.log("before hide");
    },
    afterHide: function () {
        console.log("after hide");
    },
    beforeHourSelect: function () {
        console.log("before hour selected");
    },
    afterHourSelect: function () {
        console.log("after hour selected");
    },
    beforeDone: function () {
        console.log("before done");
    },
    afterDone: function () {
        console.log("after done");
    }
});
$("input[name=date]").datepicker({
    format: 'mm/dd/yyyy',
    startDate: '-3d'
});
$('.dropdown-toggle').dropdown();

$('.carousel').carousel({
    interval: 2000
})

$(document).ready(function () {
    screen_Started();
});
function screen_Started() {
    document.getElementById("return_div").setAttribute("class", "d-none");
    document.getElementById("coming_transfer_date").setAttribute("disabled", "disabled");
}



// $('#return_status').click(function () {
//     var checkBox = document.getElementById("return_status");
//     var return_div = document.getElementById("return_div");
//     if (checkBox.checked == true) {
//         return_div.setAttribute("class", "col");
//         document.getElementById("coming_transfer_date").removeAttribute("disabled");
//         return_div.setAttribute("class", "col");
//         document.getElementById("coming_transfer_time").removeAttribute("disabled");
//         return_div.setAttribute("class", "col");
//         document.getElementById("coming_flight_no").removeAttribute("disabled");
//         return_div.setAttribute("class", "col");
//         document.getElementById("coming_destination").removeAttribute("disabled");
//     } else {
//         return_div.setAttribute("class", "d-none");
//     }

// });  
