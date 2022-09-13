from email.policy import default
from odoo import models, fields, api,_

class Phase(models.Model):
    _name = 'phase.details'
    _description = "Phase Details"
    _rec_name = "phase_name"


    schedule_id = fields.Many2one('schedule.details',string='Schedule',readonly=True)
    phase_name = fields.Char(string='Name')
    date = fields.Date(string='Date')
    
    # def action_location(self):
    #     action = self.env['ir.actions.act_window']._for_xml_id('Inventory.action_locations_details')
    #     action['domain'] = [('phase','=',self.phase_name)]    
    #     # rec = self.env['locations.details'].browse(self._context.get('active_id'))
    #     # rec.phase=self.phase_name
    #     return action
    
    
    def action_location(self):
        action = self.env['ir.actions.act_window']._for_xml_id('Inventory.action_locations_details')
        action['domain'] = [('phase_id','=',self.phase_name)]
        action['context'] = {'default_phase_id':self.id}   
        return action 
      


    