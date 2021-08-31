import json
from odoo import models
from odoo.exceptions import UserError
from datetime import datetime


class GenerateXLSXReport(models.Model):
    _name = 'report.de_report_inventory_availability.xlsx'
    _description = 'Inventory Availability Report Report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        in_date = data['in_date']
        in_date = datetime.strptime(in_date, '%Y-%m-%d %H:%M:%S')
        in_date = in_date.strftime("%Y/%m/%d")
        
        format1 = workbook.add_format({'font_size': '12', 'align': 'vcenter', 'bold': True})
        ###For SPMRF
        sheet = workbook.add_worksheet('Inventory Availability')
        sheet.merge_range('C2:E2', 'Inventory Availability', format1)
        sheet.write(1, 4, 'Inventory Valuation', format1)
        sheet.write(3, 0, 'Date From', format1)
        sheet.write(3, 1, in_date, format1)

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
            domain = [('categ_id', 'in',data['categ_ids']),
                      ('in_date', '<=', data['in_date'])
                     ]
        if data['location_ids']:
            domain = [('location_id', 'in', data['location_ids']),
                      ('in_date', '<=', data['in_date'])
                     ]
        if data['productids']:
            domain = [('product_id', 'in', data['productids']),
                     ('in_date', '<=', data['in_date'])]
                    
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
            
            
        #---------------------------below is the sample code for gorup by product data -----------------
        """
        p = self.env['model_of_product'].search([])


_product=[]
# collect all product id
for product in p:
    _product.append(product.id)

box = []
for _p in _product:
    domain = [  ('date', '=', specific_date),
                ('product_id', '=', _p)]
    record = self.env['stock.move'].search(domain)
    sum_of_stock = 0
    sum_of_client = 0
    # box will contain sets of [product_id, sum_of_stock, sum_of_client ]
    for rec in record.search([('name', '=', 'Clients')]):
        sum_of_client = sum_of_client + rec.product_uom_quantity
    for rec in record.search([('name', '=', 'Stock')]):
        sum_of_stock = sum_of_stock + rec.product_uom_quantity

    box.append([_p, sum_of_stock, sum_of_client])
return box
        """