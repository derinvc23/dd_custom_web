# -*- coding: utf-8 -*-
from odoo import http

# class DdCustomWeb(http.Controller):
#     @http.route('/dd_custom_web/dd_custom_web/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dd_custom_web/dd_custom_web/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dd_custom_web.listing', {
#             'root': '/dd_custom_web/dd_custom_web',
#             'objects': http.request.env['dd_custom_web.dd_custom_web'].search([]),
#         })

#     @http.route('/dd_custom_web/dd_custom_web/objects/<model("dd_custom_web.dd_custom_web"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dd_custom_web.object', {
#             'object': obj
#         })