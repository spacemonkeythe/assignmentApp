# -*- coding: utf-8 -*-
from openerp import http

# class FeatureManagementUser(http.Controller):
#     @http.route('/feature_management_user/feature_management_user/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/feature_management_user/feature_management_user/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('feature_management_user.listing', {
#             'root': '/feature_management_user/feature_management_user',
#             'objects': http.request.env['feature_management_user.feature_management_user'].search([]),
#         })

#     @http.route('/feature_management_user/feature_management_user/objects/<model("feature_management_user.feature_management_user"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('feature_management_user.object', {
#             'object': obj
#         })