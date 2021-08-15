# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.safe_eval import safe_eval
from odoo.tools.misc import format_date

class ProjectProject(models.Model):
    _inherit = 'project.project'
    
    product_id = fields.Many2one('product.product', string='Tower Type', domain="[('is_product_category_tower','=',True)]")
    
    power_product_ids = fields.One2many('project.power.product.line', 'project_id', string='Power Line', copy=True)
    
    purchase_line_ids = fields.One2many('purchase.order.line', 'project_id', string='PO Lines', copy=False, readonly=True)
    site_billing_info_ids = fields.One2many('site.billing.info', 'site_id', string='Billing Info', copy=False, readonly=True)
    asset_ids = fields.One2many('account.asset', 'project_id', string='Assets', copy=False, readonly=True)
    
class ProjectPowerModelLine(models.Model):
    _name = 'project.power.product.line'
    _description = 'Project Power Products'
    
    project_id = fields.Many2one('project.project', string='Project', index=True, required=True, ondelete='cascade')
    period = fields.Char(string='Period')
    date_start = fields.Date(string='Start Date')
    date_end = fields.Date(string='End Date')
    product_id = fields.Many2one('product.product', string='Power Product', readonly=False, ondelete='restrict', tracking=True, index=True, copy=False,  domain="[('is_product_category_power','=',True)]" )