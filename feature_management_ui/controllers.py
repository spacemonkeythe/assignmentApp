# -*- coding: utf-8 -*-
from openerp import http

# class FeatureManagementUi(http.Controller):
#     @http.route('/feature_management_ui/feature_management_ui/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/feature_management_ui/feature_management_ui/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('feature_management_ui.listing', {
#             'root': '/feature_management_ui/feature_management_ui',
#             'objects': http.request.env['feature_management_ui.feature_management_ui'].search([]),
#         })

#     @http.route('/feature_management_ui/feature_management_ui/objects/<model("feature_management_ui.feature_management_ui"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('feature_management_ui.object', {
#             'object': obj
#         })