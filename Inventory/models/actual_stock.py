from odoo import models, fields, api


class ActualStock(models.Model):
    _name = 'actual.stock'
    _description = "Actual Stock"

    sku = fields.Char(string='SKU')
    barcode = fields.Char(string='BarCode')
    date = fields.Date(string='Date')
    MAP = fields.Float(string='MAP')
    quantity = fields.Integer(string='Quantity')
    schedule_id = fields.Many2one('schedule.details',string='Schedule',readonly=True)
    
   