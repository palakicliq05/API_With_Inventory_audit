from odoo import models, fields, api,_,tools


class ActualStock(models.Model):
    _name = 'data.stockreport'
    _description = "Data Details"
    _auto = False
    
    
    item_name = fields.Char(string="product Name")
    sku = fields.Char(string="SKU")
    barcode = fields.Char(string="Barcode")
    actual_qty = fields.Integer(string="Actual Qty")
    location = fields.Char(string="Location")
    location_qty = fields.Integer(string="Location Qty")
    
    
    def init(self):
        # tools.drop_table_if_exists(self._table)
        tools.drop_view_if_exists(self.env.cr,self._table)
        self.env.cr.execute("""
                                create or replace view {} as(    
                                select i.id as id, i.items_name as item_name, i.sku as sku, i.barcode as barcode,
                                aq.quantity as actual_qty, l.description as location, sq.quantity as location_qty
                                from items_details i left join actual_stock aq on i.sku = aq.sku
                                and i.barcode = aq.barcode left join scanned_data sq on aq.sku = sq.sku
                                and aq.barcode = sq.barcode 
                                left join locations_details l on l.location_barcode = sq.location_barcode)
                              """.format(self._table))
            
        
    