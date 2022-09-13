from multiprocessing import context
from odoo import models, fields, api,_

class Schedule(models.Model):
    _name = 'schedule.details'
    _description = "Schedule Details"
    _rec_name = "schedule_name"


    schedule_name = fields.Char(string='Description')
    store = fields.Many2one('res.partner',string='Store')
    
    

    def action_phase(self):
        action = self.env['ir.actions.act_window']._for_xml_id('Inventory.action_phase_details')
        action['domain'] = [('schedule_id','=',self.schedule_name)] 
        action['context'] = {'default_schedule_id':self.id}  
        return action   
           
    def action_actual_stock(self):
        action = self.env['ir.actions.act_window']._for_xml_id('Inventory.action_actual_stock')
        action['domain'] = [('schedule_id','=',self.schedule_name)] 
        action['context'] = {'default_schedule_id':self.id}  
        return action 
        
    def action_scanned(self):
        action = self.env['ir.actions.act_window']._for_xml_id('Inventory.action_scanned_data')
        action['domain'] = [('schedule_id','=',self.schedule_name)]  
        action['context'] = {'default_schedule_id':self.id} 
        return action 