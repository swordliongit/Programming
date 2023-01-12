from odoo import fields, models, api,_
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
import requests
import json
cookie = "modem"

class modemProfile(models.Model):
    _name = "modem.profile"

    name = fields.Char(string="Name")
    modem_id = fields.Char(string="Device Id")
    modem_status = fields.Selection([('active','Active'),('passive', 'Passive'),('home', 'At Home')],
                                   string="Device Status",
                                   )
    live_status = fields.Selection([('wifionline','Wifi Online'),('gsmonline','Gsm Online'),('offline', 'Offline')],
    string="Live Status", default="offline"
    )
    city = fields.Char(string="City")
    #customer_id = fields.Many2one('res.partner', string="Customer")
    customer_id = fields.Many2many('res.partner',relation='x_modem_profile_res_partner_rel', column1='modem_profile_id',column2='res_partner_id', string="Customer")
    last_action_user = fields.Many2one('res.partner', string="Last Action User")
    modem_update = fields.Boolean(string="Device Update")
    modem_version = fields.Char(string="Version")
    modem_home_mode = fields.Boolean(string="Home Mode")
    modem_image = fields.Binary(string="Image")
    
    x_device_update = fields.Boolean(string="Device Update Check")
    x_uptime = fields.Char(string="Uptime")
    x_wireless_status = fields.Char(string="Wireless Status")
    x_channel = fields.Char(string="Channel")
    x_mac = fields.Char(string="MAC")
    x_device_info= fields.Char(string="Device Info")
    x_ip = fields.Char(string="IP")
    x_subnet = fields.Char(string="Subnet")
    x_dhcp = fields.Boolean(string="DHCP")
    x_enable_wireless = fields.Boolean(string="Enable Wireless")
    x_enable_ssid1 = fields.Boolean(string="Enable SSID1")
    x_enable_ssid2 = fields.Boolean(string="Enable SSID2")
    x_enable_ssid3 = fields.Boolean(string="Enable SSID3")
    x_enable_ssid4 = fields.Boolean(string="Enable SSID4")
    x_manual_time = fields.Char(string="Manual Time")
    x_new_password = fields.Char(string="New Password")
    x_hotel_name = fields.Char(string="Otel adı")
    x_update_date = fields.Char(string="Güncellenme tarihi")
    x_reboot = fields.Boolean(string="Reboot")

    
    def action_open_wizard(self):
        active_ids = self._context.get('active_ids')
        return {
            'name': "Test Wizard",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'modem.profile',
            'view_id': self.env.ref('modem.modem_wizard').id,
            'context': {'x_enable_wireless': True, 'active_ids': active_ids},
            'target': 'new'
                }
        
    def wizard_apply(self):
        #self.ensure_one()
        active_ids = self._context.get('active_ids')
        records = self.env['modem.profile'].browse(active_ids)
        records.write({'x_enable_wireless': self.x_enable_wireless})
        return {'type': 'ir.actions.act_window_close'}
        
    # def wizard_apply(self):
    #     return True

    
    # @api.multi
    # def action_open_wizard(self):
    #     return {
    #         'name': 'My Wizard',
    #         'type': 'ir.actions.act_window',
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'res_model': 'modem.profile',
    #         'context': {'default_field_name': 'initial value'},
    #         'target': 'new'
    #     }
    
    
    

    
    
    
    
    @api.onchange('modem_status')
    def _get_partner(self):
        partner = self.env['res.users'].browse(self.env.uid).partner_id
        for rec in self: 
            rec.last_action_user = partner.id

    def write_Device_Status_Active(self):
        if self.modem_update == False:
            self.write({'modem_status': 'active'})
            self.write({'modem_update': True})
            partner = self.env['res.users'].browse(self.env.uid).partner_id
            for rec in self: 
                rec.last_action_user = partner.id
        else:
            raise ValidationError("Cihaz Son Yaptığınız Ayarları Henüz Almadı. 1 Dakika Sonra Tekrar Deneyiniz.")
        
    def write_Device_Status_Passive(self):
        if self.modem_update == False:
            self.write({'modem_status': 'passive'})
            self.write({'modem_update': True})
            partner = self.env['res.users'].browse(self.env.uid).partner_id
            for rec in self: 
                rec.last_action_user = partner.id
        else:
            raise ValidationError("Cihaz Son Yaptığınız Ayarları Henüz Almadı. 1 Dakika Sonra Tekrar Deneyiniz.")

    def write_Device_Status_Home(self):
        if self.modem_update == False:
            self.write({'modem_status': 'home'})
            self.write({'modem_update': True})
            partner = self.env['res.users'].browse(self.env.uid).partner_id
            for rec in self: 
                rec.last_action_user = partner.id
        else:
            raise ValidationError("Cihaz Son Yaptığınız Ayarları Henüz Almadı. 1 Dakika Sonra Tekrar Deneyiniz.")

    def create_emergency_report(self):
        partner = self.env['res.users'].browse(self.env.uid).partner_id
        user_name = "Belirlenemeyen"
        for rec in self: 
            user_name = partner.name
        self.env['reports.profile'].sudo().create({
            'name': user_name + " Adlı kullanıcı Acil Durum Çağrısında Bulundu.",
            'ademco_id': "B001-000"
            })
    def create_ambulance_report(self):
        partner = self.env['res.users'].browse(self.env.uid).partner_id
        user_name = "Belirlenemeyen"
        for rec in self: 
            user_name = partner.name
        self.env['reports.profile'].sudo().create({
            'name': user_name + " Adlı kullanıcı Ambulans Çağrısında Bulundu.",
            'ademco_id': "B002-000"
            })
    def create_fire_report(self):
        partner = self.env['res.users'].browse(self.env.uid).partner_id
        user_name = "Belirlenemeyen"
        for rec in self: 
            user_name = partner.name
        self.env['reports.profile'].sudo().create({
            'name': user_name + " Adlı kullanıcı Yangın Çağrısında Bulundu.",
            'ademco_id': "B003-000"
            })
                              
class ResPartnersInherit(models.Model):
    _inherit = 'res.partner'

#discount_percentage = fields.Float("Discount Percentage")

    #gender = fields.Selection([('male','Male'),('female', 'Female'),('other', 'Other'),],string="Gender")
    #type_of_person = fields.Selection([('adult','Adult'),('child', 'Child'),('baby', 'Baby'),('driver', 'Driver')],string="Person Type")
    
    # How to OverRide Create Method Of a Model
    # https://www.youtube.com/watch?v=AS08H3G9x1U&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=26
    
    #@api.model
    #def create(self, vals_list):
    #    res = super(ResPartners, self).create(vals_list)
    #    print("yes working")
    #    # do the custom coding here
    #    return res
    
# class MyWizard(models.TransientModel):
#     _name = 'my.wizard'
#     field_name = fields.Boolean(string='Enable Wireless')
    
#     @api.multi
#     def wizard_apply(self):
#         self.ensure_one()
#         active_ids = self._context.get('active_ids')
#         records = self.env['modem.profile'].browse(active_ids)
#         records.write({'x_enable_wireless': self.field_name})
#         return {'type': 'ir.actions.act_window_close'}