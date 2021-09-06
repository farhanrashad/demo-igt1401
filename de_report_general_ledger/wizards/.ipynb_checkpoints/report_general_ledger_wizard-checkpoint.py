from odoo import api, fields, models, _
from odoo.exceptions import UserError


class GeneralLedgerWizard(models.TransientModel):
    _name = "general.ledger.wizard"
    _description = 'General Ledger Wizard'
    
    in_date =  fields.Datetime(string='Date')
    
    gl_account = fields.Many2many('account.account')
    
    
    def print_report(self):
        data = {
            'in_date': self.in_date, 
            'gl_account': self.gl_account.ids
        }
        if self.in_date:
            return self.env.ref('de_report_general_ledger.general_ledger_report').report_action(self, data=data)
