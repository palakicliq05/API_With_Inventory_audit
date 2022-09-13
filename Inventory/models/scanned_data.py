from odoo import models, fields, api


class ScannedData(models.Model):
    _name = 'scanned.data'
    _description = "Scanned Data"

    sku = fields.Char(string='SKU')
    barcode = fields.Char(string='Bar Code')
    date = fields.Date(string='Date')
    user = fields.Many2one('res.users',string="User")
    MAP = fields.Float(string='MAP')
    quantity = fields.Integer(string='Quantity')
    location_barcode = fields.Char(string="Location Barcode")
    schedule_id = fields.Many2one('schedule.details',string='Schedule',readonly=True)