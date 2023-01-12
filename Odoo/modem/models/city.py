# -*- coding: utf-8 -*-

from odoo import models, fields, api


# Creating Model/Table to Store Doctor Details
# https://www.youtube.com/watch?v=L6MxDR71_1k&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=2
class transferCity(models.Model):
    _name = 'transfer.city'
    _description = 'City Record'

    name = fields.Char(string="Name", required=True, translate=True)
    
    
    
class productTemplateInherit(models.Model):
    _inherit = 'product.template'
    
    from_id = fields.Many2one('transfer.city', string="From")
    to_id = fields.Many2one('transfer.city', string="To")

    

    @api.onchange('from_id','to_id')
    def onchange_ab(self):
        if self.from_id or self.to_id: 
            self.name = str(self.from_id.name) + "-" + str(self.to_id.name)
        
    
 


    