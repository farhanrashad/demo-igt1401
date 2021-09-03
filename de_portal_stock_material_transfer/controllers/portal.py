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

stock_transfer_list = []
stock_transfer_return_list = []


def stock_material_page_content(flag = 0):
    partners = request.env['res.users'].sudo().search([('id','=',http.request.env.context.get('uid'))])
    transfer_category = request.env['stock.transfer.order.category'].sudo().search([('website_published','=',True)])
    transfer_type = request.env['stock.transfer.order.type'].sudo().search([('website_published','=',True)])
    return {
        'partners': partners,
        'transfer_category': transfer_category,
        'transfer_type': transfer_type,
        'success_flag' : flag,
    }

def stock_material_type_page_content(flag = 0):
    transfer_types = request.env['stock.transfer.order.type'].sudo().search([('website_published','=',True)])
    transfer_type_list = []
    for transfer in transfer_types:
        for group in transfer.group_id.users:
            if group.id == http.request.env.context.get('uid'):
                transfer_type_list.append(transfer.id)

    transfer_type = request.env['stock.transfer.order.type'].search([('id', 'in', transfer_type_list)])
    transfer_categories = request.env['stock.transfer.order.category'].sudo().search([('website_published','=',True)])
    transfer_categ_list = []
    for categ in transfer_categories:
        for group in categ.group_id.users:
            if group.id == http.request.env.context.get('uid'):
                transfer_categ_list.append(categ.id)

    transfer_category = request.env['stock.transfer.order.category'].search([('id', 'in', transfer_categ_list)])

    return {
        'transfer_category': transfer_category,
        'transfer_type': transfer_type,
    }

def stock_material_category_page_content(transfer_category, transfer_type):
    transfer_types = transfer_type
    transfer_type_list = []
    for transfer in transfer_types:
        for group in transfer.group_id.users:
            if group.id == http.request.env.context.get('uid'):
                transfer_type_list.append(transfer.id)

    transfer_type = request.env['stock.transfer.order.type'].sudo().search([('id', 'in', transfer_type_list)])
    transfer_categories = transfer_category
    transfer_category_list = []
    for categ in transfer_categories:
        for group in categ.group_id.users:
            if group.id == http.request.env.context.get('uid'):
                transfer_category_list.append(categ.id)
    transfer_category = request.env['stock.transfer.order.category'].sudo().search([('id', 'in', transfer_category_list)])
    src_lists = request.env['stock.location'].sudo().search([])
    destination_lists = request.env['stock.location'].sudo().search([])

    return {
        'src_lists': src_lists,
        'destination_lists': destination_lists, 
        'transfer_category': transfer_category,
        'transfer_type': transfer_type.id,
    }


def stock_material_type_categ_page_content(transfer_category, transfer_type):
    global stock_transfer_list
    global stock_transfer_return_list
    product_lists = request.env['product.product'].sudo().search([])
    project_lists = request.env['project.project'].sudo().search([])
    product_lists = request.env['product.product'].sudo().search([])
    transfer_lists = request.env['stock.transfer.order'].sudo().search([])
    purchase_lists = request.env['purchase.order'].sudo().search([])
    transporter_lists = request.env['res.partner'].sudo().search([])
    supplier_lists = request.env['res.partner'].sudo().search([])
    transfer_categ_list = []
    transfer_categories = transfer_category
    for categ in transfer_categories:
        for group in categ.group_id.users:
            if group.id == http.request.env.context.get('uid'):
                transfer_categ_list.append(categ.id)
    transfer_category = request.env['stock.transfer.order.category'].sudo().search([('id','in',transfer_categ_list)])
    has_reference = '0'
    if transfer_category.has_reference == 'optional':
        has_reference = '1'
    if transfer_category.has_reference == 'required':
        has_reference = '2'
    has_purchase_order = '0'
    if transfer_category.has_purchase_order == 'optional':
        has_purchase_order = '1'
    if transfer_category.has_purchase_order == 'required':
        has_purchase_order = '2'
    has_transfer_order = '0'
    if transfer_category.has_transfer_order == 'optional':
        has_transfer_order = '1'
    if transfer_category.has_transfer_order == 'required':
        has_transfer_order = '2'
    has_transporter = '0'
    if transfer_category.has_transporter == 'optional':
        has_transporter = '1'
    if transfer_category.has_transporter == 'required':
        has_transporter = '2'
    returnable = '0'
    if transfer_category.action_type == 'returnable':
        returnable = '1'
    src_lists = request.env['stock.location'].sudo().search([('id','=',transfer_category.location_src_id.id)])
    destination_lists = request.env['stock.location'].sudo().search([('id','=',transfer_category.location_dest_id.id)])
    return {
        'src_lists':  src_lists,
        'destination_lists': destination_lists, 
        'product_lists': product_lists,
        'returnable': returnable,
        'has_transporter': has_transporter,
        'has_purchase_order': has_purchase_order,
        'has_reference': has_reference,
        'has_transfer_order': has_transfer_order,
        'purchase_lists': purchase_lists,
        'transfer_lists': transfer_lists,
        'project_lists': project_lists,
        'transporter_lists': transporter_lists,
        'stock_transfer_list': stock_transfer_list,
        'stock_transfer_return_list': stock_transfer_return_list,
        'supplier_lists': supplier_lists,
        'categ': transfer_category,
        'transfer_category': transfer_category.id,
        'transfer_type': transfer_type.id,
    }



