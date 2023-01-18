# -*- coding: utf-8 -*-

from odoo import models, fields


# Creating Model/Table to Store Doctor Details
# https://www.youtube.com/watch?v=L6MxDR71_1k&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=2
class transferCar(models.Model):
    _name = 'transfer.car'
    _description = 'Car Record'

    name = fields.Char(string="Name", required=True, translate=True)
    type = fields.Char(string="Type", required=True, translate=True)
    plate = fields.Char("Plate", copy=False)
    passenger_cap = fields.Integer("Max Person")
    luggage_cap = fields.Integer("Max Luggage")
    user_id = fields.Many2one('res.users', string='Driver')
    description = fields.Text("Description", copy=False, translate=True)
    image_1 = fields.Binary(string="Image 1")
    image_2 = fields.Binary(string="Image 2")
    image_3 = fields.Binary(string="Image 3")
    image_4 = fields.Binary(string="Image 4")
    image_5 = fields.Binary(string="Image 5")
    image_6 = fields.Binary(string="Image 6")
    car_lines = fields.One2many('transfer.car.lines', 'id', string='Cars')
    
class transferCarLines(models.Model):
    _name = 'transfer.car.lines'
    _description = 'Car Lines Record'

    car_price = fields.Float(string="Price(€)", digits=(12,2))
    car_id = fields.Many2one('transfer.car', string='Car')
    sequence = fields.Integer(string="Sequence")
    
    
    
class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    car_lines = fields.One2many('transfer.car.lines', 'sequence', string='Cars')
    
