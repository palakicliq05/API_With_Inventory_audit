from crypt import methods
import json
from odoo import http
from odoo.http import request
from datetime import date
# from odoo.addons.Inventory.controllers.login import validate_token

class Locations(http.Controller):
    # @validate_token
    @http.route('/fetch_location',type='http', auth='validate_token', method=['GET'])
    def location(self):
        try:
            location_rec = http.request.env['locations.details'].search([])
            rec_location=[]
            for rec in location_rec:
                vals = {
                    'id': rec.id,
                    'name' :rec.description,
                    'location_barcode' : rec.location_barcode,
                    'stock_auditor' :rec.stock_auditor.name,
                    'phase' : rec.phase_id.phase_name
                }
                rec_location.append(vals)
            data = {"Code":"0", "Message":"retrieve all location records", "Result":rec_location}
            return json.dumps(data,default=str)
        except Exception as e:
            return {"Code":1, "Message":"failed retrieve all location records"}
    
    # @validate_token    
    @http.route('/location',type='json', auth='validate_token' ,  method=['POST'], csrf=False)
    def PostSchedules(self, **rec):
        try:
            if request.jsonrequest:
                rec=request.jsonrequest
                if rec['description']:
                    vals = {
                        'description' :rec['description'],
                        'location_barcode' : rec['location_barcode'],
                        'stock_auditor' :rec['stock_auditor'],
                        'phase_id' : rec['phase_id']
                    }
            new_location = http.request.env['locations.details'].sudo().create(vals)
            args = {"Code":0, "Message":"successfully new record created", "Result": new_location.id}
            print('-------------------',args)
            return args
        except Exception as e:
            return {"Code":"1", "Message":"new record is not created"}
    
    # @validate_token    
    @http.route('/update_locations',type='http', auth='validate_token', csrf=False)
    def update_locations(self, **rec):
        try:
            print('-----------------',rec)
            if request.httprequest:
                if rec['id']:
                    locations = request.env['locations.details'].sudo().search([('id', '=', rec['id'])])
                    if locations:
                        locations.sudo().write(rec)
                    print('*************************',locations)
                    args = {"Code":0, "message":"Bulk update location record",'Result':rec['id']}
            return json.dumps(args)
        except Exception as e:
            return {"Code":1, "Message":"record not updated"}
    
    # @validate_token
    @http.route('/delete_locations/<int:rec_id>',type='http', auth='validate_token', method=['DELETE'], csrf=False)
    def delete_schedule(self, rec_id):
        try:
            locations_rec = request.env['locations.details'].sudo().browse(rec_id)
            id = locations_rec.id 
            locations_rec.unlink()
            data = data = {"Code":0,"Message":"Remove record","Result":id}
            return json.dumps(data)
        except Exception as e:
            return {'Code':1,'Message':"id is wrong"}