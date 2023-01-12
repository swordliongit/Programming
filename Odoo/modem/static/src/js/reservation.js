var price = 0;
var calculated_price = 0;

odoo.define('partner.myfunct', function(require) {
    'use strict';

    var rpc = require('web.rpc');
    var model = 'res.partner';

    // Use an empty array to search for all the records
    var domain = [
        ['id', '=', 1]
    ];
    // Use an empty array to read all the fields of the records
    var fields = ['name', 'discount_percentage'];
    rpc.query({
        model: model,
        method: 'search_read',
        args: [domain, fields],
    }).then(function(data) {
        price = $("#price").val();
        var percentage = (100 - (data[0]['discount_percentage']) / 2) / 100;
        calculated_price = 2 * price * percentage;
    }).then(fuction_Demo(111));

});


function fuction_Demo(data) {
    console.log(data);
}

$('#return_status').click(function () {

    if (document.getElementById('return_status').checked) {
        document.getElementById('return_div').setAttribute('class', 'col');
        document.getElementById('coming_transfer_date').disabled = false;
        document.getElementById('coming_transfer_time').disabled = false;
        document.getElementById('coming_flight_no').disabled = false;
        document.getElementById('coming_destination').disabled = false;

    } else {
        document.getElementById('return_div').setAttribute('class', 'd-none');
        document.getElementById('coming_transfer_date').disabled = true;
        document.getElementById('coming_transfer_time').disabled = true;
        document.getElementById('coming_flight_no').disabled = true;
        document.getElementById('coming_destination').disabled = true;
    }
});




$("input[type=time]").clockpicker({
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

// const phoneInputField = document.querySelector("input[type=tel]");
// const phoneInput = window.intlTelInput(phoneInputField, {
//     preferredCountries: ["tr", "de", "gb", "ru", "us"],
//     hiddenInput: "customer_country_code",
//     utilsScript:
//         "transfer/static/src/js/utils.js",
// });
var input = document.querySelector("#customer_phone");
window.intlTelInput(input, {
    hiddenInput: "customer_phone",
    preferredCountries: ["tr", "de", "gb", "ru", "us"],
    // utilsScript:
    //     "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
}
    //utilsScript: "../../build/js/utils.js?1638200991544" // just for formatting/placeholders etc
);


$(document).ready(function () {

    var quantitiy = 0;
    $('.bebek-plus').click(function (e) {

        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        var quantity = parseInt($('#baby_number').val());

        // If is not undefined

        $('#baby_number').val(quantity + 1);


        // Increment

    });

    $('.bebek-minus').click(function (e) {
        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        var quantity = parseInt($('#baby_number').val());

        // If is not undefined

        // Increment
        if (quantity > 0) {
            $('#baby_number').val(quantity - 1);
        }
    });

});

$(document).ready(function () {

    var quantitiy = 0;
    $('.yetiskin-plus').click(function (e) {

        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        var quantity = parseInt($('#passenger_number').val());

        // If is not undefined

        $('#passenger_number').val(quantity + 1);


        // Increment

    });

    $('.yetiskin-minus').click(function (e) {
        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        var quantity = parseInt($('#passenger_number').val());

        // If is not undefined

        // Increment
        if (quantity > 0) {
            $('#passenger_number').val(quantity - 1);
        }
    });

});
$(document).ready(function () {

    var quantitiy = 0;
    $('.cocuk-plus').click(function (e) {

        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        var quantity = parseInt($('#child_number').val());

        // If is not undefined

        $('#child_number').val(quantity + 1);


        // Increment

    });

    $('.cocuk-minus').click(function (e) {
        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        var quantity = parseInt($('#child_number').val());

        // If is not undefined

        // Increment
        if (quantity > 0) {
            $('#child_number').val(quantity - 1);
        }
    });

});