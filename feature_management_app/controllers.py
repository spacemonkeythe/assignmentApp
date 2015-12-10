# -*- coding: utf-8 -*-
from openerp import http

# class FeatureManagementApp(http.Controller):
#     @http.route('/feature_management_app/feature_management_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/feature_management_app/feature_management_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('feature_management_app.listing', {
#             'root': '/feature_management_app/feature_management_app',
#             'objects': http.request.env['feature_management_app.feature_management_app'].search([]),
#         })

#     @http.route('/feature_management_app/feature_management_app/objects/<model("feature_management_app.feature_management_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('feature_management_app.object', {
#             'object': obj
#         })