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
    
    user_id = fields.Many2one('res.users', string='Assigned to', default=lambda self: self.env.uid, )
    stage_category = fields.Selection([
        ('draft', 'Draft'),
        ('progress', 'In Progress'),
        ('close', 'Closed'),
    ], string='Category', default='draft')
    
    group_id = fields.Many2one('res.groups', string='Security Group')
    
    @api.constrains('sequence')
    def _check_sequence(self):
        ex_task_type_id = self.env['project.task.type']
        for record in self:
            ex_task_type_id = self.env['project.task.type'].search([('id','!=',record.id),('sequence','=',record.sequence),('active','=',True)],limit=1)
            if ex_task_type_id.sequence:
                raise ValidationError(_('Sequence already found.'))
    
class ProjectTask(models.Model):
    _inherit = 'project.task'
    
    task_stage_ids = fields.One2many('project.task.stage', 'task_id', string='Stage', copy=True)
    
    next_stage_id = fields.Many2one('project.task.type', string='Next Stage', compute='_compute_task_stage')
    prv_stage_id = fields.Many2one('project.task.type', string='Previous Stage', compute='_compute_task_stage')
    stage_category = fields.Selection(related='stage_id.stage_category')
    date_submit = fields.Datetime('Submission Date', readonly=False)
    date_approved = fields.Datetime('Approved Date', readonly=False)
    date_refused = fields.Datetime('Refused Date', readonly=False)
    
    def write(self, vals):
        stage_id = self.env['project.task.type']
        user = False
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
                    if task.task_stage_ids:
                        task.task_stage_ids.unlink()
                    self._compute_task_all_stages()
                    
                if task.stage_id.user_id:
                    user = task.stage_id.user_id.id
                else:
                    user = task.user_id.id
                task.update({
                    'user_id': user,
                })
                
        return result
    
    def _compute_task_all_stages(self):
        stages_list = []
        next_stage = prv_stage = False
        for task in self:
            stage_ids = self.env['project.task.type'].search([('project_ids', '=', task.project_id.id)])
            for stage in stage_ids:
                stages_list.append({
                    'task_id': task.id,
                    'stage_id': stage.id, 
                    'sequence': stage.sequence,
                })            
            task.task_stage_ids.sudo().create(stages_list)
            #===================================
            #++++++++Assign Next Stage++++++++++++++
            stages = self.env['project.task.stage'].search([('task_id','=', task.id)], order="sequence desc")
            for stage in stages:
                stage.sudo().update({
                    'next_stage_id': next_stage,
                })
                next_stage = stage.stage_id.id
            #++++++++++++++++++++++++++++++++++++++++
            #+++++++++++Assign Previous Stage++++++++++
            stages = self.env['project.task.stage'].search([('task_id','=', task.id)], order="sequence asc")
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
        user = False
        for task in self.sudo():
            group_id = task.stage_id.group_id
            if group_id:
                if not (group_id & self.env.user.groups_id):
                    raise UserError(_("You are not authorize to submit task."))
            
            if not task.task_stage_ids:
                self._compute_task_all_stages()
                
            if task.next_stage_id.user_id:
                user = task.next_stage_id.user_id.id
            else:
                user = task.user_id.id
        self.activity_update()
        self.update({
            'stage_id' : self.next_stage_id.id,
            'date_submit' : fields.Datetime.now(),
            'user_id': user,
        })
        
    def action_confirm(self):
        user = False
        for task in self.sudo():
            group_id = task.stage_id.group_id
            if group_id:
                if not (group_id & self.env.user.groups_id):
                    raise UserError(_("You are not authorize to approve '%s'.", task.stage_id.name))
        
            if not task.next_stage_id:
                raise UserError(_("No stage to move forward."))
                
            if task.next_stage_id.user_id:
                user = task.next_stage_id.user_id.id
            else:
                user = task.user_id.id
        
        notification = {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('There are no task to approve.'),
                'type': 'warning',
                'sticky': False,  #True/False will display for few seconds if false
            },
        }
        self.update({
            'date_approved' : fields.Datetime.now(),
            'stage_id' : self.next_stage_id.id,
            'user_id': user,
        })
        notification['params'].update({
            'title': _('The task was successfully approved.'),
            'type': 'success',
            'next': {'type': 'ir.actions.act_window_close'},
        })
            
        self.activity_update()
        return notification
        
    def action_refuse(self):
        user = False
        for task in self.sudo():
            group_id = task.stage_id.group_id
            if group_id:
                if not (group_id & self.env.user.groups_id):
                    raise UserError(_("You are not authorize to approve '%s'.", task.stage_id.name))
        
            if not task.prv_stage_id:
                raise UserError(_("No stage to move backward."))
                
            if task.prv_stage_id.user_id:
                user = task.prv_stage_id.user_id.id
            else:
                user = task.user_id.id
        self.update({
            'date_refused' : fields.Datetime.now(),
            'stage_id' : self.prv_stage_id.id,
            'user_id': user,
        })

    def _get_responsible_for_approval(self):
        if self.user_id:
            return self.user_id
        return self.env['res.users']
    
    def activity_update(self):
        for task in self.filtered(lambda hol: hol.stage_category == 'draft'):
            self.activity_schedule('de_project_task_workflow.mail_act_task_approval', user_id=task.sudo()._get_responsible_for_approval().id or self.env.user.id)
        self.filtered(lambda hol: hol.stage_category == 'progress').activity_feedback(['de_project_task_workflow.mail_act_task_approval'])
        self.filtered(lambda hol: hol.stage_category in ('draft')).activity_unlink(['de_project_task_workflow.mail_act_task_approval'])

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