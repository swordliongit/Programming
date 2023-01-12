{
    'name':'Modem',
    'version': '1.5.19',
    'author': 'Autoronics',
    'summary': 'Modem Home Management System',
    'sequence': 1,
    'description':'This is modem home management system software suppored in Odoo v15',
    'category':'modem',
    'website':'https://www.autoronics.com',
    'depends':['base','website'],

    'data':[
        'security/ir.model.access.csv',
        #'security/security.xml',
        'views/all_records_list.xml',
        # 'views/record_item.xml',
        #'views/form_response.xml',
        #'views/sale_order.xml',
        #'views/form_request.xml',
        #'views/car_view.xml',
        #'views/extra.xml',
        #'views/city.xml',
        #'views/snippets/s_booking_widget.xml',
        #'views/snippets/demo/s_cart_product/s_cart_products.xml',
        #'views/snippets/demo/snippets.xml',
        'views/modem_view.xml',
        # 'views/snippets/s_car_select.xml',
        # 'views/snippets/s_reservation_form.xml',
        # 'reports/modem_report_views.xml',
        #'data/antalyahermes.xml'
    ],

    'assets': {
        'web.assets_frontend': [
            # 'modem/static/src/css/intlTelInput.css',
            # 'modem/static/src/css/jquery-clockpicker.min.css',
            # 'modem/static/src/css/style.css',
            # 'modem/static/src/js/jquery-clockpicker.min.js',
            # 'modem/static/src/js/intlTelInput.min.js',
            # 'modem/static/src/js/utils.js',
            # 'modem/static/src/js/reservation.js',
            # 'modem/static/src/js/script.js',
            'modem/static/src/js/thunkableWebviewerExtension.js'
        ]
    }

}
