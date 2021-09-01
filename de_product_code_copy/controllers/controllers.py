# -*- coding: utf-8 -*-
# from odoo import http


# class DeProductCodeCopy(http.Controller):
#     @http.route('/de_product_code_copy/de_product_code_copy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_product_code_copy/de_product_code_copy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_product_code_copy.listing', {
#             'root': '/de_product_code_copy/de_product_code_copy',
#             'objects': http.request.env['de_product_code_copy.de_product_code_copy'].search([]),
#         })

#     @http.route('/de_product_code_copy/de_product_code_copy/objects/<model("de_product_code_copy.de_product_code_copy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_product_code_copy.object', {
#             'object': obj
#         })
