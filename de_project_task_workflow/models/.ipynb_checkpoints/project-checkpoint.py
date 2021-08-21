# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import ast
from datetime import timedelta, datetime
from random import randint

from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import UserError, AccessError, ValidationError, RedirectWarning
from odoo.tools.misc import format_date, get_lang
from odoo.osv.expression import OR

class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'
    
    stage_code = fields.Char(string='Code', size=3)
    
    stage_category = fields.Selection([
        ('draft', 'Draft'),
        ('progress', 'In Progress'),
        ('close', 'Closed'),
    ], string='Category', default='draft')
    
    group_id = fields.Many2one('res.groups', string='Security Group')
    
    @api.constrains('sequence')
    def _check_sequence(self):
        ex_task_type_id = env['project.task.type']
        for record in self:
            ex_task_type_id = env['project.task.type'].search([('id','!=',record.id),('sequence','=',record.name),('active','=',True)],limit=1)
            if record.ex_task_type_id:
                raise ValidationError(_('Sequence already found.'))
    
class ProjectTask(models.Model):
    _inherit = 'project.task'
    
    task_stage_ids = fields.One2many('project.task.stage', 'task_id', string='Stage', copy=True)
    
    next_stage_id = fields.Many2one('project.task.type', string='Next Stage', compute='_compute_task_stage')
    prv_stage_id = fields.Many2one('project.task.type', string='Previous Stage', compute='_compute_task_stage')
    stage_code = fields.Char(related='stage_id.stage_code')
    stage_category = fields.Selection(related='stage_id.stage_category')
    date_submit = fields.Datetime('Submission Date', readonly=False)
    date_approved = fields.Datetime('Approved Date', readonly=False)
    date_refused = fields.Datetime('Refused Date', readonly=False)
    
    def write(self, vals):
        stage_id = self.env['project.task.type']
        result = super(ProjectTask,self).write(vals)
         # stage change: update date_last_stage_update
        if 'stage_id' in vals:
            stage_id = self.env['project.task.type'].browse(vals.get('stage_id'))
            for task in self.sudo():
                group_id = stage_id.group_id
                if group_id:
                    if not (group_id & self.env.user.groups_id):
                        raise UserError(_("You are not authorize to approve '%s'.", stage_id.name))
                
                if task.stage_id.stage_category == 'draft':
                    if task.order_stage_ids:
                        task.task_stage_ids.unlink()
                    self._compute_task_stages()
        return result
    
    def _compute_task_stages(self):
        stages_list = []
        next_stage = prv_stage = False
        for task in self:
            stage_ids = self.env['project.task.type'].search([('project_ids', '=', task.project_id.id)])
            for stage in stage_ids:
                stages_list.append({
                    'project_id': task.id,
                    'stage_id': stage.id, 
                    'sequence': stage.sequence,
                })            
            task.task_stage_ids.sudo().create(stages_list)
            #===================================
            #++++++++Assign Next Stage++++++++++++++
            stages = self.env['project.task.stage'].search([('project_id','=', task.id)], order="sequence desc")
            for stage in stages:
                stage.sudo().update({
                    'next_stage_id': next_stage,
                })
                next_stage = stage.stage_id.id
            #++++++++++++++++++++++++++++++++++++++++
            #+++++++++++Assign Previous Stage++++++++++
            stages = self.env['project.task.stage'].search([('project_id','=', task.id)], order="sequence asc")
            for stage in stages:
                stage.sudo().update({
                    'prv_stage_id': prv_stage,
                })
                prv_stage = stage.stage_id.id
            
    def unlink(self):
        for task in self:
            if task.stage_category != 'draft':
                raise UserError(_('You cannot delete a submitted task.'))
        return super(ProjectTask, self).unlink()
    
    def _compute_task_stage(self):
        for task in self:
            next_stage = prv_stage = False
            for stage in task.task_stage_ids.filtered(lambda t: t.stage_id.id == task.stage_id.id):
                    next_stage = stage.next_stage_id.id
                    prv_stage = stage.prv_stage_id.id
            task.next_stage_id = next_stage
            task.prv_stage_id = prv_stage
            
    def action_submit(self):
        for task in self.sudo():
            group_id = task.stage_id.group_id
            if group_id:
                if not (group_id & self.env.user.groups_id):
                    raise UserError(_("You are not authorize to submit task."))
        self.update({
            'stage_id' : self.next_stage_id.id,
            'date_submit' : fields.Datetime.now(),
        })
        
    def action_confirm(self):
        for task in self.sudo():
            group_id = task.stage_id.group_id
            if group_id:
                if not (group_id & self.env.user.groups_id):
                    raise UserError(_("You are not authorize to approve '%s'.", task.stage_id.name))
        
        if not self.next_stage_id:
            raise UserError(_("No stage to move forward."))
            
        self.update({
            'date_approved' : fields.Datetime.now(),
            'stage_id' : self.next_stage_id.id,
        })
        
    def action_refuse(self):
        for task in self.sudo():
            group_id = task.stage_id.group_id
            if group_id:
                if not (group_id & self.env.user.groups_id):
                    raise UserError(_("You are not authorize to approve '%s'.", task.stage_id.name))
        
        if not self.prv_stage_id:
            raise UserError(_("No stage to move backward."))
            
        self.update({
            'date_refused' : fields.Datetime.now(),
            'stage_id' : self.prv_stage_id.id,
        })


class ProjectTaskStage(models.Model):
    _name = 'project.task.stage'
    _description = 'Project Task Stages'
    _order = 'sequence'
    
    task_id = fields.Many2one('project.task', string='Task', index=True, required=True, ondelete='cascade')

    #task_stage_ids = fields.Many2many('project.task.type', string='Task Stage', compute='_compute_task_stages')
    stage_id = fields.Many2one('project.task.type', string='Stage', readonly=False, ondelete='restrict', tracking=True, index=True, copy=False)
    sequence = fields.Integer(string='Sequence')
    next_stage_id = fields.Many2one('project.task.type', string='Next Stage', readonly=False, ondelete='restrict', tracking=True, index=True, copy=False)
    prv_stage_id = fields.Many2one('project.task.type', string='Previous Stage', readonly=False, ondelete='restrict', tracking=True, index=True, copy=False)
    
    def _compute_task_stages(self):
        stages = stage_ids = self.env['project.task.type']
        for ts in self:
            stage_ids = self.env['project.task.type'].search([('project_ids','=',ts.task_id.project_id.id)])
            for stage in stage_ids:
                stages += stage
            ts.task_stage_ids = stages