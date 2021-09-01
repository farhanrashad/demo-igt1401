import json
from odoo import models
from odoo.exceptions import UserError
from datetime import datetime


class GenerateXLSXReport(models.Model):
    _name = 'report.de_report_general_ledger.general_ledger_xlsx'
    _description = 'General Ledger Report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, linesmodel="ir.actions.report",output_format="xlsx",report_name="de_report_general_ledger.general_ledger_xlsx"):
#         raise UserError(data['gl_account'])
        
        in_date = data['in_date']
        in_date = datetime.strptime(in_date, '%Y-%m-%d %H:%M:%S')
        in_date = in_date.strftime("%Y/%m/%d")
        
        format1 = workbook.add_format({'font_size': '12', 'align': 'vcenter', 'bold': True})
        ###For SPMRF
        sheet = workbook.add_worksheet('General Ledger')
        sheet.merge_range('C2:E2', 'General Ledger Report', format1)
        sheet.write(1, 4, 'General Ledger Report', format1)
        sheet.write(3, 0, 'Date', format1)
        sheet.write(3, 1, in_date, format1)

        sheet.write(6, 0, 'Name', format1)
        sheet.write(6, 1, 'Date', format1)
        sheet.write(6, 2, 'Communication', format1)
        sheet.write(6, 3, 'Partner', format1)
        sheet.write(6, 4, 'Currency', format1)
        sheet.write(6, 5, 'Debit', format1)
        sheet.write(6, 6, 'Credit', format1)
        sheet.write(6, 7, 'Balance', format1)
        
        format2 = workbook.add_format({'font_size': '12', 'align': 'vcenter'})
        row = 7
        row1 = 7
        row2 = 7
        domain = ''
        if data['gl_account']:
            domain = [('id', 'in',data['gl_account'])
                     ]
            
        account_ids = self.env['account.account'].search(domain)
        #raise UserError(account_ids)
        for account in account_ids:
            account_name = account.code + " " + account.name
            domain1 = [('account_id','=',account_name),
                       ('date','<=', data['in_date'])
                      ]
            account_lines = self.env['account.move.line'].search(domain1)
            debit  = 0
            credit = 0
            balance = 0
            for line in account_lines:
                #raise UserError(line.debit)
                debit += line.debit
                credit += line.credit
            balance = debit - credit
            sheet.write(row, 0, account_name, format2)
#             sheet.write(row, 1, quant.product_id.name, format2)
#             sheet.write(row, 2, quant.product_id.categ_id.name, format2)
#             sheet.write(row, 3, quant.product_id.type, format2)
#             sheet.write(row, 4, quant.product_id.uom_id.name, format2)
            sheet.write(row, 5, debit, format2)
            sheet.write(row, 6, credit, format2)
            sheet.write(row, 7, balance, format2)
            row = row + 1
            
