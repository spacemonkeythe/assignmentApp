# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class Tag(models.Model):
    _name = 'app.feature.tag'

    name = fields.Char('Name', size=40, translate=True)
    task_ids = fields.Many2many('app.feature', string='Tasks')


class Stage(models.Model):
    _name = 'app.feature.stage'
    _order = 'sequence,name'
    _rec_name = 'name'
    _table_name = 'feature_stage'

    name = fields.Char(
        string='Name',
        # Common field attributes:
        copy=False,
        default='New',
        groups="base.group_user,base.group_no_one",
        help='The title for the stage.',
        index=True,
        readonly=False,
        required=True,
        states={'done': [('readonly', False)]},
        size=40,
        translate=True,
    )

    sequence = fields.Integer('Sequence')

    description = fields.Text('Description')
    state = fields.Selection([('draft', 'New'), ('open', 'Started'), ('done', 'Closed')],'State',)
    documentations = fields.Html('Documentation')

    percent_complete = fields.Float('% Complete', (3, 2))

    date_effective = fields.Date('Effective Date')
    date_changed = fields.Datetime('Last Changed')

    image = fields.Binary('Image')

    feature_ids = fields.One2many('app.feature', 'stage_id', 'Features in this stage')

class Feature(models.Model):
    _inherit = 'app.feature'

    stage_id = fields.Many2one('app.feature.stage', 'Stage')
    tag_ids = fields.Many2many('app.feature.tag', string='Tags')

    @api.one
    @api.constrains('title')
    def _check_title_size(self):
        if len(self.title) < 5:
            raise ValidationError('Title must have 5 chars!')

    _sql_constraints = [(
        'app_feature_title_unique',
        'UNIQUE (title, user_id, active)',
        'Feature title must be unique!'
    )]

    # Related field:
    stage_state = fields.Selection(
        related='stage_id.state',
        string='Stage State',
        store=True,
    )

    @api.one
    def compute_user_feature_count(self):
        self.user_feature_count = self.search_count(
            [('user_id', '=', self.user_id.id)])

    user_feature_count = fields.Integer(
        'User Feature Count',
        compute='compute_user_feature_count'
    )

    effort_estimate = fields.Integer('Effort Estimate')
