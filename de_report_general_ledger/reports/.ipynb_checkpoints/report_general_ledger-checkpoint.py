import json
from odoo.exceptions import UserError
from datetime import datetime
from odoo import api, fields, models, _

class GenerateXLSXReport(models.Model):
    _name = 'report.de_report_general_ledger.general_ledger_xlsx'
    _description = 'General Ledger Report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, linesmodel="ir.actions.report",output_format="xlsx",report_name="de_report_general_ledger.general_ledger_xlsx"):
#         raise UserError(data['gl_account'])
        
        f_date = data['from_date']
        f_date = datetime.strptime(f_date, '%Y-%m-%d')
        f_date = f_date.strftime("%d/%m/%Y")
        
        t_date = data['to_date']
        t_date = datetime.strptime(t_date, '%Y-%m-%d')
        t_date = t_date.strftime("%d/%m/%Y")
        
        date = str(f_date) + str(t_date)
        
        format0 = workbook.add_format({'font_size': '12', 'align': 'vcenter', 'bold': True,})
        format1 = workbook.add_format({'font_size': '12', 'align': 'vcenter', 'bold': True, 'bg_color': 'yellow'})

        sheet = workbook.add_worksheet('General Ledger')
        sheet.merge_range('C2:E2', 'General Ledger Report', format0)
        sheet.write(1, 4, 'General Ledger Report', format0)
        sheet.write(3, 0, 'Date', format0)
        sheet.write(3, 1, date, format0)

        sheet.write(6, 0, 'Date', format1)
        sheet.write(6, 1, 'Journal', format1)
        sheet.write(6, 2, 'Partner', format1)
        sheet.write(6, 3, 'Counterpart', format1)
        sheet.write(6, 4, 'Ref', format1)
        sheet.write(6, 5, 'Period', format1)
        sheet.write(6, 6, 'Employee', format1)
        sheet.write(6, 7, 'Department', format1)
        sheet.write(6, 8, 'Project', format1)
        sheet.write(6, 9, 'Cost Center', format1)
        sheet.write(6, 10, 'Move', format1)
        sheet.write(6, 11, 'Label', format1)
        sheet.write(6, 12, 'Debit', format1)
        sheet.write(6, 13, 'Credit', format1)
        sheet.write(6, 14, 'Balance', format1)
        sheet.write(6, 15, 'Currency', format1)
        sheet.write(6, 16, 'Company Curr. Balance', format1)
        sheet.write(6, 17, 'Company Currency', format1)
        format2 = workbook.add_format({'font_size': '12', 'align': 'vcenter'})
        row = 7
        
        move_lines = opening_lines = self.env['account.move.line']
        counter_entries = self.env['account.move']
        counter_account = ''
        
        m_date = ''
        partner = project = employee = department = ccenter = ''
        ibal = bal = comp_bal = 0
        domain = domain_state = ''
        if data['state'] == 'draft':
            domain_state = [('parent_state','=','draft')]
        elif data['state'] == 'posted':
            domain_state = [('parent_state','=','posted')]
        else:
            doamin_state = [('parent_state','in',['draft','posted'])]
            
        if data['account_ids']:
            account_ids = self.env['account.account'].search([('id', 'in', data['account_ids'])])
            for account in account_ids:
                ibal = bal = comp_bal = 0
                domain = domain_state + [('account_id','=',account.id),('date','<',data['from_date'])]
                opening_lines = self.env['account.move.line'].search(domain)
                for line in opening_lines:
                    ibal = ibal + (line.debit - line.credit)
                sheet.merge_range(row, 0, row, 4, (account.code + '-' + account.name), format0)
                sheet.write(row, 13, 'Initial Balance', format0)
                sheet.write(row, 14, ('{:,}'.format(ibal)), format0)
                
                row = row + 1
                #move_lines = self.env['account.move.line'].search([('account_id','=',account.id),('date','>=',data['from_date']),('date','<=',data['to_date'])])
                domain = domain_state + [('account_id','=',account.id),('date','>=',data['from_date']),('date','<=',data['to_date'])]
                move_lines = self.env['account.move.line'].search(domain)
                for line in move_lines:
                    m_date = str(line.date)
                    m_date = datetime.strptime(m_date, '%Y-%m-%d')
                    m_date = m_date.strftime("%d/%m/%Y")
                    bal = bal + ibal + (line.debit - line.credit)
                    
                    if not (line.currency_id.id == line.company_id.currency_id.id):
                        comp_bal = line.currency_id._get_conversion_rate(line.currency_id, line.company_currency_id,line.company_id, fields.date.today()) * bal
                    else:
                        comp_bal = bal
                
                    if line.partner_id:
                        partner = line.partner_id.name
                    if line.project_id:
                        project = line.project_id.name
                    if line.analytic_account_id:
                        ccenter = line.analytic_account_id.name
                    if line.employee_id:
                        employee = line.employee_id.name
                    if line.department_id:
                        department = line.department_id.name
                    
                    counter_entries = self.env['account.move'].search([('id','=',line.move_id.id)])
                    for cline in counter_entries.line_ids.filtered(lambda x: x.account_id.id != line.account_id.id):
                        counter_account = cline.account_id.code + '-' + cline.account_id.name
                        break
                    sheet.write(row, 0, m_date, format2)
                    sheet.write(row, 1, line.journal_id.name, format2)
                    sheet.write(row, 2, partner, format2)
                    sheet.write(row, 3, counter_account, format2)
                    sheet.write(row, 4, line.ref, format2)
                    sheet.write(row, 5, line.account_period, format2)
                    sheet.write(row, 6, employee, format2)
                    sheet.write(row, 7, department, format2)
                    sheet.write(row, 8, project, format2)
                    sheet.write(row, 9, ccenter, format2)
                    sheet.write(row, 10, line.move_id.name, format2)
                    sheet.write(row, 11, line.name, format2)
                    sheet.write(row, 12, ('{:,}'.format(line.debit)), format2)
                    sheet.write(row, 13, ('{:,}'.format(line.credit)), format2)
                    sheet.write(row, 14, ('{:,}'.format(bal)), format2)
                    sheet.write(row, 15, line.currency_id.name, format2)
                    sheet.write(row, 16, ('${:,.2f}'.format(comp_bal)), format2)
                    sheet.write(row, 17, line.company_id.currency_id.name, format2)
                    row = row + 1
            
