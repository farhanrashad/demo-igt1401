from odoo import models
from odoo.exceptions import UserError


class GenerateXLSXReport(models.Model):
    _name = 'report.de_report_purchase_budget.report_purchase_budget'
    _description = 'Purchase Budget Report XLSX'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines,model="ir.actions.report",output_format="xlsx",report_name="de_report_purchase_budget.report_purchase_budget"):
        
        format1 = workbook.add_format({'font_size': '12', 'align': 'vcenter', 'bold': True})
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
        
        sheet1.set_column(row, 0, 50)
        sheet1.set_column(row, 1, 25)
        sheet1.set_column(row, 2, 20)
        sheet1.set_column(row, 3, 20)
        sheet1.set_column(row, 4, 20)
        sheet1.set_column(row, 5, 20)
        sheet1.set_column(row, 6, 20)
        sheet1.set_column(row, 7, 20)
        sheet1.set_column(row, 8, 20)
        sheet1.set_column(row, 9, 20)
        sheet1.set_column(row, 10, 20)
        sheet1.set_column(row, 11, 20)
        sheet1.set_column(row, 12, 20)
        sheet1.set_column(row, 13, 20)
        
        sheet2.set_column(row, 0, 50)
        sheet2.set_column(row, 1, 25)
        sheet2.set_column(row, 2, 20)
        sheet2.set_column(row, 3, 20)
        sheet2.set_column(row, 4, 20)
        sheet2.set_column(row, 5, 20)
        sheet2.set_column(row, 6, 20)
        sheet2.set_column(row, 7, 20)
        sheet2.set_column(row, 8, 20)
        sheet2.set_column(row, 9, 20)
        sheet2.set_column(row, 10, 20)
        sheet2.set_column(row, 11, 20)
        sheet2.set_column(row, 12, 20)
        sheet2.set_column(row, 13, 20)
        
        sheet3.set_column(row, 0, 50)
        sheet3.set_column(row, 1, 25)
        sheet3.set_column(row, 2, 20)
        sheet3.set_column(row, 3, 20)
        sheet3.set_column(row, 4, 20)
        sheet3.set_column(row, 5, 20)
        sheet3.set_column(row, 6, 20)
        sheet3.set_column(row, 7, 20)
        sheet3.set_column(row, 8, 20)
        sheet3.set_column(row, 9, 20)
        sheet3.set_column(row, 10, 20)
        sheet3.set_column(row, 11, 20)
        sheet3.set_column(row, 12, 20)
        sheet3.set_column(row, 13, 20)
        
        sheet4.set_column(row, 0, 50)
        sheet4.set_column(row, 1, 25)
        sheet4.set_column(row, 2, 20)
        sheet4.set_column(row, 3, 20)
        sheet4.set_column(row, 4, 20)
        sheet4.set_column(row, 5, 20)
        sheet4.set_column(row, 6, 20)
        sheet4.set_column(row, 7, 20)
        sheet4.set_column(row, 8, 20)
        sheet4.set_column(row, 9, 20)
        sheet4.set_column(row, 10, 20)
        sheet4.set_column(row, 11, 20)
        sheet4.set_column(row, 12, 20)
        sheet4.set_column(row, 13, 20)
        
        sheet5.set_column(row, 0, 50)
        sheet5.set_column(row, 1, 25)
        sheet5.set_column(row, 2, 20)
        sheet5.set_column(row, 3, 20)
        sheet5.set_column(row, 4, 20)
        sheet5.set_column(row, 5, 20)
        sheet5.set_column(row, 6, 20)
        sheet5.set_column(row, 7, 20)
        sheet5.set_column(row, 8, 20)
        sheet5.set_column(row, 9, 20)
        sheet5.set_column(row, 10, 20)
        sheet5.set_column(row, 11, 20)
        sheet5.set_column(row, 12, 20)
        sheet5.set_column(row, 13, 20)
        
        sheet6.set_column(row, 0, 50)
        sheet6.set_column(row, 1, 25)
        sheet6.set_column(row, 2, 20)
        sheet6.set_column(row, 3, 20)
        sheet6.set_column(row, 4, 20)
        sheet6.set_column(row, 5, 20)
        sheet6.set_column(row, 6, 20)
        sheet6.set_column(row, 7, 20)
        sheet6.set_column(row, 8, 20)
        sheet6.set_column(row, 9, 20)
        sheet6.set_column(row, 10, 20)
        sheet6.set_column(row, 11, 20)
        sheet6.set_column(row, 12, 20)
        sheet6.set_column(row, 13, 20)
        
        sheet7.set_column(row, 0, 50)
        sheet7.set_column(row, 1, 25)
        sheet7.set_column(row, 2, 20)
        sheet7.set_column(row, 3, 20)
        sheet7.set_column(row, 4, 20)
        sheet7.set_column(row, 5, 20)
        sheet7.set_column(row, 6, 20)
        sheet7.set_column(row, 7, 20)
        sheet7.set_column(row, 8, 20)
        sheet7.set_column(row, 9, 20)
        sheet7.set_column(row, 10, 20)
        sheet7.set_column(row, 11, 20)
        sheet7.set_column(row, 12, 20)
        sheet7.set_column(row, 13, 20)
        
        sheet8.set_column(row, 0, 50)
        sheet8.set_column(row, 1, 25)
        sheet8.set_column(row, 2, 20)
        sheet8.set_column(row, 3, 20)
        sheet8.set_column(row, 4, 20)
        sheet8.set_column(row, 5, 20)
        sheet8.set_column(row, 6, 20)
        sheet8.set_column(row, 7, 20)
        sheet8.set_column(row, 8, 20)
        sheet8.set_column(row, 9, 20)
        sheet8.set_column(row, 10, 20)
        sheet8.set_column(row, 11, 20)
        sheet8.set_column(row, 12, 20)
        sheet8.set_column(row, 13, 20)
        
        sheet9.set_column(row, 0, 50)
        sheet9.set_column(row, 1, 25)
        sheet9.set_column(row, 2, 20)
        sheet9.set_column(row, 3, 20)
        sheet9.set_column(row, 4, 20)
        sheet9.set_column(row, 5, 20)
        sheet9.set_column(row, 6, 20)
        sheet9.set_column(row, 7, 20)
        sheet9.set_column(row, 8, 20)
        sheet9.set_column(row, 9, 20)
        sheet9.set_column(row, 10, 20)
        sheet9.set_column(row, 11, 20)
        sheet9.set_column(row, 12, 20)
        sheet9.set_column(row, 13, 20)
        
        sheet10.set_column(row, 0, 50)
        sheet10.set_column(row, 1, 25)
        sheet10.set_column(row, 2, 20)
        sheet10.set_column(row, 3, 20)
        sheet10.set_column(row, 4, 20)
        sheet10.set_column(row, 5, 20)
        sheet10.set_column(row, 6, 20)
        sheet10.set_column(row, 7, 20)
        sheet10.set_column(row, 8, 20)
        sheet10.set_column(row, 9, 20)
        sheet10.set_column(row, 10, 20)
        sheet10.set_column(row, 11, 20)
        sheet10.set_column(row, 12, 20)
        sheet10.set_column(row, 13, 20)
        
        sheet11.set_column(row, 0, 50)
        sheet11.set_column(row, 1, 25)
        sheet11.set_column(row, 2, 20)
        sheet11.set_column(row, 3, 20)
        sheet11.set_column(row, 4, 20)
        sheet11.set_column(row, 5, 20)
        sheet11.set_column(row, 6, 20)
        sheet11.set_column(row, 7, 20)
        sheet11.set_column(row, 8, 20)
        sheet11.set_column(row, 9, 20)
        sheet11.set_column(row, 10, 20)
        sheet11.set_column(row, 11, 20)
        sheet11.set_column(row, 12, 20)
        sheet11.set_column(row, 13, 20)
        
        sheet12.set_column(row, 0, 50)
        sheet12.set_column(row, 1, 25)
        sheet12.set_column(row, 2, 20)
        sheet12.set_column(row, 3, 20)
        sheet12.set_column(row, 4, 20)
        sheet12.set_column(row, 5, 20)
        sheet12.set_column(row, 6, 20)
        sheet12.set_column(row, 7, 20)
        sheet12.set_column(row, 8, 20)
        sheet12.set_column(row, 9, 20)
        sheet12.set_column(row, 10, 20)
        sheet12.set_column(row, 11, 20)
        sheet12.set_column(row, 12, 20)
        sheet12.set_column(row, 13, 20)
        
        
        for id in lines:
            if id.purchase_budget_line:
                for line in id.purchase_budget_line:
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

        
        