from odoo import models, fields, api


class Locations(models.Model):
    _name = 'locations.details'
    _description = "locations Details"

    description = fields.Char(string='Description')
    location_barcode = fields.Char(string='Location Barcode')
    stock_auditor = fields.Many2one('res.users',string='Stock Auditor')
    # phase = fields.Char('phase.details',string='Phase')
    phase_id = fields.Many2one('phase.details',string='Phase',readonly=True)
    
    