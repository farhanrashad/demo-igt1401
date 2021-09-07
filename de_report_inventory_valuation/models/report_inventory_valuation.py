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
        in_date = in_date.strftime("%d/%m/%Y")
        
        format0 = workbook.add_format({'font_size': '12', 'align': 'vcenter', 'bold': True,})
        format1 = workbook.add_format({'font_size': '12', 'align': 'vcenter', 'bold': True, 'bg_color': 'yellow'})
        ###For SPMRF
        sheet = workbook.add_worksheet('Inventory Valuation')
        sheet.merge_range('C2:E2', 'Inventory Valuation', format0)
        sheet.write(1, 4, 'Inventory Valuation', format0)
        sheet.write(3, 0, 'Report On', format0)
        sheet.write(3, 1, in_date, format0)

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
       
        domain = domain1 = domain_mrf = domain_spmrf = ''
        
        products_list = []
        domain = [('in_date','<=',data['in_date'])]
        if data['product_ids']:
            domain += [('product_id','in',data['product_ids'])]
        if data['location_ids']:            
            domain += [('location_id','in',data['location_ids'])]
            
        if data['categ_ids']:
            categ_products_ids = self.env['product.product'].search([('categ_id', 'in', data['categ_ids'])])
            product_ids = tuple([pro_id.id for pro_id in categ_products_ids])
            domain += [('product_id','in',product_ids)]
        
        quant_product_ids = self.env['stock.quant'].search(domain)
        for p in quant_product_ids.product_id:
            if p not in products_list:
                products_list.append(p)
        
        quantity = stock_value = avail_qty = reserved_qty = in_qty = out_qty = min_price = max_price = landed_cost = 0
        
        move_line_ids = self.env['stock.move.line']
        purchase_order_line = self.env['purchase.order.line']
        pickings = self.env['stock.picking']
        stock_valuation_lines = self.env['stock.valuation.adjustment.lines']
        for product in products_list:
            quantity = stock_value = avail_qty = reserved_qty = in_qty = out_qty = min_price = max_price = landed_cost = 0
            domain1 = domain + [('product_id','=',product.id)]
            
            quant_ids = self.env['stock.quant'].search(domain1)
            for quant in quant_ids:
                quantity += quant.quantity
                stock_value += quant.value
                avail_qty += quant.available_quantity
                reserved_qty = quantity - avail_qty
            
            pickings = self.env['stock.picking'].search([('scheduled_date','<=',data['in_date']),('state','=','done')])
            for picking in pickings:
                for line in picking.move_line_ids.filtered(lambda x: x.product_id.id == product.id and x.picking_id.id == picking.id and x.location_id.id in data['location_ids']):
                    out_qty += line.qty_done
                for line in picking.move_line_ids.filtered(lambda x: x.product_id.id == product.id and x.picking_id.id == picking.id and x.location_dest_id.id in data['location_ids']):
                    in_qty += line.qty_done
                    
            stock_valuation_lines = self.env['stock.valuation.adjustment.lines'].search([('product_id','=',product.id)])
            for val in stock_valuation_lines:
                landed_cost += val.additional_landed_cost
                
            purchase_order_line = self.env['purchase.order.line'].search([('product_id','=',product.id),('date_order','<=',data['in_date']),('state','in',['purchase','done'])],order='price_unit',limit=1)
            min_price = purchase_order_line.price_unit
            purchase_order_line = self.env['purchase.order.line'].search([('product_id','=',product.id),('date_order','<=',data['in_date']),('state','in',['purchase','done'])],order='price_unit desc',limit=1)
            max_price = purchase_order_line.price_unit
                
            sheet.write(row, 0, product.default_code, format2)
            sheet.write(row, 1, product.name, format2)
            sheet.write(row, 2, product.categ_id.name, format2)
            sheet.write(row, 3, product.type, format2)
            sheet.write(row, 4, product.uom_id.name, format2)
            sheet.write(row, 5, quantity, format2)
            sheet.write(row, 6, stock_value, format2)
            sheet.write(row, 7, in_qty, format2)
            sheet.write(row, 8, in_qty, format2)
            sheet.write(row, 9, out_qty, format2)
            sheet.write(row, 10, quantity, format2)
            sheet.write(row, 11, stock_value, format2)
            sheet.write(row, 12, landed_cost, format2)
            sheet.write(row, 13, max_price, format2)
            sheet.write(row, 14, min_price, format2)
            sheet.write(row, 15, product.standard_price, format2)
            row = row + 1
        