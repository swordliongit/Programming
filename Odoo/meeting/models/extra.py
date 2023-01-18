# -*- coding: utf-8 -*-

from odoo import models, fields


# Creating Model/Table to Store Doctor Details
# https://www.youtube.com/watch?v=L6MxDR71_1k&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=2
class transferExtra(models.Model):
    _name = 'transfer.extra'
    _description = 'Extra Record'

    name = fields.Char(string="Name", required=True, translate=True)
    extra_status = fields.Boolean(string="Extra Service")
    extra_reservation_show = fields.Boolean(string="Reservation Page")
    extra_car_show = fields.Boolean(string="Select Car Page")
    image = fields.Binary(string="Image")
    
    
    
class transferCarInherit(models.Model):
    _inherit = 'transfer.car'

    extras = fields.Many2many('transfer.extra',relation='x_transfer_car_transfer_extra_rel', column1='transfer_car_id',column2='transfer_extra_id', string="Extras")
    