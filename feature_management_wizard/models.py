# -*- coding: utf-8 -*-
from openerp import exceptions
from openerp import models, fields, api


class FeatureWizard(models.TransientModel):
    _name = 'app.feature.wizard'

    feature_ids = fields.Many2many('app.feature', string='Features')
    new_user_id = fields.Many2one('res.users', string='Set Responsible Person')
    new_deadline = fields.Date('Set Deadline')

    @api.multi
    def count_active_features(self):
        Feature = self.env['app.feature']
        count = Feature.search_count([])

        raise exceptions.Warning(
            'There are %d active features.' % count)

    @api.multi
    def reopen_wizard(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,  # this model
            'res_id': self.id,  # the current wizard record
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new'}

    @api.multi
    def update_features(self):
        self.ensure_one()

        Feature = self.env['app.feature']
        all_features = Feature.search([])
        self.feature_ids = all_features

        return self.reopen_wizard()

    @api.multi
    def all_features_update(self):
        self.ensure_one()

        if not (self.new_deadline or self.new_user_id):
            raise exceptions.ValidationError('No data to update!')

        if self.new_deadline:
            self.feature_ids.write({'date_deadline': self.new_deadline})

        if self.new_user_id:
            self.feature_ids.write({'user_id': self.new_user_id.id})

        return True