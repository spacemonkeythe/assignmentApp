from openerp import models, fields

class Feature(models.Model):
    _inherit = 'app.feature'

    priority = fields.Selection([('0', 'Low'), ('1', 'Normal'), ('2', 'High')],
            'Priority', default='0')
    kanban_state = fields.Selection([('normal', 'In Progress'),('blocked', 'Blocked'), ('done', 'Ready for next stage')],
            'Kanban State', default='normal')
    color = fields.Integer('Color Index')
