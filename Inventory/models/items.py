from odoo import models, fields, api

class Items(models.Model):
    _name = 'items.details'
    _description = "items Details"
    
    items_name = fields.Char(string='Name')
    sku = fields.Char(string='sku')
    description = fields.Text(string='description')
    barcode = fields.Char(string='barcode')
    MAP = fields.Float(string='MAP')
    