from odoo import models
from odoo.exceptions import UserError
from datetime import date, datetime, timedelta




class GenerateXLSXReport(models.Model):
    _name = 'report.de_report_purchase_budget.xlsx_1'
    _description = 'Purchase Report Budget'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, obj):
        report_obj = self.env['report.de_report_purchase_budget.xlsx_1']
        result = report_obj._get_report_values(obj, data)
        #         raise UserError(data['id'])
       
        format1 = workbook.add_format({'font_size': '12', 'align': 'vcenter', 'bold': True})
        format3 = workbook.add_format({'font_size': '12', 'align': 'vcenter', 'bold': True, 'font_color': '#0000FF'})
        sheet = workbook.add_worksheet('MSA Report')
        sheet.write(1, 0, 'Client', format1)
        sheet.write(2, 0, 'Simulation Date', format1)
        sheet.write(3, 0, 'Exchange Rate (from USD to MMK)', format1)
        sheet.write(4, 0, 'Number Days In Month', format1)
        sheet.write(5, 0, 'Totals', format3)
        sheet.write(6, 0, 'Total IP Fee CAPEX (USD)', format1)
        sheet.write(6, 2, 'Total IP Fee OPEX (MMK)', format1)
        sheet.write(7, 0, 'Price Details', format3)
        sheet.write(9, 0, 'IGT Site Code', format1)
        sheet.write(9, 1, 'Customer Site Code', format1)
        sheet.write(9, 2, 'Marketing Cluster', format1)
        sheet.write(9, 3, 'Marketing Mini Cluster', format1)
        sheet.write(9, 4, 'Network Type', format1)
        sheet.write(9, 5, 'Year', format1)
        sheet.write(9, 6, 'Month Year', format1)
        sheet.write(9, 7, 'RFU date', format1)
        sheet.write(9, 8, 'Invoicing Days', format1)
        sheet.write(9, 9, 'Lease Agreement', format1)
        sheet.write(9, 10, 'Lease Agreement Extra', format1)
        sheet.write(9, 11, 'Region Factor', format1)
        sheet.write(9, 12, 'Collocation Discount for Tower CAPEX', format1)
        sheet.write(9, 13, 'Collocation Discount for Tower OPEX', format1)
        sheet.write(9, 14, 'Tower Type', format1)
        sheet.write(9, 15, 'Tower Height', format1)
        sheet.write(9, 16, 'Wind Factor', format1)
        sheet.write(9, 17, 'Power Model', format1)
        sheet.write(9, 18, 'Tower w/o Power CAPEX', format1)
        sheet.write(9, 19, 'Tower w/o Power OPEX', format1)
        sheet.write(9, 20, 'Invoiced Rent Adjustment', format1)
        sheet.write(9, 21, 'Power CAPEX', format1)
        sheet.write(9, 22, 'CPI CAPEX', format1)
        sheet.write(9, 23, 'CPI OPEX', format1)
        sheet.write(9, 24, 'IP Fee CAPEX', format1)
        sheet.write(9, 25, 'IP Fee Capex billed', format1)
        sheet.write(9, 26, 'Diff. Capex', format1)
        sheet.write(9, 27, 'IP Fee OPEX', format1)
        sheet.write(9, 28, 'IP Fee Opex billed', format1)
        sheet.write(9, 29, 'Diff. Opex', format1)

        format2 = workbook.add_format({'font_size': '12', 'align': 'vcenter'})
        row = 1
        sheet.set_column(row, 0, 50)
        sheet.set_column(row, 1, 25)
        sheet.set_column(row, 2, 20)
        sheet.set_column(row, 3, 35)
        sheet.set_column(row, 4, 20)
        sheet.set_column(row, 5, 20)
        sheet.set_column(row, 6, 35)
        sheet.set_column(row, 7, 20)
        sheet.set_column(row, 8, 20)
        sheet.set_column(row, 9, 35)
        sheet.set_column(row, 10, 20)
        sheet.set_column(row, 11, 35)
        sheet.set_column(row, 12, 20)
        sheet.set_column(row, 13, 20)
        sheet.set_column(row, 14, 20)
        sheet.set_column(row, 15, 20)
        sheet.set_column(row, 16, 20)
        sheet.set_column(row, 17, 20)
        sheet.set_column(row, 18, 35)
        sheet.set_column(row, 19, 20)
        sheet.set_column(row, 20, 45)
        sheet.set_column(row, 21, 45)
        sheet.set_column(row, 22, 20)
        sheet.set_column(row, 23, 20)
        sheet.set_column(row, 24, 20)
        sheet.set_column(row, 25, 20)
        sheet.set_column(row, 26, 35)
        sheet.set_column(row, 27, 35)
        sheet.set_column(row, 28, 35)
        sheet.set_column(row, 29, 35)
        sheet.set_column(row, 30, 20)
        sheet.set_column(row, 31, 20)
        sheet.set_column(row, 32, 20)
        sheet.set_column(row, 33, 20)
        sheet.set_column(row, 34, 35)
        sheet.set_column(row, 35, 20)
        sheet.set_column(row, 36, 35)
        sheet.set_column(row, 37, 20)
        

