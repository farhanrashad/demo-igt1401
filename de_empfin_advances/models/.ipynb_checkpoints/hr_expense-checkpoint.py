# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import re

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import email_split, float_is_zero

class HrExpenseSheetType(models.Model):
    _name = 'hr.expense.sheet.type'
    _description = 'Expense Sheet Type'
    
    name = fields.Char(string='Expense Type', required=True, translate=True)
    
    group_id = fields.Many2one('res.groups', string='Security Group')
    
class HrExpenseSheet(models.Model):
    _inherit = 'hr.expense.sheet'
    
    sheet_ref = fields.Char(string='Reference', readonly=True, default=lambda self: 'HEX/')
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit', 'Submitted'),
        ('approve', 'Line Manager Approval'),
        ('exp_approve', 'Expense Category Approval'),
        ('fin_approve', 'Finance Approval'),
        ('post', 'Waiting Account Entries'),
        ('payment', 'Waiting Payment'),
        ('done', 'Paid'),
        ('cancel', 'Refused')
    ], string='Status', index=True, readonly=True, tracking=True, copy=False, default='draft', required=True, help='Expense Report State')
    
    
    hr_salary_advance_id  = fields.Many2one('hr.salary.advance', string='Advances Request', domain='[("employee_id","=", employee_id), ("state","in", ("paid","close"))]')
    
    hr_expense_sheet_type_id  = fields.Many2one('hr.expense.sheet.type', string='Expense Type')
    
    total_currency_amount = fields.Float(string='Total curr.Amount', compute='_compute_curr_amount', store=True, tracking=True)
    
    @api.depends('expense_line_ids.total_amount')
    def _compute_curr_amount(self):
        for sheet in self:
            sheet.total_currency_amount = sum(sheet.expense_line_ids.mapped('total_amount'))
    
    @api.model
    def create(self, vals):
        vals['sheet_ref'] = self.env['ir.sequence'].get('hr.expense.sheet') or ' '
        sheet = super(HrExpenseSheet, self.with_context(mail_create_nosubscribe=True, mail_auto_subscribe_no_notify=True)).create(vals)
        sheet.activity_update()
        return sheet
    
    # --------------------------------------------
    # Expense Sheet Submit Button
    # --------------------------------------------
    def action_submit_sheet(self):
        for sheet in self.sudo():
            group_id = sheet.hr_expense_sheet_type_id.group_id
            if group_id:
                if not (group_id & self.env.user.groups_id):
                    raise UserError(_("You are not authorize to submit request in category '%s'.", sheet.hr_expense_sheet_type_id.name))
            
            if not sheet.expense_line_ids:
                raise UserError(_("You cannot submit expense '%s' because there is no line.", self.name))
                    
        self.write({'state': 'submit'})
        self.activity_update()
    
    # --------------------------------------------
    # Expense Sheet Approval Buttons
    # --------------------------------------------
    def approve_expense_finance(self):
        #Finanace Approval
        for line in self.expense_line_ids:
            if line.expense_approved:
                if line.total_amount != line.amount_approved and line.fin_remarks == False:
                    raise UserError(_("Approved amount is different than advance amount, Please specify remarks"))
                    break
                    
        notification = {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('There are no expense reports to approve.'),
                'type': 'warning',
                'sticky': False,  #True/False will display for few seconds if false
            },
        }
        
        #Line Finance Approval
        filtered_sheet_exp = self.filtered(lambda s: s.state in ['exp_approve'])
        if not filtered_sheet_exp:
            return notification
        for sheet in filtered_sheet_exp:
            sheet.write({'state': 'fin_approve', 'user_id': sheet.user_id.id or self.env.user.id})
        
        notification['params'].update({
            'title': _('The expense reports were successfully approved.'),
            'type': 'success',
            'next': {'type': 'ir.actions.act_window_close'},
        })
        
    def approve_expense_category(self):
        for line in self.expense_line_ids:
            if line.expense_approved:
                if line.total_amount != line.amount_approved and line.remarks == False:
                    raise UserError(_("Approved amount is different than advance amount, Please specify remarks"))
                    break
            expense_type_id = self.env['hr.expense.type'].search([('id','=',line.expense_type_id.id)],limit=1)
            group_id = expense_type_id.group_id
            if group_id:
                if (group_id & self.env.user.groups_id):
                    if line.expense_approved == True or line.remarks != False:
                        line.write({
                            'state': 'approved', 
                        })
        
        #Line Category Expense Approval
        notification = {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('There are no expense reports to approve.'),
                'type': 'warning',
                'sticky': False,  #True/False will display for few seconds if false
            },
        }
        
        if all(expense.state == 'approved' for expense in self.expense_line_ids.filtered(lambda p: p.sheet_id.state == 'approve')):
            filtered_sheet_apr = self.filtered(lambda s: s.state in ['approve'])
            if not filtered_sheet_apr:
                return notification
            for sheet in filtered_sheet_apr:
                sheet.write({'state': 'exp_approve', 'user_id': sheet.user_id.id or self.env.user.id})
        
            notification['params'].update({
                'title': _('The expense reports were successfully approved.'),
                'type': 'success',
                'next': {'type': 'ir.actions.act_window_close'},
            })
                            
    def approve_expense_sheets(self):
        expense_type_id = self.env['hr.expense.type']
        if not self.user_has_groups('hr_expense.group_hr_expense_team_approver'):
            raise UserError(_("Only Managers and HR Officers can approve expenses"))
        elif not self.user_has_groups('hr_expense.group_hr_expense_manager'):
            current_managers = self.employee_id.expense_manager_id | self.employee_id.parent_id.user_id | self.employee_id.department_id.manager_id.user_id

            if self.employee_id.user_id == self.env.user:
                raise UserError(_("You cannot approve your own expenses"))

            if not self.env.user in current_managers and not self.user_has_groups('hr_expense.group_hr_expense_user') and self.employee_id.expense_manager_id != self.env.user:
                raise UserError(_("You can only approve your department expenses"))
                
        for line in self.expense_line_ids:
            if line.expense_approved:
                if line.total_amount != line.amount_approved and line.remarks == False:
                    raise UserError(_("Approved amount is different than advance amount, Please specify remarks"))
                    break
        
        notification = {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('There are no expense reports to approve.'),
                'type': 'warning',
                'sticky': False,  #True/False will display for few seconds if false
            },
        }
        #Line Manager Approval
        if self.state in ('submit','draft'):
            filtered_sheet = self.filtered(lambda s: s.state in ['submit', 'draft'])
            if not filtered_sheet:
                return notification
            for sheet in filtered_sheet:
                sheet.write({'state': 'approve', 'user_id': sheet.user_id.id or self.env.user.id})
            
        notification['params'].update({
            'title': _('The expense reports were successfully approved.'),
            'type': 'success',
            'next': {'type': 'ir.actions.act_window_close'},
        })
        
    # --------------------------------------------
    # Actions
    # --------------------------------------------

    def action_sheet_move_create(self):
        samples = self.mapped('expense_line_ids.sample')
        if samples.count(True):
            if samples.count(False):
                raise UserError(_("You can't mix sample expenses and regular ones"))
            self.write({'state': 'post'})
            return

        if any(sheet.state != 'fin_approve' for sheet in self):
            raise UserError(_("You can only generate accounting entry for approved expense(s)."))

        if any(not sheet.journal_id for sheet in self):
            raise UserError(_("Expenses must have an expense journal specified to generate accounting entries."))

        expense_line_ids = self.mapped('expense_line_ids')\
            .filtered(lambda r: not float_is_zero(r.total_amount, precision_rounding=(r.currency_id or self.env.company.currency_id).rounding))
        
        res = expense_line_ids.action_move_create()
        for sheet in self.filtered(lambda s: not s.accounting_date):
            sheet.accounting_date = sheet.account_move_id.date
        to_post = self.filtered(lambda sheet: sheet.payment_mode == 'own_account' and sheet.expense_line_ids)
        to_post.write({'state': 'post'})
        (self - to_post).write({'state': 'done'})
        self.activity_update()
        # change status of advances
        #expense.hr_salary_advance_id.hr_expense_sheet_id = self.id
        for expense in expense_line_ids:
            #expense.hr_salary_advance_id.state = 'close'
            expense.advance_line_id.state = 'close'
            #expense.hr_salary_advance_id.hr_expense_id = expense.id
            #expense.hr_salary_advance_id.hr_expense_id = expense.id
        return res
    
