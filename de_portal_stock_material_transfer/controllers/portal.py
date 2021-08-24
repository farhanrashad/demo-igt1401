# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import OrderedDict
from operator import itemgetter
from odoo.exceptions import UserError

from odoo import http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.tools import groupby as groupbyelem

from odoo.osv.expression import OR

def hoto_site_page_content(flag = 0):
    partners = request.env['res.users'].search([('id','=',http.request.env.context.get('uid'))])
    projects = request.env['project.project'].search([('name','=','HOTO')])
    sites = request.env['project.project'].search([('allow_site_planning','=',True)])
    return {
        'partners': partners,
        'projects': projects,
        'sites': sites,
        'success_flag' : flag,
    }



class CreateHotoTask(http.Controller):
    @http.route('/material/transfer/create/',type="http", website=True, auth='user')
    def hoto_task_create_template(self, **kw):
       return request.render("de_portal_stock_material_transfer.hoto_site_task_Create", hoto_site_page_content())
    
    
    @http.route('/hoto/task/save', type="http", auth="public", website=True)
    def hoto_task_save(self, **kw):
        if not kw.get('project_id'):
            raise UserError('You Are Not Allow to access HOTO Project!')
        if not kw.get('site_id'):
            raise UserError('You Are Not Allow to access any Site Project!')    
        vals = {
            'name': 'HOTO',
            'partner_id': int(kw.get('partner_id')),
            'project_id': int(kw.get('project_id')),
            'site_id': int(kw.get('site_id')),
            'site_hoto': True,
            'hoto_type': kw.get('hoto_type'),
            'date_handover': kw.get('date_handover'),
            'date_rfi': kw.get('date_rfi'),
            'date_onair': kw.get('date_onair'),
        }
        task = request.env['project.task'].create(vals)
        return request.redirect('/hoto/task/%s'%(task.id))

class CustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'hoto_count' in counters:
            active_user = request.env['res.users'].search([('id','=',http.request.env.context.get('uid'))])    
            values['hoto_count'] = request.env['project.task'].search_count([('partner_id','=', active_user.partner_id.id)])
        return values

   
    # ------------------------------------------------------------
    # My Task
    # ------------------------------------------------------------
    def _hoto_site_task_get_page_view_values(self, task, access_token, **kwargs):
        values = {
            'page_name': 'Hoto task',
            'task': task,
            'user': request.env.user
        }
        return self._get_page_view_values(task, access_token, values, 'hoto_tasks_history', False, **kwargs)

    @http.route(['/material/transfers', '/material/transfers/page/<int:page>'], type='http', auth="user", website=True)
    def portal_material_transfer_list(self, page=1, date_begin=None, date_end=None, sortby=None, filterby=None, search=None, search_in='content', groupby=None, **kw):
        values = self._prepare_portal_layout_values()
        searchbar_sortings = {
            'date': {'label': _('Newest'), 'order': 'create_date desc'},
            'name': {'label': _('Title'), 'order': 'name'},
            'stage': {'label': _('Stage'), 'order': 'stage_id'},
        }
        searchbar_filters = {
            'all': {'label': _('All'), 'domain': []},
        }
        searchbar_inputs = {
            'customer': {'input': 'partner_id', 'label': _('Search in Contractor')},
            'stage': {'input': 'stage_id.name', 'label': _('Search in Stages')},
            'all': {'input': 'all', 'label': _('Search in All')},
        }
        searchbar_groupby = {
            'none': {'input': 'none', 'label': _('None')},
            'stage': {'input': 'stage_id.name', 'label': _('Stage')},
        }

        # extends filterby criteria with project the customer has access to
        transfers = request.env['stock.transfer.order'].search([('name','=','HOTO')])
        for transfer in transfers:
            searchbar_filters.update({
                str(transfer.id): {'label': transfer.name, 'domain': [('id', '=', transfer.id)]}
            })

        # extends filterby criteria with project (criteria name is the project id)
        # Note: portal users can't view projects they don't follow

        # default sort by value
        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']

        # default filter by value
        if not filterby:
            filterby = 'all'
        domain = searchbar_filters.get(filterby, searchbar_filters.get('all'))['domain']

        # default group by value
        if not groupby:
            groupby = 'project'

        if date_begin and date_end:
            domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]

        # search
        if search and search_in:
            search_domain = []
            if search_in in ('content', 'all'):
                search_domain = OR([search_domain, ['|', ('name', 'ilike', search), ('description', 'ilike', search)]])
            if search_in in ('customer', 'all'):
                search_domain = OR([search_domain, [('partner_id', 'ilike', search)]])
            if search_in in ('message', 'all'):
                search_domain = OR([search_domain, [('message_ids.body', 'ilike', search)]])
            if search_in in ('stage', 'all'):
                search_domain = OR([search_domain, [('stage_id', 'ilike', search)]])
            if search_in in ('project', 'all'):
                search_domain = OR([search_domain, [('project_id', 'ilike', search)]])
            domain += search_domain
            
        active_user = request.env['res.users'].search([('id','=',http.request.env.context.get('uid'))])    
        domain += [('partner_id', '=', active_user.partner_id.id)]
        # task count
        task_count = request.env['project.task'].search_count(domain)
        # pager
        pager = portal_pager(
            url="/hoto/tasks",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby, 'filterby': filterby, 'groupby': groupby, 'search_in': search_in, 'search': search},
            total=task_count,
            page=page,
            step=self._items_per_page
        )
        # content according to pager and archive selected
        if groupby == 'project':
            order = "project_id, %s" % order  # force sort on project first to group by project in view
        elif groupby == 'stage':
            order = "stage_id, %s" % order  # force sort on stage first to group by stage in view

        tasks = request.env['project.task'].search(domain, order=order, limit=self._items_per_page, offset=pager['offset'])
        request.session['hoto_tasks_history'] = tasks.ids[:100]

        
        grouped_tasks = [tasks]

        values.update({
            'date': date_begin,
            'date_end': date_end,
            'grouped_tasks': grouped_tasks,
            'page_name': 'Hoto Task',
            'default_url': '/hoto/tasks',
            'pager': pager,
            'searchbar_sortings': searchbar_sortings,
            'searchbar_groupby': searchbar_groupby,
            'searchbar_inputs': searchbar_inputs,
            'search_in': search_in,
            'search': search,
            'sortby': sortby,
            'groupby': groupby,
            'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
            'filterby': filterby,
        })
        return request.render("de_portal_stock_material_transfer.portal_material_transfers", values)

   