"""
        msa_obj = self.env['master.service.agreement'].browse(data['id'])
        site_billing_id = self.env['site.billing.info']
        sheet.write(1, 1, str(msa_obj.partner_id.name), format2)
        sheet.write(2, 1, str(msa_obj.simulation_date_from), format2)
        sheet.write(3, 1, str(msa_obj.exchange_rate), format2)
        sheet.write(4, 1, str(msa_obj.number_days_in_month), format2)
        sheet.write(6, 1, str(msa_obj.total_gross_capex), format2)
        sheet.write(6, 3, str(msa_obj.total_gross_opex), format2)
        row = 10
        network_type_id = ''
        rfu_date = ''
        
        for line in msa_obj.msa_simulation_ids:
            site_billing_id = self.env['site.billing.info'].search([('msa_id','=',line.msa_id.id),('site_id','=',line.site_id.id)],limit=1)
            if site_billing_id.network_type_id:
                network_type_id = site_billing_id.network_type_id.name
            if line.rfu_date:
                rfu_date = str(line.rfu_date.day) + '/' + str(line.rfu_date.month) + '/' + str(line.rfu_date.year)
                
            sheet.write(row, 0, line.site_id.name, format2)
            sheet.write(row, 1, site_billing_id.name, format2)
            sheet.write(row, 2, '', format2)
            sheet.write(row, 3, '', format2)
            sheet.write(row, 4, network_type_id, format2)
            sheet.write(row, 5, line.year, format2)
            sheet.write(row, 6, line.month_year, format2)
            sheet.write(row, 7, rfu_date, format2)
            sheet.write(row, 8, line.invoicing_days, format2)
            sheet.write(row, 9, line.head_lease, format2)
            sheet.write(row, 10, line.head_lease_extra, format2)
            sheet.write(row, 11, line.region_factor, format2)
            sheet.write(row, 12, line.collocation_capex, format2)
            sheet.write(row, 13, line.collocation_opex, format2)
            sheet.write(row, 14, line.inv_tower_type.name, format2)
            sheet.write(row, 15, line.inv_tower_type.tower_height, format2)
            sheet.write(row, 16, line.wind_factor, format2)
            sheet.write(row, 17, line.inv_power_model.name, format2)
            sheet.write(row, 18, line.ip_fee_capex, format2)
            sheet.write(row, 19, line.ip_fee_opex, format2)
            sheet.write(row, 20, line.invoiced_rent_adjustment, format2)
            sheet.write(row, 21, line.power_fee_capex, format2)
            sheet.write(row, 22, line.capex_escalation, format2)
            sheet.write(row, 23, line.opex_cpi, format2)
            sheet.write(row, 24, line.gross_ip_fee_capex, format2)
            sheet.write(row, 25, line.ip_fee_capex_billed, format2)
            sheet.write(row, 26, line.diff_capex, format2)
            sheet.write(row, 27, line.gross_ip_fee_opex, format2)
            sheet.write(row, 28, line.ip_fee_opex_billed, format2)
            sheet.write(row, 29, line.diff_opex, format2)
            
            row = row + 1
"""