class HrExpenseType(models.Model):
    _name = 'hr.expense.type'
    _description = 'Expense Type'
    
    name = fields.Char(string='Expense Category', required=True, translate=True)
    group_id = fields.Many2one('res.groups', string='Security Group')

class HrExpense(models.Model):
    _inherit = 'hr.expense'
    
    #hr_salary_advance_id  = fields.Many2one('hr.salary.advance', string='Advances Request', domain='[("employee_id","=", employee_id), ("state","in", ("paid","close"))]')

    hr_salary_advance_id  = fields.Many2one('hr.salary.advance', string='Advances Request', )
    advance_line_id  = fields.Many2one('hr.salary.advance.line', string='Advances Line', domain='[("advance_id","=", hr_salary_advance_id)]')
    hr_expense_sheet_type_id  = fields.Many2one('hr.expense.sheet.type', related='sheet_id.hr_expense_sheet_type_id')
    expense_type_id = fields.Many2one('hr.expense.type', string='Expense Category', copy=False)
    amount_approved = fields.Monetary(string='Approved Amount', compute='_compute_amount_approved', store=True)
    expense_approved = fields.Boolean(string='Is Approved', default=False)
    remarks = fields.Char(string='Remarks')
    fin_remarks = fields.Char(string='Finance Remarks')
    

    @api.depends('total_amount')
    def _compute_amount_approved(self):
        for line in self:
            line.update({
                'amount_approved': line.total_amount,
            })
    #@api.depends('product_id', 'company_id')
    def _compute_from_product_id_company_id(self):
        for expense in self.filtered('product_id'):
            expense = expense.with_company(expense.company_id)
            expense.name = expense.name or expense.product_id.display_name
            if not expense.attachment_number or (expense.attachment_number and not expense.unit_amount):
                expense.unit_amount = expense.unit_amount
            expense.product_uom_id = expense.product_id.uom_id
            expense.tax_ids = expense.product_id.supplier_taxes_id.filtered(lambda tax: tax.company_id == expense.company_id)  # taxes only from the same company
            account = expense.product_id.product_tmpl_id._get_product_accounts()['expense']
            if account:
                expense.account_id = account
    
   
    
    @api.onchange('hr_salary_advance_id')
    def onchange_advaces(self):
        if self.hr_salary_advance_id:
            self.update({
                'name': self.hr_salary_advance_id.name, 
                #'product_id': self.hr_salary_advance_id.product_id.id,
                'unit_amount': self.hr_salary_advance_id.amount_total,
                #'currency_id': self.hr_salary_advance_id.currency_id,
                'quantity': 1,
                'payment_mode': 'own_account',
            })
            
    @api.onchange('advance_line_id')
    def onchange_advace_line(self):
        if self.advance_line_id:
            self.update({
                'unit_amount': self.advance_line_id.unit_price,
                'quantity': self.advance_line_id.quantity,
                'product_id': False,
            })