from crypt import methods
import json
from unittest import result
from odoo import http
from odoo.http import request
from datetime import date
# from odoo.addons.Inventory.controllers.login import validate_token

class Schedules(http.Controller):
    
    # @validate_token
    @http.route('/fetch_schedule',type='http', auth='validate_token',method=['GET'], csrf=False)
    def schedule(self):
        print("-----------fetch_schedules-----------------")
        try:
            schedule_rec = http.request.env['schedule.details'].search([])
            rec_schedules=[]
            for rec in schedule_rec:
                vals = {
                    'id' : rec.id,
                    'name' :rec.schedule_name,
                    'store' : rec.store.name
                }
                rec_schedules.append(vals)
            data = {"Code":0, "Message":"retrieve all schedule records", "Result":rec_schedules}
            return json.dumps(data)
        except Exception as e:
            return {"Code":1, "Message":"failed retrieve all schedule records"}
    
    # @validate_token
    @http.route('/schedule',type='json', auth='validate_token',  method=['POST'], csrf=False)
    def schedules(self, **rec):
        try:
            if request.jsonrequest:
                rec = request.jsonrequest
                if rec['schedule_name']:
                    vals = {
                        'schedule_name' :rec['schedule_name'],
                        'store' : rec['store']
                    }
                new_schedule = http.request.env['schedule.details'].sudo().create(vals)
                args = {"Code":"0", "Message":"successfully new record created", "Result":new_schedule.schedule_name}
                print('-------------------',args)
            return args
        except Exception as e:
            return {"Code":"1",'Message':"new record is not created"}
    
    
    # @validate_token
    @http.route('/update_schedules',type='http',auth='validate_token', csrf=False)
    def update_schedule(self, **rec):
        try:
            if request.httprequest:
                if rec['id']:
                    schdules = request.env['schedule.details'].sudo().search([('id', '=', rec['id'])])
                    if schdules:
                        schdules.sudo().write(rec)
                    args = {"Code":"0", "Message":"Bulk update schedule record","Result":rec['id']}
            return json.dumps(args)
        except Exception as e:
            return {"Code":"1",'Message':"record not updated"}
    
    # @validate_token
    @http.route('/delete_schedules/<int:rec_id>',type='http',auth='validate_token', method=['DELETE'], csrf=False)
    def delete_schedule(self, rec_id):
        try:
            schedule_rec = request.env['schedule.details'].sudo().browse(rec_id)
            id = schedule_rec.id 
            schedule_rec.unlink()
            data = data = {"Code":"0", "Message":"Remove record", "Result":id}
            return json.dumps(data)
        except Exception as e:
            return {"Code":"1",'Message':"id is wrong"}
          
    

        
    
    