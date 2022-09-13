from crypt import methods
import json
from odoo import http
from odoo.http import request
from datetime import date
# from odoo.addons.Inventory.controllers.login import validate_token


class Items(http.Controller):
    
    # @validate_token
    @http.route('/fetch_items',type='http',auth='validate_token',method=['GET'])
    def item(self):
        try:
            items_rec = http.request.env['items.details'].search([])
            rec_items=[]
            for rec in items_rec:
                vals = {
                    'id': rec.id,
                    'name':rec.items_name,
                    'sku': rec.sku,
                    'description':rec.description,
                    'barcode': rec.barcode,
                    'MAP': rec.MAP
                }
                rec_items.append(vals)
                print('******************************',rec_items)
            data = {"Code":"0", "Message":"successfully new record created", "Result":rec_items}
            return json.dumps(data,default=str)
        except Exception as e:
            return {"Code":1, "Message":"new record is not created"}


    
    # @validate_token    
    @http.route('/item',type='json', method=['POST'],auth='validate_token', csrf=False)
    def item(self, **rec):
        try:
            if request.jsonrequest:
                rec=request.jsonrequest
                if rec['items_name']:
                    vals = {
                        'items_name' :rec['items_name'],
                        'sku' : rec['sku'],
                        'description' :rec['description'],
                        'barcode' : rec['barcode'],
                        'MAP' : rec['MAP']
                        }
            new_item = http.request.env['items.details'].sudo().create(vals)
            args = {"Code":0, "Message":"Bulk update items record", "Result":new_item.id}
            print('-------------------',args)
            return args
        except Exception as e:
            return {"Code":1, "Message":"record not updated"}
    
    # @validate_token        
    @http.route('/update_items',type='http',auth='validate_token', csrf=False)
    def update_items(self, **rec):
        try:
            if request.httprequest:
                if rec['id']:
                    items = request.env['items.details'].sudo().search([('id', '=', rec['id'])])
                    if items:
                        items.sudo().write(rec)
                    print('*************************',items)
                    args = {"Code":0, "Message":"retrieve all Phase records", "Result":rec['id']}
            return json.dumps(args)
        except Exception as e:
            return {"Code":1, "Message":" faild retrieve all records"}
    
    # @validate_token    
    @http.route('/delete_items/<int:rec_id>',type='http',auth='validate_token', method=['DELETE'], csrf=False)
    def delete_items(self, rec_id):
        try:
            items_rec = request.env['items.details'].sudo().browse(rec_id)
            id = items_rec.id 
            items_rec.unlink()
            data = data = {"Code":0, "Message":"Remove record", "Result":id}
            return json.dumps(data)
        except Exception as e:
            return {"Code":1,'Message':"id is wrong"}