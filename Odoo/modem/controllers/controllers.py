# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools
from odoo import http
from odoo.http import request, Response, route, JsonRequest
from datetime import datetime,date
import logging
import requests
import json
_logger = logging.getLogger(__name__)
from odoo.tools import date_utils

class CustomSnippets(http.Controller):
    @http.route(['/transfer/cart_content'], type='http', auth="public", website=True)
    def cart(self):
        products = request.website.sale_get_order().order_line.product_id
        data = []
        for product in products:
            fields = product.read(['display_name', 'description_sale', 'list_price', 'website_url'])[0];
            fields['image'] = request.env['website'].image_url(product, 'image_512')
            data.append(fields)
        return request.env['ir.ui.view']._render_template('transfer.s_cart_products_card', {'products': data})

class modemProfileReq(http.Controller):
    @http.route(['/create/modems_from_data'], type="json", auth="public", methods=["POST"], cors='*', csrf=False)
    def modem_data_send(self):
        data = json.loads(request.httprequest.data)
        for modem in data["modems"]:
            http.request.env['modem.profile'].sudo().create({
                'x_uptime': modem['x_uptime'],
                'x_wireless_status': modem['x_wireless_status'],
                'x_channel': modem['x_channel'],
                'x_mac': modem['x_mac'],
                'x_device_info': modem['x_device_info'],
                'x_ip': modem['x_ip'],
                'x_subnet': modem['x_subnet'],
                'x_dhcp': modem['x_dhcp'],
                'x_enable_wireless': modem['x_enable_wireless'],
                'x_enable_ssid1': modem['x_enable_ssid1'],
                'x_enable_ssid2': modem['x_enable_ssid2'],
                'x_enable_ssid3': modem['x_enable_ssid3'],
                'x_enable_ssid4': modem['x_enable_ssid4'], 
                'x_manual_time': modem['x_manual_time'],
                'x_new_password': modem['x_new_password'],
                'x_hotel_name': modem['x_hotel_name'],
                'x_update_date': modem['x_update_date']
            })
        # for modem in data:
        #     http.request.env['modem.profile'].sudo().create({
        #         'x_uptime': modem['x_uptime'],
        #         'x_wireless_status': modem['x_wireless_status'],
        #         'x_channel': modem['x_channel'],
        #         'x_mac': modem['x_mac'],
        #         'x_device_info': modem['x_device_info'],
        #         'x_ip': modem['x_ip'],
        #         'x_subnet': modem['x_subnet'],
        #         'x_dhcp': modem['x_dhcp'],
        #         'x_enable_wireless': modem['x_enable_wireless'],
        #         'x_enable_ssid1': modem['x_enable_ssid1'],
        #         'x_enable_ssid2': modem['x_enable_ssid2'],
        #         'x_enable_ssid3': modem['x_enable_ssid3'],
        #         'x_enable_ssid4': modem['x_enable_ssid4'], 
        #         'x_manual_time': modem['x_manual_time'],
        #         'x_new_password': modem['x_new_password'],
        #         'x_hotel_name': modem['x_hotel_name'],
        #         'x_update_date': modem['x_update_date']
        #     })

        return data
    
    #############################################
    #############################################
    #############################################
    
    @http.route(['/create/report-for-modem'], type="json", auth="public", methods=["POST"], cors='*', csrf=False)
    def create_modem_req_1(self):
        data = json.loads(request.httprequest.data)
        modem_id = http.request.env['modem.profile'].sudo().search([["modem_id","=",data['params']['modem_id']]],limit=1)
        if len(modem_id) > 0:
            result = ""
            if data['params']['modem_update'] == 2:
                modem_id.modem_update = False
            if data['params']['modem_update'] == 0:
                modem_id.modem_update = True
            if data['params']['create_report'] == False and modem_id.modem_update == False:
                result = {"code": 200, "message": "Idle Ask Successfully"}
            if data['params']['create_report'] == False and modem_id.modem_update == True:
                settings = http.request.env['settings.profile'].sudo().search([["modem_id.modem_id","=",data['params']['modem_id']]],limit=1)
                result = {"code": 200, "message": "Idle Ask Successfully", "modem_update": modem_id.modem_update, "modem_status": modem_id.modem_status, "entrance_delay_time": settings.entrance_delay_time, "exit_delay_time": settings.exit_delay_time, "alarm_time": settings.alarm_time, "default_settings_1": settings.default_settings_1, "zone_status_1": settings.zone_status_1, "always_on_1": settings.always_on_1, "sudden_alarm_1": settings.sudden_alarm_1, "default_settings_2": settings.default_settings_2, "zone_status_2": settings.zone_status_2, "always_on_2": settings.always_on_2, "sudden_alarm_2": settings.sudden_alarm_2, "default_settings_3": settings.default_settings_3, "zone_status_3": settings.zone_status_3, "always_on_3": settings.always_on_3, "sudden_alarm_3": settings.sudden_alarm_3, "default_settings_4": settings.default_settings_4, "zone_status_4": settings.zone_status_4, "always_on_4": settings.always_on_4, "sudden_alarm_4": settings.sudden_alarm_4, "wifi_name": settings.wifi_name, "wifi_password": settings.wifi_password, "test_signal_time": settings.test_signal_time, "last_value": 1}
            if data['params']['create_report'] == True and modem_id.modem_update == False:
                val = {
                'modem_id': modem_id.id,
                'ademco_id': data['params']['code'],
                'zone': data['params']['zone'],
                #'date': datetime.now()
                }
                create = request.env['reports.profile'].sudo().create(val)
                result = {"code": 200, "message": "Live Report Created Successfully"}
            if data['params']['create_report'] == True and modem_id.modem_update == True:
                settings = http.request.env['settings.profile'].sudo().search([["modem_id.modem_id","=",data['params']['modem_id']]],limit=1)
                val = {
                'modem_id': modem_id.id,
                'ademco_id': data['params']['code'],
                'zone': data['params']['zone'],
                #'date': datetime.now()
                }
                create = request.env['reports.profile'].sudo().create(val)
                result = {"code": 200, "message": "Live Report Created Successfully", "modem_update": modem_id.modem_update, "modem_status": modem_id.modem_status, "entrance_delay_time": settings.entrance_delay_time, "exit_delay_time": settings.exit_delay_time, "alarm_time": settings.alarm_time, "default_settings_1": settings.default_settings_1, "zone_status_1": settings.zone_status_1, "always_on_1": settings.always_on_1, "sudden_alarm_1": settings.sudden_alarm_1, "default_settings_2": settings.default_settings_2, "zone_status_2": settings.zone_status_2, "always_on_2": settings.always_on_2, "sudden_alarm_2": settings.sudden_alarm_2, "default_settings_3": settings.default_settings_3, "zone_status_3": settings.zone_status_3, "always_on_3": settings.always_on_3, "sudden_alarm_3": settings.sudden_alarm_3, "default_settings_4": settings.default_settings_4, "zone_status_4": settings.zone_status_4, "always_on_4": settings.always_on_4, "sudden_alarm_4": settings.sudden_alarm_4, "wifi_name": settings.wifi_name, "wifi_password": settings.wifi_password, "test_signal_time": settings.test_signal_time, "last_value": 1}
            return result
        else:
            return "no"

    @http.route(['/create/report-for-modem-gsm'], type="http", auth="public", methods=["GET"], cors='*', csrf=False)
    def create_modem_req_gsm_2(self):
        return "{'code': 200, 'message': 'Idle Ask Successfully'}"


    @http.route('/chplayerid/<email>/<player_id>', type='http', auth="public", methods=["GET"], cors='*', website=False)
    def write_Playerid(self, email,player_id):
        # get the information using the SUPER USER
        result = "not found"
        contact = http.request.env['res.partner'].sudo().search([['email','=', str(email)]])
        if len(contact) == 1:
            contact['player_id'] = player_id
            result = "ok"
        return result
    
    #widget transfer booking
    @http.route('/selectionlogin/form-1', type="http", auth="public", website=True,  csrf=False)
    def log_in_modem(self, **kw):
        print("Data Received.....", kw)
        vals = {
             'user_id': kw.get('user_id'),
             'virtual_user_id': kw.get('virtual_user_id'),
             'access_code': kw.get('access_code'),
             'modem_id': kw.get('modem_id')
         }
        contact = http.request.env['res.partner'].sudo().search([['id','=', kw.get('user_id')]])
        virtual_contact = http.request.env['res.partner'].sudo().search([['id','=', kw.get('virtual_user_id')]])
        if len(contact) == 1:
            if virtual_contact in contact.x_modem_users or virtual_contact in contact:
                if virtual_contact.x_access_code == kw.get('access_code'):
                    contact['ref'] = kw.get('modem_id')
                    if virtual_contact.x_contract_manager == True:
                        return request.redirect('/shop?shop_value=vN9dOkuiQdCXMOiZMGRFtUBDUZN7RhY2')
                    if virtual_contact.x_contract_manager == False:
                        return request.redirect('/shop?shop_value=nN9dOkuiQdCXMOiZMGBFtUBDUZN7RhY2')
        else:
            contact['ref'] = False
            return request.redirect('/wrong_values')
    
    @http.route('/selectionlogout/<user_id>/<modem_id>', type='http', auth="public", methods=["GET"], cors='*', website=False)
    def log_out_modem(self, user_id,modem_id):
        # get the information using the SUPER USER
        result = "not found"
        modem_order = http.request.env['sale.modem.order'].sudo().search([['id','=', modem_id]],limit=1)
        contact = http.request.env['res.partner'].sudo().search([['id','=', user_id]])
        order = http.request.env['sale.order'].sudo().search(["&","&",['partner_id.id','=', modem_order.partner_id.id],["website_id.id","=",1],["state","=","draft"]])
        if len(modem_order) == 0:
            contact['ref'] = False
            return request.redirect('/contracts')
        elif len(contact) == 1 and len(order) == 0:
            contact['ref'] = False
            return request.redirect('/contracts')
        elif len(contact) == 1 and len(order) == 1 and len(order.order_line) == 0:
            contact['ref'] = False
            return request.redirect('/contracts')
        elif len(contact) == 1 and len(order) == 1 and len(order.order_line) > 0:
            #return request.render("website_sale.cart", {'alert_id': 1, 'product':result})
            return request.redirect('/shop/cart?alert_id=1')
        else:
            contact['ref'] = False
            return request.redirect('/contracts')

    #widget transfer booking
    @http.route('/addtocard/form-1', type="http", auth="public", website=True,  csrf=False)
    def add_to_card(self, **kw):
        print("Data Received.....", kw)
        vals = {
            'user_id': kw.get('user_id'),
            'virtual_user_id': kw.get('virtual_user_id'),
            'product_id': kw.get('product_id'),
            'product_stock': kw.get('product_stock'),
            'product_validity_date': kw.get('product_validity_date'),
            'quantity': kw.get('quantity'),
            'price': kw.get('price'),
            'currency': kw.get('currency'),
            'website_url': kw.get('website_url'),
            'modem_id': kw.get('modem_id')
         }
        if kw.get('product_stock'):
            if float(kw.get('product_stock')) > 0 and kw.get('quantity') <= kw.get('product_stock'):
                order = http.request.env['sale.order'].sudo().search(["&","&",['partner_id.id','=', kw.get('user_id')],["website_id.id","=",1],["state","=","draft"]])
                if len(order) > 1:
                    for item in order:
                        if len(item.order_line) == 0:
                            item.sudo().unlink()
                modem_order_line = http.request.env['sale.modem.order.line'].sudo().search(["&",['order_id.id','=', kw.get('modem_id')],["product_id.id","=",kw.get('product_id')]],limit=1)
                base_url = http.request.env['ir.config_parameter'].sudo().get_param('web.base.url')
                if len(order) == 1 and len(order.order_line) > 0:
                    order.sudo().write({
                        "order_line":[
                        [
                            0,
                            "virtual_610",
                            {
                                "product_id": int(kw.get('product_id')),
                                "modem_order_line":modem_order_line.id,
                                "product_template_id":int(kw.get('product_id')),
                                "product_uom_qty":int(kw.get('quantity')),
                                "qty_delivered":0,
                                "qty_delivered_manual":0,
                                "product_uom":1,
                                "customer_lead":0,
                                "product_packaging_qty":0,
                                "product_packaging_id":False,
                                "price_unit":float(kw.get('price')),
                                "product_id":int(kw.get('product_id')),
                                "tax_id":[
                                    [
                                    6,
                                    False,
                                    [
                                        1
                                    ]
                                    ]
                                ],
                                "discount":0
                            }
                        ]
                        ]
                        })
                    
                    items = order.order_line.sudo().search([])
                    
                    # create_ir_logging = http.request.env['ir.logging'].sudo().create({
                    #         'dbname': "Last Server",
                    #         'type': 'server',
                    #         'name': 'odoo.addons.base.models.ir_actions',
                    #         'level': 'info',
                    #         'path': 'action',
                    #         'line': '489',
                    #         'func': 'order line',
                    #         'message': items.mapped('name')
                    #     })
                        

                    order.order_line[len(order.order_line)-1].write({
                        "modem_order_line":modem_order_line.id
                    })
                    return request.redirect(str(kw.get('website_url')).replace(base_url, ''))

                if len(order) == 1 and len(order.order_line) == 0:
                    order.sudo().write({
                        "order_line":[
                        [
                            0,
                            "virtual_610",
                            {
                                "product_id": int(kw.get('product_id')),
                                "modem_order_line":modem_order_line.id,
                                "product_template_id":int(kw.get('product_id')),
                                "product_uom_qty":int(kw.get('quantity')),
                                "qty_delivered":0,
                                "qty_delivered_manual":0,
                                "product_uom":1,
                                "customer_lead":0,
                                "product_packaging_qty":0,
                                "product_packaging_id":False,
                                "price_unit":float(kw.get('price')),
                                "product_id":int(kw.get('product_id')),
                                "tax_id":[
                                    [
                                    6,
                                    False,
                                    [
                                        1
                                    ]
                                    ]
                                ],
                                "discount":0
                            }
                        ]
                        ]
                        })
                    
                    return request.redirect(str(kw.get('website_url')).replace(base_url, ''))
                
                if len(order) == 0:
                    sale_order = http.request.env['sale.order'].sudo().create({
                    'date_order': datetime.now(),
                    'partner_id': modem_order_line.partner_id.id,
                    'partner_invoice_id': modem_order_line.partner_id.id,
                    'partner_shipping_id': modem_order_line.partner_id.id,
                    'website_id': 1,
                    "order_line":[
                        [
                            0,
                            "virtual_610",
                            {
                                "product_id": int(kw.get('product_id')),
                                "modem_order_line":modem_order_line.id,
                                "product_template_id":int(kw.get('product_id')),
                                "product_uom_qty":int(kw.get('quantity')),
                                "qty_delivered":0,
                                "qty_delivered_manual":0,
                                "product_uom":1,
                                "customer_lead":0,
                                "product_packaging_qty":0,
                                "product_packaging_id":False,
                                "price_unit":float(kw.get('price')),
                                "product_id":int(kw.get('product_id')),
                                "tax_id":[
                                    [
                                    6,
                                    False,
                                    [
                                        1
                                    ]
                                    ]
                                ],
                                "discount":0
                            }
                        ]
                        ]
                        })
                    return request.redirect(str(kw.get('website_url')).replace(base_url, ''))
        else:
            return request.redirect("/stokyok")

    # @http.route(['/create/report-for-modem'], type="json", auth="public", methods=["POST"], csrf=False)
    # def create_modem_req_1(self, **kw):
    #     print("Data Received.....", kw)  
    #     return "hello"
    
    # @http.route('/my_module/xxx', type='json', auth='none', methods=['POST']) 
    # def my_foo(self, **post):
    #     data = request.jsonrequest
    #     return data
    

