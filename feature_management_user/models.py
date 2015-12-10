# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Feature(models.Model):
    _name = 'app.feature'
    _inherit = ['app.feature', 'mail.thread']

    user_id = fields.Many2one('res.users', 'Responsible Person')
    date_deadline = fields.Date('Deadline')
    title = fields.Char(help="What needs to be done?")
    description = fields.Text(help="What's the description of this feature?")

    @api.multi
    def clear_done_features(self):
        domain = [('is_done', '=', True),
                  '|', ('user_id', '=', self.env.uid),
                       ('user_id', '=', False)]
        done_features = self.search(domain)

        done_features.write({'active': False})

        return True

    @api.one
    def toggle_done(self):
        if self.user_id != self.env.user:
            raise Exception('Only the responsible can do this!')
        else:
            return super(Feature, self).toggle_done()