class CreateStockMaterial(http.Controller):

    @http.route('/stock/material/type/',type="http", website=True, auth='user')
    def stock_material_type_template(self, **kw):
       return request.render("de_portal_stock_material_transfer.stock_transfer_type", stock_material_type_page_content())

    @http.route('/stock/material/type/categ/', type="http", website=True, auth='user')
    def stock_material_type_categ_template(self, **kw):
        id = int(kw.get('transfer_type_id'))
        transfer_type = request.env['stock.transfer.order.type'].sudo().search([('id','=',id)])
        transfer_category = request.env['stock.transfer.order.category'].sudo().search([('transfer_order_type_id','=',id)])
        return request.render("de_portal_stock_material_transfer.stock_transfer_type_categ_Create",
                              stock_material_category_page_content(transfer_category, transfer_type))

    @http.route('/stock/material/transfer/categ/', type="http", website=True, auth='user')
    def stock_material_transfer_categ_template(self, **kw):
        global stock_transfer_list
        global stock_transfer_return_list
        stock_transfer_return_list = []
        stock_transfer_list = []
        id = int(kw.get('transfer_type_id'))
        transfer_type = request.env['stock.transfer.order.type'].sudo().search([('id','=',id)])
        transfer_category = request.env['stock.transfer.order.category'].sudo().search([('id','=',int(kw.get('categ_id')))])

        return request.render("de_portal_stock_material_transfer.portal_create_stock_material_transfer",
                              stock_material_type_categ_page_content(transfer_category, transfer_type))

    @http.route('/stock/material/save', type="http", auth="public", website=True)
    def create_stock_material(self, **kw):
        list = []

        global stock_transfer_list
        global stock_transfer_return_list
        has_purchase = False
        has_transfer = False
        has_transporter = False
        if kw.get('purchase_id'):
            has_purchase = int(kw.get('purchase_id'))
        if kw.get('transfer_id'):
            has_transfer = int(kw.get('transfer_id'))
        if kw.get('transporter_id'):
            has_transporter = int(kw.get('transporter_id'))

        material_val = {
            'purchase_id': has_purchase,
            'stock_transfer_order_id': has_transfer,
            'transfer_order_type_id': int(kw.get('transfer_type_id')),
            'stage_id': request.env['stock.transfer.order.stage'].sudo().search([('stage_category','=','draft')], limit=1).id,
            'transfer_order_category_id': int(kw.get('transfer_category_id')),
            'partner_id':request.env['res.users'].sudo().search([('id','=',http.request.env.context.get('uid'))]).partner_id.id,
            'transporter_id': has_transporter,
            'reference': kw.get('reference'),
        }
        record = request.env['stock.transfer.order'].sudo().create(material_val)
        for stock in stock_transfer_list:
            line_vals = {
                'stock_transfer_order_id': record.id,
                'product_id': stock['product_id'],
                'name': stock['name'],
                'product_uom_qty': stock['product_uom_qty'],
                'project_id': stock['project_id'],
                'date_scheduled': stock['date_scheduled'],
                'supplier_id': stock['supplier_id'],
                'location_dest_id': stock['location_dest_id'] if stock['location_dest_id'] else False, 
            }
            record_lines = request.env['stock.transfer.order.line'].sudo().create(line_vals)
        stock_transfer_list = []
        for stockline in stock_transfer_return_list:
            line_vals = {
                'stock_transfer_order_id': record.id,
                'product_id': stockline['product_id'],
                'name': stockline['name'],
                'product_uom_qty': stockline['product_uom_qty'],
                'project_id': stockline['project_id'],
                'date_scheduled': stockline['date_scheduled'],
                'location_src_id': stockline['location_src_id'] if stockline['location_src_id'] else False,
            }
            record_lines = request.env['stock.transfer.return.line'].sudo().create(line_vals)
        stock_transfer_return_list = []
        return request.render("de_portal_stock_material_transfer.stock_material_submited", {})

    @http.route('/stock/material/line/save', type="http", auth="public", website=True)
    def create_stock_material_line(self, **kw):
        global stock_transfer_list

        line_vals = {
            'product_id': int(kw.get('product_id')),
            'name': kw.get('name'),
            'product_uom_qty': kw.get('product_uom_qty'),
            'project_id': int(kw.get('project_id')),
            'date_scheduled': kw.get('date_scheduled'),
            'supplier_id': int(kw.get('supplier_id')),
            'location_dest_id': int(kw.get('location_dest_id')) if kw.get('location_dest_id') else False,
        }
        stock_transfer_list.append(line_vals)
        transfer_type = request.env['stock.transfer.order.type'].sudo().search([('id', '=', int(kw.get('transfer_type_id_line')))])
        transfer_category = request.env['stock.transfer.order.category'].sudo().search([('id', '=', int(kw.get('transfer_category_id_line')))])
        return request.render("de_portal_stock_material_transfer.portal_create_stock_material_transfer", stock_material_type_categ_page_content(transfer_category, transfer_type))

    @http.route('/stock/material/return/line/save', type="http", auth="public", website=True)
    def create_stock_material_return_line(self, **kw):
        global stock_transfer_return_list

        line_vals = {
            'product_id': int(kw.get('product_id')),
            'name': kw.get('name'),
            'product_uom_qty': kw.get('product_uom_qty'),
            'project_id': int(kw.get('project_id')),
            'date_scheduled': kw.get('date_scheduled'),
            'location_src_id': int(kw.get('location_src_id')) if kw.get('location_src_id') else False,
        }
        stock_transfer_return_list.append(line_vals)
        transfer_type = request.env['stock.transfer.order.type'].sudo().search([('id', '=', int(kw.get('transfer_type_id_line')))])
        transfer_category = request.env['stock.transfer.order.category'].sudo().search([('id', '=', int(kw.get('transfer_category_id_line')))])
        return request.render("de_portal_stock_material_transfer.portal_create_stock_material_transfer", stock_material_type_categ_page_content(transfer_category, transfer_type))


class CustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'material_count' in counters:
            active_user = request.env['res.users'].sudo().search([('id','=',http.request.env.context.get('uid'))])    
            values['material_count'] = request.env['stock.transfer.order'].sudo().search_count([('partner_id','=', active_user.partner_id.id)])
        return values

   
    # ------------------------------------------------------------
    # Stock Transfer
    # ------------------------------------------------------------
    def _stock_material_get_page_view_values(self, stock_material, access_token, **kwargs):
        returnable = '0'
        if stock_material.transfer_order_category_id.action_type == 'returnable':
            returnable = '1'
        values = {
            'returnable': returnable,
            'page_name': 'stock_material',
            'stock_material': stock_material,
            'user': request.env.user
        }
        return self._get_page_view_values(stock_material, access_token, values, 'stock_material_history', False, **kwargs)

    @http.route(['/stock/materials', '/stock/materials/page/<int:page>'], type='http', auth="user", website=True)
    def portal_stock_materials(self, page=1, date_begin=None, date_end=None, sortby=None, filterby=None, search=None, search_in='content', groupby=None, **kw):
        values = self._prepare_portal_layout_values()
        searchbar_sortings = {
            'date': {'label': _('Newest'), 'order': 'create_date desc'},
            'name': {'label': _('Title'), 'order': 'name'},
            'stage': {'label': _('Stage'), 'order': 'stage_id'},
            'update': {'label': _('Last Stage Update'), 'order': 'date_last_stage_update desc'},
        }
        searchbar_filters = {
            'all': {'label': _('All'), 'domain': []},
        }
        searchbar_inputs = {
            'message': {'input': 'message', 'label': _('Search in Messages')},
            'customer': {'input': 'customer', 'label': _('Search in Customer')},
            'stage': {'input': 'stage', 'label': _('Search in Stages')},
            'all': {'input': 'all', 'label': _('Search in All')},
        }
        searchbar_groupby = {
            'none': {'input': 'none', 'label': _('None')},
            'stage': {'input': 'stage', 'label': _('Stage')},
        }

        # default sort by value
        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']

        # default filter by value
        if not filterby:
            filterby = 'all'
        domain = searchbar_filters.get(filterby, searchbar_filters.get('all'))['domain']
        if not groupby:
            groupby = 'stage'

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

            domain += search_domain
            
        active_user = request.env['res.users'].sudo().search([('id','=',http.request.env.context.get('uid'))])    
        domain += [('partner_id', '=', active_user.partner_id.id)]
        # task count
        stock_material_count = request.env['stock.transfer.order'].sudo().search_count(domain)
        # pager
        pager = portal_pager(
            url="/stock/materials",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby, 'filterby': filterby, 'groupby': groupby, 'search_in': search_in, 'search': search},
            total=stock_material_count,
            page=page,
            step=self._items_per_page
        )

        materials = request.env['stock.transfer.order'].sudo().search(domain, order=order, limit=self._items_per_page, offset=pager['offset'])
        request.session['stock_material_history'] = materials.ids[:100]

        
        grouped_materials = [materials]

        values.update({
            'date': date_begin,
            'date_end': date_end,
            'grouped_materials': grouped_materials,
            'page_name': 'stock_material',
            'default_url': '/stock/materials',
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
        return request.render("de_portal_stock_material_transfer.portal_stock_materials", values)

    @http.route(['/stock/material/<int:material_id>'], type='http', auth="public", website=True)
    def portal_stock_material(self, material_id, access_token=None, **kw):
        try:
            task_sudo = request.env['stock.transfer.order'].sudo().search([('id', '=', material_id)])
        except (AccessError, MissingError):
            return request.redirect('/my')


        values = self._stock_material_get_page_view_values(task_sudo, access_token, **kw)
        return request.render("de_portal_stock_material_transfer.portal_stock_material", values)
