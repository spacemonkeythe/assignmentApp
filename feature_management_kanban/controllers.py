# -*- coding: utf-8 -*-
from openerp import http

# class FeatureManagementKanban(http.Controller):
#     @http.route('/feature_management_kanban/feature_management_kanban/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/feature_management_kanban/feature_management_kanban/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('feature_management_kanban.listing', {
#             'root': '/feature_management_kanban/feature_management_kanban',
#             'objects': http.request.env['feature_management_kanban.feature_management_kanban'].search([]),
#         })

#     @http.route('/feature_management_kanban/feature_management_kanban/objects/<model("feature_management_kanban.feature_management_kanban"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('feature_management_kanban.object', {
#             'object': obj
#         })