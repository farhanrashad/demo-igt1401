from odoo import models
from odoo.exceptions import UserError


class GenerateXLSXReport(models.Model):
    _name = 'report.de_report_purchase_budget.report_purchase_budget'
    _description = 'Purchase Budget Report XLSX'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines,model="ir.actions.report",output_format="xlsx",report_name="de_report_purchase_budget.report_purchase_budget"):
        
        format1 = workbook.add_format({'font_size': '12', 'align': 'vcenter', 'bold': True})
        
        sheet1 = workbook.add_worksheet('January')
        sheet1.write(3, 0, 'Department', format1)
        sheet1.write(3, 1, 'Budget Reference', format1)
        sheet1.write(3, 2, 'Duration', format1)
        sheet1.write(3, 3, 'Month', format1)
        sheet1.write(3, 4, 'Capitalisation', format1)
        sheet1.write(3, 5, 'Category', format1)
        sheet1.write(3, 6, 'Line Budget', format1)
        sheet1.write(3, 7, 'Allocated QTY', format1)
        sheet1.write(3, 8, 'Allocated Unit Price', format1)
        sheet1.write(3, 9, 'Allocated Amount', format1)
        sheet1.write(3, 10, 'Used QTY', format1)
        sheet1.write(3, 11, 'Used Amount', format1)
        sheet1.write(3, 12, 'Available QTY', format1)
        sheet1.write(3, 13, 'Available Amount', format1)
 
        sheet2 = workbook.add_worksheet('February')
        sheet2.write(3, 0, 'Department', format1)
        sheet2.write(3, 1, 'Budget Reference', format1)
        sheet2.write(3, 2, 'Duration', format1)
        sheet2.write(3, 3, 'Month', format1)
        sheet2.write(3, 4, 'Capitalisation', format1)
        sheet2.write(3, 5, 'Category', format1)
        sheet2.write(3, 6, 'Line Budget', format1)
        sheet2.write(3, 7, 'Allocated QTY', format1)
        sheet2.write(3, 8, 'Allocated Unit Price', format1)
        sheet2.write(3, 9, 'Allocated Amount', format1)
        sheet2.write(3, 10, 'Used QTY', format1)
        sheet2.write(3, 11, 'Used Amount', format1)
        sheet2.write(3, 12, 'Available QTY', format1)
        sheet2.write(3, 13, 'Available Amount', format1)
        
        sheet3 = workbook.add_worksheet('March')
        sheet3.write(3, 0, 'Department', format1)
        sheet3.write(3, 1, 'Budget Reference', format1)
        sheet3.write(3, 2, 'Duration', format1)
        sheet3.write(3, 3, 'Month', format1)
        sheet3.write(3, 4, 'Capitalisation', format1)
        sheet3.write(3, 5, 'Category', format1)
        sheet3.write(3, 6, 'Line Budget', format1)
        sheet3.write(3, 7, 'Allocated QTY', format1)
        sheet3.write(3, 8, 'Allocated Unit Price', format1)
        sheet3.write(3, 9, 'Allocated Amount', format1)
        sheet3.write(3, 10, 'Used QTY', format1)
        sheet3.write(3, 11, 'Used Amount', format1)
        sheet3.write(3, 12, 'Available QTY', format1)
        sheet3.write(3, 13, 'Available Amount', format1)
        
        sheet4 = workbook.add_worksheet('April')
        sheet4.write(3, 0, 'Department', format1)
        sheet4.write(3, 1, 'Budget Reference', format1)
        sheet4.write(3, 2, 'Duration', format1)
        sheet4.write(3, 3, 'Month', format1)
        sheet4.write(3, 4, 'Capitalisation', format1)
        sheet4.write(3, 5, 'Category', format1)
        sheet4.write(3, 6, 'Line Budget', format1)
        sheet4.write(3, 7, 'Allocated QTY', format1)
        sheet4.write(3, 8, 'Allocated Unit Price', format1)
        sheet4.write(3, 9, 'Allocated Amount', format1)
        sheet4.write(3, 10, 'Used QTY', format1)
        sheet4.write(3, 11, 'Used Amount', format1)
        sheet4.write(3, 12, 'Available QTY', format1)
        sheet4.write(3, 13, 'Available Amount', format1)
        
        sheet5 = workbook.add_worksheet('May')
        sheet5.write(3, 0, 'Department', format1)
        sheet5.write(3, 1, 'Budget Reference', format1)
        sheet5.write(3, 2, 'Duration', format1)
        sheet5.write(3, 3, 'Month', format1)
        sheet5.write(3, 4, 'Capitalisation', format1)
        sheet5.write(3, 5, 'Category', format1)
        sheet5.write(3, 6, 'Line Budget', format1)
        sheet5.write(3, 7, 'Allocated QTY', format1)
        sheet5.write(3, 8, 'Allocated Unit Price', format1)
        sheet5.write(3, 9, 'Allocated Amount', format1)
        sheet5.write(3, 10, 'Used QTY', format1)
        sheet5.write(3, 11, 'Used Amount', format1)
        sheet5.write(3, 12, 'Available QTY', format1)
        sheet5.write(3, 13, 'Available Amount', format1)
        
        sheet6 = workbook.add_worksheet('June')
        sheet6.write(3, 0, 'Department', format1)
        sheet6.write(3, 1, 'Budget Reference', format1)
        sheet6.write(3, 2, 'Duration', format1)
        sheet6.write(3, 3, 'Month', format1)
        sheet6.write(3, 4, 'Capitalisation', format1)
        sheet6.write(3, 5, 'Category', format1)
        sheet6.write(3, 6, 'Line Budget', format1)
        sheet6.write(3, 7, 'Allocated QTY', format1)
        sheet6.write(3, 8, 'Allocated Unit Price', format1)
        sheet6.write(3, 9, 'Allocated Amount', format1)
        sheet6.write(3, 10, 'Used QTY', format1)
        sheet6.write(3, 11, 'Used Amount', format1)
        sheet6.write(3, 12, 'Available QTY', format1)
        sheet6.write(3, 13, 'Available Amount', format1)
        
        sheet7 = workbook.add_worksheet('July')
        sheet7.write(3, 0, 'Department', format1)
        sheet7.write(3, 1, 'Budget Reference', format1)
        sheet7.write(3, 2, 'Duration', format1)
        sheet7.write(3, 3, 'Month', format1)
        sheet7.write(3, 4, 'Capitalisation', format1)
        sheet7.write(3, 5, 'Category', format1)
        sheet7.write(3, 6, 'Line Budget', format1)
        sheet7.write(3, 7, 'Allocated QTY', format1)
        sheet7.write(3, 8, 'Allocated Unit Price', format1)
        sheet7.write(3, 9, 'Allocated Amount', format1)
        sheet7.write(3, 10, 'Used QTY', format1)
        sheet7.write(3, 11, 'Used Amount', format1)
        sheet7.write(3, 12, 'Available QTY', format1)
        sheet7.write(3, 13, 'Available Amount', format1)
        
        sheet8 = workbook.add_worksheet('August')
        sheet8.write(3, 0, 'Department', format1)
        sheet8.write(3, 1, 'Budget Reference', format1)
        sheet8.write(3, 2, 'Duration', format1)
        sheet8.write(3, 3, 'Month', format1)
        sheet8.write(3, 4, 'Capitalisation', format1)
        sheet8.write(3, 5, 'Category', format1)
        sheet8.write(3, 6, 'Line Budget', format1)
        sheet8.write(3, 7, 'Allocated QTY', format1)
        sheet8.write(3, 8, 'Allocated Unit Price', format1)
        sheet8.write(3, 9, 'Allocated Amount', format1)
        sheet8.write(3, 10, 'Used QTY', format1)
        sheet8.write(3, 11, 'Used Amount', format1)
        sheet8.write(3, 12, 'Available QTY', format1)
        sheet8.write(3, 13, 'Available Amount', format1)
        
        sheet9 = workbook.add_worksheet('September')
        sheet9.write(3, 0, 'Department', format1)
        sheet9.write(3, 1, 'Budget Reference', format1)
        sheet9.write(3, 2, 'Duration', format1)
        sheet9.write(3, 3, 'Month', format1)
        sheet9.write(3, 4, 'Capitalisation', format1)
        sheet9.write(3, 5, 'Category', format1)
        sheet9.write(3, 6, 'Line Budget', format1)
        sheet9.write(3, 7, 'Allocated QTY', format1)
        sheet9.write(3, 8, 'Allocated Unit Price', format1)
        sheet9.write(3, 9, 'Allocated Amount', format1)
        sheet9.write(3, 10, 'Used QTY', format1)
        sheet9.write(3, 11, 'Used Amount', format1)
        sheet9.write(3, 12, 'Available QTY', format1)
        sheet9.write(3, 13, 'Available Amount', format1)
        
        sheet10 = workbook.add_worksheet('October')
        sheet10.write(3, 0, 'Department', format1)
        sheet10.write(3, 1, 'Budget Reference', format1)
        sheet10.write(3, 2, 'Duration', format1)
        sheet10.write(3, 3, 'Month', format1)
        sheet10.write(3, 4, 'Capitalisation', format1)
        sheet10.write(3, 5, 'Category', format1)
        sheet10.write(3, 6, 'Line Budget', format1)
        sheet10.write(3, 7, 'Allocated QTY', format1)
        sheet10.write(3, 8, 'Allocated Unit Price', format1)
        sheet10.write(3, 9, 'Allocated Amount', format1)
        sheet10.write(3, 10, 'Used QTY', format1)
        sheet10.write(3, 11, 'Used Amount', format1)
        sheet10.write(3, 12, 'Available QTY', format1)
        sheet10.write(3, 13, 'Available Amount', format1)
        
        sheet11 = workbook.add_worksheet('November')
        sheet11.write(3, 0, 'Department', format1)
        sheet11.write(3, 1, 'Budget Reference', format1)
        sheet11.write(3, 2, 'Duration', format1)
        sheet11.write(3, 3, 'Month', format1)
        sheet11.write(3, 4, 'Capitalisation', format1)
        sheet11.write(3, 5, 'Category', format1)
        sheet11.write(3, 6, 'Line Budget', format1)
        sheet11.write(3, 7, 'Allocated QTY', format1)
        sheet11.write(3, 8, 'Allocated Unit Price', format1)
        sheet11.write(3, 9, 'Allocated Amount', format1)
        sheet11.write(3, 10, 'Used QTY', format1)
        sheet11.write(3, 11, 'Used Amount', format1)
        sheet11.write(3, 12, 'Available QTY', format1)
        sheet11.write(3, 13, 'Available Amount', format1)
        
        sheet12 = workbook.add_worksheet('December')
        sheet12.write(3, 0, 'Department', format1)
        sheet12.write(3, 1, 'Budget Reference', format1)
        sheet12.write(3, 2, 'Duration', format1)
        sheet12.write(3, 3, 'Month', format1)
        sheet12.write(3, 4, 'Capitalisation', format1)
        sheet12.write(3, 5, 'Category', format1)
        sheet12.write(3, 6, 'Line Budget', format1)
        sheet12.write(3, 7, 'Allocated QTY', format1)
        sheet12.write(3, 8, 'Allocated Unit Price', format1)
        sheet12.write(3, 9, 'Allocated Amount', format1)
        sheet12.write(3, 10, 'Used QTY', format1)
        sheet12.write(3, 11, 'Used Amount', format1)
        sheet12.write(3, 12, 'Available QTY', format1)
        sheet12.write(3, 13, 'Available Amount', format1)
        
        sheet = workbook.add_worksheet('Total')
        sheet.write(3, 0, 'Department', format1)
        sheet.write(3, 1, 'Budget Reference', format1)
        sheet.write(3, 2, 'Duration', format1)
        sheet.write(3, 3, 'Month', format1)
        sheet.write(3, 4, 'Capitalisation', format1)
        sheet.write(3, 5, 'Category', format1)
        sheet.write(3, 6, 'Line Budget', format1)
        sheet.write(3, 7, 'Allocated QTY', format1)
        sheet.write(3, 8, 'Allocated Unit Price', format1)
        sheet.write(3, 9, 'Allocated Amount', format1)
        sheet.write(3, 10, 'Used QTY', format1)
        sheet.write(3, 11, 'Used Amount', format1)
        sheet.write(3, 12, 'Available QTY', format1)
        sheet.write(3, 13, 'Available Amount', format1)
  

        format2 = workbook.add_format({'font_size': '12', 'align': 'vcenter'})
        row = 4
        sheet.set_column(row, 0, 50)
        sheet.set_column(row, 1, 25)
        sheet.set_column(row, 2, 20)
        sheet.set_column(row, 3, 20)
        sheet.set_column(row, 4, 20)
        sheet.set_column(row, 5, 20)
        sheet.set_column(row, 6, 20)
        sheet.set_column(row, 7, 20)
        sheet.set_column(row, 8, 20)
        sheet.set_column(row, 9, 20)
        sheet.set_column(row, 10, 20)
        sheet.set_column(row, 11, 20)
        sheet.set_column(row, 12, 20)
        sheet.set_column(row, 13, 20)
        
        row1 = 4
        sheet1.set_column(row1, 0, 50)
        sheet1.set_column(row1, 1, 25)
        sheet1.set_column(row1, 2, 20)
        sheet1.set_column(row1, 3, 20)
        sheet1.set_column(row1, 4, 20)
        sheet1.set_column(row1, 5, 20)
        sheet1.set_column(row1, 6, 20)
        sheet1.set_column(row1, 7, 20)
        sheet1.set_column(row1, 8, 20)
        sheet1.set_column(row1, 9, 20)
        sheet1.set_column(row1, 10, 20)
        sheet1.set_column(row1, 11, 20)
        sheet1.set_column(row1, 12, 20)
        sheet1.set_column(row1, 13, 20)
        
        row2 = 4
        sheet2.set_column(row2, 0, 50)
        sheet2.set_column(row2, 1, 25)
        sheet2.set_column(row2, 2, 20)
        sheet2.set_column(row2, 3, 20)
        sheet2.set_column(row2, 4, 20)
        sheet2.set_column(row2, 5, 20)
        sheet2.set_column(row2, 6, 20)
        sheet2.set_column(row2, 7, 20)
        sheet2.set_column(row2, 8, 20)
        sheet2.set_column(row2, 9, 20)
        sheet2.set_column(row2, 10, 20)
        sheet2.set_column(row2, 11, 20)
        sheet2.set_column(row2, 12, 20)
        sheet2.set_column(row2, 13, 20)
       
        row3 = 4
        sheet3.set_column(row3, 0, 50)
        sheet3.set_column(row3, 1, 25)
        sheet3.set_column(row3, 2, 20)
        sheet3.set_column(row3, 3, 20)
        sheet3.set_column(row3, 4, 20)
        sheet3.set_column(row3, 5, 20)
        sheet3.set_column(row3, 6, 20)
        sheet3.set_column(row3, 7, 20)
        sheet3.set_column(row3, 8, 20)
        sheet3.set_column(row3, 9, 20)
        sheet3.set_column(row3, 10, 20)
        sheet3.set_column(row3, 11, 20)
        sheet3.set_column(row3, 12, 20)
        sheet3.set_column(row3, 13, 20)
       
        row4 = 4
        sheet4.set_column(row4, 0, 50)
        sheet4.set_column(row4, 1, 25)
        sheet4.set_column(row4, 2, 20)
        sheet4.set_column(row4, 3, 20)
        sheet4.set_column(row4, 4, 20)
        sheet4.set_column(row4, 5, 20)
        sheet4.set_column(row4, 6, 20)
        sheet4.set_column(row4, 7, 20)
        sheet4.set_column(row4, 8, 20)
        sheet4.set_column(row4, 9, 20)
        sheet4.set_column(row4, 10, 20)
        sheet4.set_column(row4, 11, 20)
        sheet4.set_column(row4, 12, 20)
        sheet4.set_column(row4, 13, 20)
        
        row5 = 4
        sheet5.set_column(row5, 0, 50)
        sheet5.set_column(row5, 1, 25)
        sheet5.set_column(row5, 2, 20)
        sheet5.set_column(row5, 3, 20)
        sheet5.set_column(row5, 4, 20)
        sheet5.set_column(row5, 5, 20)
        sheet5.set_column(row5, 6, 20)
        sheet5.set_column(row5, 7, 20)
        sheet5.set_column(row5, 8, 20)
        sheet5.set_column(row5, 9, 20)
        sheet5.set_column(row5, 10, 20)
        sheet5.set_column(row5, 11, 20)
        sheet5.set_column(row5, 12, 20)
        sheet5.set_column(row5, 13, 20)
        
        row6 = 4
        sheet6.set_column(row6, 0, 50)
        sheet6.set_column(row6, 1, 25)
        sheet6.set_column(row6, 2, 20)
        sheet6.set_column(row6, 3, 20)
        sheet6.set_column(row6, 4, 20)
        sheet6.set_column(row6, 5, 20)
        sheet6.set_column(row6, 6, 20)
        sheet6.set_column(row6, 7, 20)
        sheet6.set_column(row6, 8, 20)
        sheet6.set_column(row6, 9, 20)
        sheet6.set_column(row6, 10, 20)
        sheet6.set_column(row6, 11, 20)
        sheet6.set_column(row6, 12, 20)
        sheet6.set_column(row6, 13, 20)
        
        row7 = 4
        sheet7.set_column(row7, 0, 50)
        sheet7.set_column(row7, 1, 25)
        sheet7.set_column(row7, 2, 20)
        sheet7.set_column(row7, 3, 20)
        sheet7.set_column(row7, 4, 20)
        sheet7.set_column(row7, 5, 20)
        sheet7.set_column(row7, 6, 20)
        sheet7.set_column(row7, 7, 20)
        sheet7.set_column(row7, 8, 20)
        sheet7.set_column(row7, 9, 20)
        sheet7.set_column(row7, 10, 20)
        sheet7.set_column(row7, 11, 20)
        sheet7.set_column(row7, 12, 20)
        sheet7.set_column(row7, 13, 20)
        
        row8 = 4
        sheet8.set_column(row8, 0, 50)
        sheet8.set_column(row8, 1, 25)
        sheet8.set_column(row8, 2, 20)
        sheet8.set_column(row8, 3, 20)
        sheet8.set_column(row8, 4, 20)
        sheet8.set_column(row8, 5, 20)
        sheet8.set_column(row8, 6, 20)
        sheet8.set_column(row8, 7, 20)
        sheet8.set_column(row8, 8, 20)
        sheet8.set_column(row8, 9, 20)
        sheet8.set_column(row8, 10, 20)
        sheet8.set_column(row8, 11, 20)
        sheet8.set_column(row8, 12, 20)
        sheet8.set_column(row8, 13, 20)
        
        row9 = 4
        sheet9.set_column(row9, 0, 50)
        sheet9.set_column(row9, 1, 25)
        sheet9.set_column(row9, 2, 20)
        sheet9.set_column(row9, 3, 20)
        sheet9.set_column(row9, 4, 20)
        sheet9.set_column(row9, 5, 20)
        sheet9.set_column(row9, 6, 20)
        sheet9.set_column(row9, 7, 20)
        sheet9.set_column(row9, 8, 20)
        sheet9.set_column(row9, 9, 20)
        sheet9.set_column(row9, 10, 20)
        sheet9.set_column(row9, 11, 20)
        sheet9.set_column(row9, 12, 20)
        sheet9.set_column(row9, 13, 20)
        
        row10 = 4
        sheet10.set_column(row10, 0, 50)
        sheet10.set_column(row10, 1, 25)
        sheet10.set_column(row10, 2, 20)
        sheet10.set_column(row10, 3, 20)
        sheet10.set_column(row10, 4, 20)
        sheet10.set_column(row10, 5, 20)
        sheet10.set_column(row10, 6, 20)
        sheet10.set_column(row10, 7, 20)
        sheet10.set_column(row10, 8, 20)
        sheet10.set_column(row10, 9, 20)
        sheet10.set_column(row10, 10, 20)
        sheet10.set_column(row10, 11, 20)
        sheet10.set_column(row10, 12, 20)
        sheet10.set_column(row10, 13, 20)
        
        row11 = 4
        sheet11.set_column(row11, 0, 50)
        sheet11.set_column(row11, 1, 25)
        sheet11.set_column(row11, 2, 20)
        sheet11.set_column(row11, 3, 20)
        sheet11.set_column(row11, 4, 20)
        sheet11.set_column(row11, 5, 20)
        sheet11.set_column(row11, 6, 20)
        sheet11.set_column(row11, 7, 20)
        sheet11.set_column(row11, 8, 20)
        sheet11.set_column(row11, 9, 20)
        sheet11.set_column(row11, 10, 20)
        sheet11.set_column(row11, 11, 20)
        sheet11.set_column(row11, 12, 20)
        sheet11.set_column(row11, 13, 20)
        
        row12 = 4
        sheet12.set_column(row12, 0, 50)
        sheet12.set_column(row12, 1, 25)
        sheet12.set_column(row12, 2, 20)
        sheet12.set_column(row12, 3, 20)
        sheet12.set_column(row12, 4, 20)
        sheet12.set_column(row12, 5, 20)
        sheet12.set_column(row12, 6, 20)
        sheet12.set_column(row12, 7, 20)
        sheet12.set_column(row12, 8, 20)
        sheet12.set_column(row12, 9, 20)
        sheet12.set_column(row12, 10, 20)
        sheet12.set_column(row12, 11, 20)
        sheet12.set_column(row12, 12, 20)
        sheet12.set_column(row12, 13, 20)
        
        
        for id in lines:
            if id.purchase_budget_line:
                for line in id.purchase_budget_line:
                    po_lines = self.env['purchase.order.line'].search([('purchase_budget_line_id','=',line.id)])
                    for po in po_lines:
                        #raise UserError(type(po.date_order.month))
                        
                        ############## For January #############
                        try:
                            dep = []
                            for department in id.department_ids:
                                dep.append(department.name)

                            departments = ''
                            departments = ','.join(dep)
                        except:
                            departments = None
                        try:    
                            if id.name:
                                ref = id.name
                            else:
                                ref = None
                        except:
                            ref = None

                        try:
                            if line.date_from:
                                start_date = line.date_from.strftime("%Y-%m-%d")
                            else:
                                start_date = None
                        except:
                            start_date = None
                        try:
                            if line.date_to:
                                end_date = line.date_to.strftime("%Y-%m-%d")
                            else:
                                end_date = None
                        except:
                            end_date = None

                        try:
                            if start_date and end_date:
                                duration = start_date + '~' + end_date
                            else:
                                duration = None
                        except:
                            duration = None

                        try:
                            if po.date_order:
                                month1 = po.date_order.strftime("%Y")
                                month1 = "January/"+month1
                            else:
                                month1 = None
                        except:
                            month1 = None
                        try:
                            if line.expense_category:
                                capitalisation = line.expense_category
                            else:
                                capitalisation = None
                        except:
                            capitalisation = None
                        try:
                            if line.name:
                                line_budget = line.name
                            else:
                                line_budget = None
                        except:
                            line_budget = None
                        try:
                            if line.planned_quantity:
                                allocated_qty = line.planned_quantity
                            else:
                                allocated_qty = 0.0
                        except:
                            allocated_qty = 0.0

                        try:
                            if line.planned_price_unit:
                                allocated_unit_price = line.planned_price_unit
                            else:
                                allocated_unit_price = 0.0
                        except:
                            allocated_unit_price = 0.0

                        try:
                            if line.planned_amount:
                                allocated_amount = line.planned_amount
                            else:
                                allocated_amount = 0.0
                        except:
                            allocated_amount = 0.0

                        try:
                            if po.product_qty:
                                used_qty1 = po.product_qty
                            else:
                                used_qty1 = 0.0
                        except:
                            used_qty1 = 0.0

                        try:
                            if po.qty_received:
                                used_amount1 = po.qty_received
                            else:
                                used_amount1 = 0.0
                        except:
                            used_amount1 = 0.0

                        try:
                            available_qty = allocated_qty - used_qty
                        except:
                            available_qty = 0.0

                        try:
                            available_amount = allocated_amount - used_amount
                        except:
                            available_amount = 0.0


                        sheet1.write(row1, 0, departments, format2)
                        sheet1.write(row1, 1, ref, format2)
                        sheet1.write(row1, 2, duration, format2)
                        sheet1.write(row1, 3, month1, format2)
                        sheet1.write(row1, 4, capitalisation, format2)
                        #sheet.write(row, 5, category, format2)
                        sheet1.write(row1, 6, line_budget, format2)
                        sheet1.write(row1, 7, allocated_qty, format2)
                        sheet1.write(row1, 8, allocated_unit_price, format2)
                        sheet1.write(row1, 9, allocated_amount, format2)
                        sheet1.write(row1, 10, used_qty1, format2)
                        sheet1.write(row1, 11, used_amount1, format2)
                        sheet1.write(row1, 12, available_qty, format2)
                        sheet1.write(row1, 13, available_amount, format2)

                        row1 = row1 + 1
                        
                        ############## For February ##################
                        
                        try:
                            if po.date_order:
                                month2 = po.date_order.strftime("%Y")
                                month2 = "February/"+month2
                            else:
                                month2 = None
                        except:
                            month2 = None

                        try:
                            if po.product_qty:
                                used_qty2 = po.product_qty
                            else:
                                used_qty2 = 0.0
                        except:
                            used_qty2 = 0.0

                        try:
                            if po.qty_received:
                                used_amount2 = po.qty_received
                            else:
                                used_amount2 = 0.0
                        except:
                            used_amount2 = 0.0

                        


                        sheet2.write(row2, 0, departments, format2)
                        sheet2.write(row2, 1, ref, format2)
                        sheet2.write(row2, 2, duration, format2)
                        sheet2.write(row2, 3, month2, format2)
                        sheet2.write(row2, 4, capitalisation, format2)
                        #sheet.write(row, 5, category, format2)
                        sheet2.write(row2, 6, line_budget, format2)
                        sheet2.write(row2, 7, allocated_qty, format2)
                        sheet2.write(row2, 8, allocated_unit_price, format2)
                        sheet2.write(row2, 9, allocated_amount, format2)
                        sheet2.write(row2, 10, used_qty2, format2)
                        sheet2.write(row2, 11, used_amount2, format2)
                        sheet2.write(row2, 12, available_qty, format2)
                        sheet2.write(row2, 13, available_amount, format2)

                        row2 = row2 + 1
                            
                        
                            ############## For March #############
                        

                        try:
                            if po.date_order:
                                month3 = po.date_order.strftime("%Y")
                                month3 = "March/"+month3
                            else:
                                month3 = None
                        except:
                            month3 = None
                        try:
                            if line.expense_category:
                                capitalisation = line.expense_category
                            else:
                                capitalisation = None
                        except:
                            capitalisation = None
                        try:
                            if line.name:
                                line_budget = line.name
                            else:
                                line_budget = None
                        except:
                            line_budget = None
                        try:
                            if line.planned_quantity:
                                allocated_qty = line.planned_quantity
                            else:
                                allocated_qty = 0.0
                        except:
                            allocated_qty = 0.0

                        try:
                            if line.planned_price_unit:
                                allocated_unit_price = line.planned_price_unit
                            else:
                                allocated_unit_price = 0.0
                        except:
                            allocated_unit_price = 0.0


                        try:
                            if po.product_qty:
                                used_qty3 = po.product_qty
                            else:
                                used_qty3 = 0.0
                        except:
                            used_qty3 = 0.0

                        try:
                            if po.qty_received:
                                used_amount3 = po.qty_received
                            else:
                                used_amount3 = 0.0
                        except:
                            used_amount3 = 0.0

                        


                        sheet3.write(row3, 0, departments, format2)
                        sheet3.write(row3, 1, ref, format2)
                        sheet3.write(row3, 2, duration, format2)
                        sheet3.write(row3, 3, month3, format2)
                        sheet3.write(row3, 4, capitalisation, format2)
                        #sheet.write(row, 5, category, format2)
                        sheet3.write(row3, 6, line_budget, format2)
                        sheet3.write(row3, 7, allocated_qty, format2)
                        sheet3.write(row3, 8, allocated_unit_price, format2)
                        sheet3.write(row3, 9, allocated_amount, format2)
                        sheet3.write(row3, 10, used_qty3, format2)
                        sheet3.write(row3, 11, used_amount3, format2)
                        sheet3.write(row3, 12, available_qty, format2)
                        sheet3.write(row3, 13, available_amount, format2)

                        row3 = row3 + 1
                        
                        
                            ############## For April #############
                        

                        try:
                            if po.date_order:
                                month4 = po.date_order.strftime("%Y")
                                month4 = "April/"+month4
                            else:
                                month4 = None
                        except:
                            month4 = None
                        

                        try:
                            if po.product_qty:
                                used_qty4 = po.product_qty
                            else:
                                used_qty4 = 0.0
                        except:
                            used_qty4 = 0.0

                        try:
                            if po.qty_received:
                                used_amount4 = po.qty_received
                            else:
                                used_amount4 = 0.0
                        except:
                            used_amount4 = 0.0

                        


                        sheet4.write(row4, 0, departments, format2)
                        sheet4.write(row4, 1, ref, format2)
                        sheet4.write(row4, 2, duration, format2)
                        sheet4.write(row4, 3, month4, format2)
                        sheet4.write(row4, 4, capitalisation, format2)
                        #sheet.write(row, 5, category, format2)
                        sheet4.write(row4, 6, line_budget, format2)
                        sheet4.write(row4, 7, allocated_qty, format2)
                        sheet4.write(row4, 8, allocated_unit_price, format2)
                        sheet4.write(row4, 9, allocated_amount, format2)
                        sheet4.write(row4, 10, used_qty4, format2)
                        sheet4.write(row4, 11, used_amount4, format2)
                        sheet4.write(row4, 12, available_qty, format2)
                        sheet4.write(row4, 13, available_amount, format2)

                        row4 = row4 + 1
                        
                        
                            ############## For May #############
                        

                        try:
                            if po.date_order:
                                month5 = po.date_order.strftime("%Y")
                                month5 = "May/"+month5
                            else:
                                month5 = None
                        except:
                            month5 = None
                        

                        try:
                            if po.product_qty:
                                used_qty5 = po.product_qty
                            else:
                                used_qty5 = 0.0
                        except:
                            used_qty5 = 0.0

                        try:
                            if po.qty_received:
                                used_amount5 = po.qty_received
                            else:
                                used_amount5 = 0.0
                        except:
                            used_amount5 = 0.0

                        


                        sheet5.write(row5, 0, departments, format2)
                        sheet5.write(row5, 1, ref, format2)
                        sheet5.write(row5, 2, duration, format2)
                        sheet5.write(row5, 3, month5, format2)
                        sheet5.write(row5, 4, capitalisation, format2)
                        #sheet.write(row, 5, category, format2)
                        sheet5.write(row5, 6, line_budget, format2)
                        sheet5.write(row5, 7, allocated_qty, format2)
                        sheet5.write(row5, 8, allocated_unit_price, format2)
                        sheet5.write(row5, 9, allocated_amount, format2)
                        sheet5.write(row5, 10, used_qty5, format2)
                        sheet5.write(row5, 11, used_amount5, format2)
                        sheet5.write(row5, 12, available_qty, format2)
                        sheet5.write(row5, 13, available_amount, format2)

                        row5 = row5 + 1
                        
                        
                        ############## For June #############
                        

                        try:
                            if po.date_order:
                                month6 = po.date_order.strftime("%Y")
                                month6 = "June/"+month6
                            else:
                                month6 = None
                        except:
                            month6 = None
                        

                        try:
                            if po.product_qty:
                                used_qty6 = po.product_qty
                            else:
                                used_qty6 = 0.0
                        except:
                            used_qty6 = 0.0

                        try:
                            if po.qty_received:
                                used_amount6 = po.qty_received
                            else:
                                used_amount6 = 0.0
                        except:
                            used_amount6 = 0.0


                        sheet6.write(row6, 0, departments, format2)
                        sheet6.write(row6, 1, ref, format2)
                        sheet6.write(row6, 2, duration, format2)
                        sheet6.write(row6, 3, month6, format2)
                        sheet6.write(row6, 4, capitalisation, format2)
                        #sheet.write(row, 5, category, format2)
                        sheet6.write(row6, 6, line_budget, format2)
                        sheet6.write(row6, 7, allocated_qty, format2)
                        sheet6.write(row6, 8, allocated_unit_price, format2)
                        sheet6.write(row6, 9, allocated_amount, format2)
                        sheet6.write(row6, 10, used_qty6, format2)
                        sheet6.write(row6, 11, used_amount6, format2)
                        sheet6.write(row6, 12, available_qty, format2)
                        sheet6.write(row6, 13, available_amount, format2)

                        row6 = row6 + 1
                        
                        
                        ############## For July #############
                        

                        try:
                            if po.date_order:
                                month7 = po.date_order.strftime("%Y")
                                month7 = "July/"+month7
                            else:
                                month7 = None
                        except:
                            month7 = None
                        

                        try:
                            if po.product_qty:
                                used_qty7 = po.product_qty
                            else:
                                used_qty7 = 0.0
                        except:
                            used_qty7 = 0.0

                        try:
                            if po.qty_received:
                                used_amount7 = po.qty_received
                            else:
                                used_amount7 = 0.0
                        except:
                            used_amount7 = 0.0

                        


                        sheet7.write(row7, 0, departments, format2)
                        sheet7.write(row7, 1, ref, format2)
                        sheet7.write(row7, 2, duration, format2)
                        sheet7.write(row7, 3, month7, format2)
                        sheet7.write(row7, 4, capitalisation, format2)
                        #sheet.write(row, 5, category, format2)
                        sheet7.write(row7, 6, line_budget, format2)
                        sheet7.write(row7, 7, allocated_qty, format2)
                        sheet7.write(row7, 8, allocated_unit_price, format2)
                        sheet7.write(row7, 9, allocated_amount, format2)
                        sheet7.write(row7, 10, used_qty7, format2)
                        sheet7.write(row7, 11, used_amount7, format2)
                        sheet7.write(row7, 12, available_qty, format2)
                        sheet7.write(row7, 13, available_amount, format2)

                        row7 = row7 + 1
                        
                        
                            ############## For August #############
                        

                        try:
                            if po.date_order:
                                month8 = po.date_order.strftime("%Y")
                                month8 = "January/"+month8
                            else:
                                month8 = None
                        except:
                            month8 = None
                        

                        try:
                            if po.product_qty:
                                used_qty8 = po.product_qty
                            else:
                                used_qty8 = 0.0
                        except:
                            used_qty = 0.0

                        try:
                            if po.qty_received:
                                used_amount8 = po.qty_received
                            else:
                                used_amount8 = 0.0
                        except:
                            used_amount8 = 0.0

                        


                        sheet8.write(row8, 0, departments, format2)
                        sheet8.write(row8, 1, ref, format2)
                        sheet8.write(row8, 2, duration, format2)
                        sheet8.write(row8, 3, month8, format2)
                        sheet8.write(row8, 4, capitalisation, format2)
                        #sheet.write(row, 5, category, format2)
                        sheet8.write(row8, 6, line_budget, format2)
                        sheet8.write(row8, 7, allocated_qty, format2)
                        sheet8.write(row8, 8, allocated_unit_price, format2)
                        sheet8.write(row8, 9, allocated_amount, format2)
                        sheet8.write(row8, 10, used_qty8, format2)
                        sheet8.write(row8, 11, used_amount8, format2)
                        sheet8.write(row8, 12, available_qty, format2)
                        sheet8.write(row8, 13, available_amount, format2)

                        row8 = row8 + 1
                        
                        
                        ############## For September #############
                        

                        try:
                            if po.date_order:
                                month9 = po.date_order.strftime("%Y")
                                month9 = "September/"+month9
                            else:
                                month9 = None
                        except:
                            month9 = None
                        

                        try:
                            if po.product_qty:
                                used_qty9 = po.product_qty
                            else:
                                used_qty9 = 0.0
                        except:
                            used_qty9 = 0.0

                        try:
                            if po.qty_received:
                                used_amount9 = po.qty_received
                            else:
                                used_amount9 = 0.0
                        except:
                            used_amount9 = 0.0

                        


                        sheet9.write(row9, 0, departments, format2)
                        sheet9.write(row9, 1, ref, format2)
                        sheet9.write(row9, 2, duration, format2)
                        sheet9.write(row9, 3, month9, format2)
                        sheet9.write(row9, 4, capitalisation, format2)
                        #sheet.write(row, 5, category, format2)
                        sheet9.write(row9, 6, line_budget, format2)
                        sheet9.write(row9, 7, allocated_qty, format2)
                        sheet9.write(row9, 8, allocated_unit_price, format2)
                        sheet9.write(row9, 9, allocated_amount, format2)
                        sheet9.write(row9, 10, used_qty9, format2)
                        sheet9.write(row9, 11, used_amount9, format2)
                        sheet9.write(row9, 12, available_qty, format2)
                        sheet9.write(row9, 13, available_amount, format2)

                        row9 = row9 + 1
                        
                        
                        ############## For October #############
                        

                        try:
                            if po.date_order:
                                month10 = po.date_order.strftime("%Y")
                                month10 = "October/"+month10
                            else:
                                month10 = None
                        except:
                            month10 = None
                        

                        try:
                            if po.product_qty:
                                used_qty10 = po.product_qty
                            else:
                                used_qty10 = 0.0
                        except:
                            used_qty10 = 0.0

                        try:
                            if po.qty_received:
                                used_amount10 = po.qty_received
                            else:
                                used_amount10 = 0.0
                        except:
                            used_amount10 = 0.0

                        


                        sheet10.write(row10, 0, departments, format2)
                        sheet10.write(row10, 1, ref, format2)
                        sheet10.write(row10, 2, duration, format2)
                        sheet10.write(row10, 3, month10, format2)
                        sheet10.write(row10, 4, capitalisation, format2)
                        #sheet.write(row, 5, category, format2)
                        sheet10.write(row10, 6, line_budget, format2)
                        sheet10.write(row10, 7, allocated_qty, format2)
                        sheet10.write(row10, 8, allocated_unit_price, format2)
                        sheet10.write(row10, 9, allocated_amount, format2)
                        sheet10.write(row10, 10, used_qty10, format2)
                        sheet10.write(row10, 11, used_amount10, format2)
                        sheet10.write(row10, 12, available_qty, format2)
                        sheet10.write(row10, 13, available_amount, format2)

                        row10 = row10 + 1
                        
                        
                        ############## For November #############
                        

                        try:
                            if po.date_order:
                                month11 = po.date_order.strftime("%Y")
                                month11 = "November/"+month11
                            else:
                                month11 = None
                        except:
                            month11 = None
                        

                        try:
                            if po.product_qty:
                                used_qty11 = po.product_qty
                            else:
                                used_qty11 = 0.0
                        except:
                            used_qty11 = 0.0

                        try:
                            if po.qty_received:
                                used_amount11 = po.qty_received
                            else:
                                used_amount11 = 0.0
                        except:
                            used_amount11 = 0.0

                        


                        sheet11.write(row11, 0, departments, format2)
                        sheet11.write(row11, 1, ref, format2)
                        sheet11.write(row11, 2, duration, format2)
                        sheet11.write(row11, 3, month11, format2)
                        sheet11.write(row11, 4, capitalisation, format2)
                        #sheet.write(row, 5, category, format2)
                        sheet11.write(row11, 6, line_budget, format2)
                        sheet11.write(row11, 7, allocated_qty, format2)
                        sheet11.write(row11, 8, allocated_unit_price, format2)
                        sheet11.write(row11, 9, allocated_amount, format2)
                        sheet11.write(row11, 10, used_qty11, format2)
                        sheet11.write(row11, 11, used_amount11, format2)
                        sheet11.write(row11, 12, available_qty, format2)
                        sheet11.write(row11, 13, available_amount, format2)

                        row11 = row11 + 1
                        
                        
                        ############## For December #############


                        try:
                            if po.date_order:
                                month12 = po.date_order.strftime("%Y")
                                month12 = "December/"+month12
                            else:
                                month12 = None
                        except:
                            month12 = None


                        try:
                            if po.product_qty:
                                used_qty12 = po.product_qty
                            else:
                                used_qty12 = 0.0
                        except:
                            used_qty12 = 0.0

                        try:
                            if po.qty_received:
                                used_amount12 = po.qty_received
                            else:
                                used_amount12 = 0.0
                        except:
                            used_amount12 = 0.0




                        sheet12.write(row12, 0, departments, format2)
                        sheet12.write(row12, 1, ref, format2)
                        sheet12.write(row12, 2, duration, format2)
                        sheet12.write(row12, 3, month12, format2)
                        sheet12.write(row12, 4, capitalisation, format2)
                        #sheet.write(row, 5, category, format2)
                        sheet12.write(row12, 6, line_budget, format2)
                        sheet12.write(row12, 7, allocated_qty, format2)
                        sheet12.write(row12, 8, allocated_unit_price, format2)
                        sheet12.write(row12, 9, allocated_amount, format2)
                        sheet12.write(row12, 10, used_qty12, format2)
                        sheet12.write(row12, 11, used_amount12, format2)
                        sheet12.write(row12, 12, available_qty, format2)
                        sheet12.write(row12, 13, available_amount, format2)

                        row12 = row12 + 1




                        ########## For Total #################
                        try:
                            dep = []
                            for department in id.department_ids:
                                dep.append(department.name)

                            departments = ''
                            departments = ','.join(dep)
                        except:
                            departments = None
                        try:    
                            if id.name:
                                ref = id.name
                            else:
                                ref = None
                        except:
                            ref = None

                        try:
                            if line.date_from:
                                start_date = line.date_from.strftime("%Y-%m-%d")
                            else:
                                start_date = None
                        except:
                            start_date = None
                        try:
                            if line.date_to:
                                end_date = line.date_to.strftime("%Y-%m-%d")
                            else:
                                end_date = None
                        except:
                            end_date = None

                        try:
                            if start_date and end_date:
                                duration = start_date + '~' + end_date
                            else:
                                duration = None
                        except:
                            duration = None

                        try:
                            if line.date_from:
                                month = line.date_from.strftime("%B/%Y")
                            else:
                                month = None
                        except:
                            month = None
                        try:
                            if line.expense_category:
                                capitalisation = line.expense_category
                            else:
                                capitalisation = None
                        except:
                            capitalisation = None
                        try:
                            if line.name:
                                line_budget = line.name
                            else:
                                line_budget = None
                        except:
                            line_budget = None
                        try:
                            if line.planned_quantity:
                                allocated_qty = line.planned_quantity
                            else:
                                allocated_qty = 0.0
                        except:
                            allocated_qty = 0.0

                        try:
                            if line.planned_price_unit:
                                allocated_unit_price = line.planned_price_unit
                            else:
                                allocated_unit_price = 0.0
                        except:
                            allocated_unit_price = 0.0

                        try:
                            if line.planned_amount:
                                allocated_amount = line.planned_amount
                            else:
                                allocated_amount = 0.0
                        except:
                            allocated_amount = 0.0

                        try:
                            if line.practical_quantity:
                                used_qty = line.practical_quantity
                            else:
                                used_qty = 0.0
                        except:
                            used_qty = 0.0

                        try:
                            if line.practical_amount:
                                used_amount = line.practical_amount
                            else:
                                used_amount = 0.0
                        except:
                            used_amount = 0.0

                        try:
                            available_qty = allocated_qty - used_qty
                        except:
                            available_qty = 0.0

                        try:
                            available_amount = allocated_amount - used_amount
                        except:
                            available_amount = 0.0


                        sheet.write(row, 0, departments, format2)
                        sheet.write(row, 1, ref, format2)
                        sheet.write(row, 2, duration, format2)
                        sheet.write(row, 3, month, format2)
                        sheet.write(row, 4, capitalisation, format2)
                        #sheet.write(row, 5, category, format2)
                        sheet.write(row, 6, line_budget, format2)
                        sheet.write(row, 7, allocated_qty, format2)
                        sheet.write(row, 8, allocated_unit_price, format2)
                        sheet.write(row, 9, allocated_amount, format2)
                        sheet.write(row, 10, used_qty, format2)
                        sheet.write(row, 11, used_amount, format2)
                        sheet.write(row, 12, available_qty, format2)
                        sheet.write(row, 13, available_amount, format2)

                        row = row + 1

        
        