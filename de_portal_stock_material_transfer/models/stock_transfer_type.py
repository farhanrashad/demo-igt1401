# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class TransferType(models.Model):
    _inherit = 'stock.transfer.order.type'

    website_published = fields.Boolean(string='Publish on Website')


# class ProjectTask(models.Model):
#     _inherit = 'project.task'
#
#
# class ResPartner(models.Model):
#     _inherit = 'res.partner'
#
# class ResUsers(models.Model):
#     _inherit = 'res.users'