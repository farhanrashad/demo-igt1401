import json
from odoo import models
from odoo.exceptions import UserError
from datetime import datetime


class GenerateXLSXReport(models.Model):
    _name = 'report.de_report_inventory_valuation.report_inventory_valuation'
    _description = 'Inventory Valuation Report Report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        in_date = data['in_date']
        in_date = datetime.strptime(in_date, '%Y-%m-%d %H:%M:%S')
        in_date = in_date.strftime("%Y/%m/%d")
        
        format1 = workbook.add_format({'font_size': '12', 'align': 'vcenter', 'bold': True})
        ###For SPMRF
        sheet = workbook.add_worksheet('Inventory Valuation')
        sheet.merge_range('C2:E2', 'Inventory Valuation', format1)
        sheet.write(1, 4, 'Inventory Valuation', format1)
        sheet.write(3, 0, 'Date From', format1)
        sheet.write(3, 1, start_date, format1)
        sheet.write(4, 0, 'Date To', format1)
        sheet.write(4, 1, end_date, format1)

        sheet.write(6, 0, 'Product Reference', format1)
        sheet.write(6, 1, 'Product Name', format1)
        sheet.write(6, 2, 'Category', format1)
        sheet.write(6, 3, 'Product Type', format1)
        sheet.write(6, 4, 'UOM', format1)
        sheet.write(6, 5, 'Total Stock Quantity', format1)
        sheet.write(6, 6, 'Total Stock Value', format1)
        sheet.write(6, 7, 'Stock Location', format1)
        sheet.write(6, 8, 'In Qunatity', format1)
        sheet.write(6, 9, 'Out Quantity', format1)
        sheet.write(6, 10, 'Quantity', format1)
        sheet.write(6, 11, 'Value', format1)
        sheet.write(6, 12, 'Landed Cost', format1)
        sheet.write(6, 13, 'MAX Cost', format1)
        sheet.write(6, 14, 'MIN Cost', format1)
        sheet.write(6, 15, 'AVG. Cost', format1)
        
        
        
        format2 = workbook.add_format({'font_size': '12', 'align': 'vcenter'})
        row = 7
        row1 = 7
        row2 = 7
        domain = ''
        if data['categ_ids']:
            domain = [('account_id', '=', line.analytic_account_id.id),
                      ('date', '>=', date_from),
                      ('date', '<=', date_to),
                     ]
        if data['location_ids']:
            domain += [('general_account_id', 'in', acc_ids)]
        if data['product_ids']:
            domain += [('general_account_id', 'in', acc_ids)]
                    
        #quant_ids = self.env['stock.quant'].search([('date_order','>=',data['start_date']),('date_order','<=',data['end_date'])])
        quant_ids = self.env['stock.quant'].search([])
        for quant in quant_ids:
            sheet.write(row, 0, quant.product_id.default_code, format2)
            sheet.write(row, 1, quant.product_id.name, format2)
            sheet.write(row, 2, quant.product_id.categ_id.name, format2)
            sheet.write(row, 3, quant.product_id.type, format2)
            sheet.write(row, 4, quant.product_id.uom_id.name, format2)
            sheet.write(row, 5, quant.quantity, format2)
            sheet.write(row, 6, quant.value, format2)
            sheet.write(row, 7, quant.location_id.name, format2)
            row = row + 1