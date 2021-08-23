from odoo import models, api


class PurchaseBudget(models.Model):
    _inherit = 'purchase.budget'

    def print_purchase_budget_report(self):
        data = {
            'id': self.id
        }
        return self.env.ref('de_report_purchase_budget.report_purchase_budget_xlsx_1').report_action(self, data=data)
