# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Feature(models.Model):
    _name = 'app.feature'
    _description = 'Feature which needs to be developed.'

    title = fields.Char('Title', required=True)
    description = fields.Text()
    is_done = fields.Boolean('Is it done?')
    active = fields.Boolean('Is it active?', default=True)

    @api.one
    def toggle_done(self):
        self.is_done = not self.is_done

        return True

    @api.multi
    def clear_done_features(self):
        done_features = self.search([('is_done', '=', True)])

        done_features.write({'active': False})

        return True