class transferProfileReq(http.Controller):
    
    #widget transfer booking
    @http.route('/create/form-1', type="http", auth="public", website=True,  csrf=False)
    def create_form_req_1(self, **kw):
        print("Data Received.....", kw)
        request.env['transfer.profile'].sudo().create(kw)
        vals = {
             'from': kw.get('from_id'),
             'to': kw.get('to_id'),
             'currency': kw.get('currency_id')
         }
         
        result = http.request.env['product.template'].sudo().search(["|","&",["from_id.id","=",kw.get('from_id')],["to_id.id","=",kw.get('to_id')],"&",["from_id.id","=",kw.get('to_id')],["to_id.id","=",kw.get('from_id')]],limit=1)
        if result:
            return request.render("transfer.form_response_1", {'form_1_details': kw, 'product':result})
        else:
            return request.render("transfer.form_response_4", {'form_1_details': kw, 'product':result})
        
    #car select
    @http.route('/create/form-2', type="http", auth="public", website=True,  csrf=False)
    def create_form_req_2(self, **kw):
        vals = {
             'product': kw.get('product_id'),
             'car': kw.get('car_id'),
             'price': kw.get('price'),
             'currency': kw.get('currency_id')
         }
        return request.render("transfer.form_response_2", {'form_2_details': vals})

    #reservation details
    @http.route('/create/form-3', type="http", auth="public", website=True,  csrf=False)
    def create_form_req_3(self, **kw):
        vals = {
             'id_of_product': kw.get('id_of_product'),
             'from_id': kw.get('from_id'),
             'to_id': kw.get('to_id'),
             'currency': kw.get('currency'),
             'going_transfer_date': kw.get('going_transfer_date'),
             'going_transfer_time': kw.get('going_transfer_time'),
             'going_flight_no': kw.get('going_flight_no'),
             'going_destination': kw.get('going_destination'),
             'return_status': kw.get('return_status'),
             'coming_transfer_date': kw.get('coming_transfer_date'),
             'coming_transfer_time': kw.get('coming_transfer_time'),
             'coming_flight_no': kw.get('coming_flight_no'),
             'coming_destination': kw.get('coming_destination'),
             'special_note': kw.get('special_note'),
             'passenger_number': kw.get('passenger_number'),
             'child_number': kw.get('child_number'),
             'baby_number': kw.get('baby_number'),
             'welcome_status': kw.get('welcome_status'),
             'baby_seat_number': kw.get('baby_seat_number'),
             'booster_seat_number': kw.get('booster_seat_number'),
             'stroller_seat_number': kw.get('stroller_seat_number'),
             'promotion_code': kw.get('promotion_code'),
             'customer_name': kw.get('customer_name'),
             'customer_surname': kw.get('customer_surname'),
             'customer_email': kw.get('customer_email'),
             'customer_phone': kw.get('customer_phone'),
             'another_passengers': kw.get('another_passengers'),
             'price': kw.get('price'),
             'car_name': kw.get('car_name'),
             'car_type': kw.get('car_type'),
             'car_id': kw.get('car_id')
         }
        
        partner_id = http.request.env['res.partner'].sudo().search(["&","&",["name","=",vals['customer_name']],["phone","=",vals['customer_phone']],["email","=",vals['customer_email']]])
        if len(partner_id) == 0:
            request.env['res.partner'].sudo().create({
            'name': vals['customer_name'] + " " + vals['customer_surname'],
            'email': vals['customer_email'],
            'phone': vals['customer_phone']
            })
        
        partner_id = http.request.env['res.partner'].sudo().search(["&","&",["name","=",vals['customer_name'] + " " + vals['customer_surname']],["phone","=",vals['customer_phone']],["email","=",vals['customer_email']]])
        from_id = http.request.env['transfer.city'].sudo().search([["name", "=", vals['from_id']]])
        to_id = http.request.env['transfer.city'].sudo().search([["name", "=", vals['to_id']]])
        currency_id = http.request.env['res.currency'].sudo().search([["name", "=", vals['currency']]])
        product = http.request.env['product.template'].sudo().search([["id", "=", vals['id_of_product']]])
        pricelist_id = http.request.env['product.pricelist'].sudo().search([["currency_id.id", "=", currency_id.id]])
        
        sale_order = request.env['sale.order'].sudo().create({
        'partner_id': partner_id.id,
        'pricelist_id': pricelist_id.id,
        'date_order': datetime.now(),
        
        'id_of_product': vals['id_of_product'],
        'from_id': from_id.id,
        'to_id': to_id.id,
        'currency': vals['currency'],
        'going_transfer_date': vals['going_transfer_date'],
        'going_transfer_time': vals['going_transfer_time'],
        'going_flight_no': vals['going_flight_no'],
        'going_destination': vals['going_destination'],
        'return_status': vals['return_status'],
        'coming_transfer_date': vals['coming_transfer_date'],
        'coming_transfer_time': vals['coming_transfer_time'],
        'coming_flight_no': vals['coming_flight_no'],
        'coming_destination': vals['coming_destination'],
        'special_note': vals['special_note'],
        'passenger_number': vals['passenger_number'],
        'child_number': vals['child_number'],
        'baby_number': vals['baby_number'],
        'welcome_status': vals['welcome_status'],
        'baby_seat_number': vals['baby_seat_number'],
        'booster_seat_number': vals['booster_seat_number'],
        'stroller_seat_number': vals['stroller_seat_number'],
        'promotion_code': vals['promotion_code'],
        'customer_name': vals['customer_name'],
        'customer_surname': vals['customer_surname'],
        'customer_email': vals['customer_email'],
        'customer_phone': vals['customer_phone'],
        'another_passengers': vals['another_passengers'],
        'price': vals['price'],
        'car_name': vals['car_name'],
        'car_type': vals['car_type'],
        'car_id': vals['car_id'],
        #"order_line":[(0,0,{"sequence":10,"display_type":False,"product_uom_qty":1,"qty_delivered":0,"qty_delivered_manual":0,"customer_lead":0,"price_unit":vals['price'],"discount":0,"product_id":sale_order_line.product_id.id,"product_template_id":product.id,"name":product.name,"product_uom":1})]
        
        })
        prd = http.request.env['product.product'].sudo().search([["name", "=", product.name]])
        sale_order.write({
            'order_line': [(0,0, {'product_id':prd.id,"name":product.name,"price_unit":vals['price'],"product_uom_qty":1})]
        })
        #product_id = http.request.env['product.product'].search([],limit=1)
        #sale_order_line = request.env['sale.order.line'].create({  
        #                      'product_id': product.id, 
        #                      "name":product.name,
        #                      "price_unit":vals['price'],
        #                      "product_uom_qty":1,
        #                      "order_id":
        #                    })

        return request.render("transfer.form_response_3", {'form_3_details': vals})