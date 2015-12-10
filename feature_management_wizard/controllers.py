# -*- coding: utf-8 -*-
from openerp import http

# class FeatureManagementWizard(http.Controller):
#     @http.route('/feature_management_wizard/feature_management_wizard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/feature_management_wizard/feature_management_wizard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('feature_management_wizard.listing', {
#             'root': '/feature_management_wizard/feature_management_wizard',
#             'objects': http.request.env['feature_management_wizard.feature_management_wizard'].search([]),
#         })

#     @http.route('/feature_management_wizard/feature_management_wizard/objects/<model("feature_management_wizard.feature_management_wizard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('feature_management_wizard.object', {
#             'object': obj
#         })