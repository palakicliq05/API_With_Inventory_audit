from crypt import methods
import json
from re import A
from telnetlib import STATUS
from odoo import http
from odoo.http import request
from datetime import datetime
# from odoo.addons.Inventory.controllers.login import validate_token


class Phase(http.Controller):
    # @validate_token
    @http.route('/fetch_phase',type='http',auth='validate_token',method=['GET'])
    def get_phase(self):
        try:
            phase_rec = http.request.env['phase.details'].search([])
            rec_phase=[]
            for rec in phase_rec:
                vals = {
                    'id': rec.id,
                    'name' :rec.phase_name,
                    'date' : rec.date,
                    'schedule' : rec.schedule_id.schedule_name
                }
                rec_phase.append(vals)
                print('******************************',rec_phase)
            data = {"Code":0, "Message":"retrieve all Phase records", "Result":rec_phase}
            print("---------------------0",data)
            return json.dumps(data,default=str)
        except Exception as e:
            return {"Code":1, "Message":"failed retrieve all phase records"}
    
    # @validate_token
    @http.route('/phase',type='json',auth='validate_token', method=['POST'], csrf=False)
    def phase(self, **rec):
        try:
            if request.jsonrequest:
                rec=request.jsonrequest
                if rec['phase_name']:
                    vals = {
                        'phase_name' :rec['phase_name'],
                        'date' :datetime.strptime(rec['date'], '%d/%m/%Y'),
                        'schedule_id':rec['schedule_id']                   
                    }
            new_phase =http.request.env['phase.details'].sudo().create(vals)
            args ={"Code":0, "Message":"successfully new record created", "Result":new_phase.id}
            print('-------------------',args)
            return args
        except Exception as e:
            return {"code":1,'Message':"new record is not created","Error":e}
    
    # @validate_token    
    @http.route('/update_phase',type='http',auth='validate_token', csrf=False)
    def update_phase(self, **rec):
        try:
            if request.httprequest:
                if rec['id']:
                    phase = request.env['phase.details'].sudo().search([('id', '=', rec['id'])])
                    if phase:
                        phase.sudo().write(rec)
                    print('*************************',phase)
                    args = {"Code":"0", "Message":"Bulk update Phase record","Result":rec['id']}
            return json.dumps(args)
        except Exception as e:
            return {"code":"1",'Message':"record not updated"}
    
    
    # @validate_token
    @http.route('/delete_phase/<int:rec_id>',type='http',auth='validate_token', method=['DELETE'], csrf=False)
    def delete_phase(self, rec_id):
        try:
            phase_rec = request.env['phase.details'].sudo().browse(rec_id)
            id = phase_rec.id 
            phase_rec.unlink()
            data = data = {"Code":"0", "Message":"Remove record","Result":id}
            return json.dumps(data)
        except Exception as e:
            return {"code":"1",'Message':"something is wrong"}