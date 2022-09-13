from crypt import methods
import json
from odoo import http
from odoo.http import request
from datetime import datetime
# from odoo.addons.Inventory.controllers.login import validate_token

class Actualstock(http.Controller):
    # @validate_token
    @http.route('/fetch_actualstock',type='http',auth='validate_token',method=['GET'])
    def actualStock(self):
        try:
            actualstock_rec = http.request.env['actual.stock'].search([])
            rec_actualstock=[]
            for rec in actualstock_rec:
                vals = {
                    'id': rec.id,
                    'sku': rec.sku,
                    'barcode': rec.barcode,
                    'date':rec.date,
                    'MAP': rec.MAP,
                    'Quantity':rec.quantity,
                    'schedule_name':rec.schedule_id.schedule_name
                }
                rec_actualstock.append(vals)
                print('******************************',rec_actualstock)
            data = {"Code":0, "Message":"retrieve all actualstock records", "Result":rec_actualstock}
            return json.dumps(data,default=str)
        except Exception as e:
            return {"Code":1, "Message":"failed retrieve all schedule records"}
    
    # @validate_token        
    @http.route('/actualstock',type='json', method=['POST'],auth='validate_token', csrf=False)
    def actualstocks(self, **rec):
        try:
            if request.jsonrequest:
                rec=request.jsonrequest
                if rec['sku']:
                    vals = {
                        'sku' :rec['sku'],
                        'barcode' : rec['barcode'],
                        'date' :datetime.strptime(rec['date'], '%d/%m/%Y'),
                        'MAP' : rec['MAP'],
                        'quantity' : rec['quantity'],
                        'schedule_id' : rec['schedule_id']  
                    }
            new_actualstocks = http.request.env['actual.stock'].sudo().create(vals)
            args = {"Code":0, "Message":"successfully new record created", "Result":new_actualstocks.id}
            print('-------------------',args)
            return args
        except Exception as e:
            return {"Code":"1", "Message":"new record is not created"}
    
    # @validate_token
    @http.route('/update_actualstock',type='http',auth='validate_token', csrf=False)
    def update_actualstock(self, **rec):
        try:
            if request.httprequest:
                if rec['id']:
                    actualstock = request.env['items.details'].sudo().search([('id', '=', rec['id'])])
                    if actualstock:
                        actualstock.sudo().write(rec)
                    print('*************************',actualstock)
                    args = {"Code":0, "Message":"Bulk update actualstock record", "Result":rec['id']}
            return json.dumps(args)
        except Exception as e:
            return {"Code":"1", "Message":"record not updated"}
    
    # @validate_token
    @http.route('/delete_actualstock/<int:rec_id>',type='http',auth='validate_token', method=['DELETE'], csrf=False)
    def delete_actualstock(self, rec_id):
        try:
            actualstock_rec = request.env['items.details'].sudo().browse(rec_id)
            id = actualstock_rec.id 
            actualstock_rec.unlink()
            data = data = {"status":"0","message":"Remove record","id":id}
            return json.dumps(data)
        except Exception as e:
            return {"Code":"1", "Message":"record not deleted"}