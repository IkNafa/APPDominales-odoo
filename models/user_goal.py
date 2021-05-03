from odoo import _, api, fields, models

class UserGoal(models.Model):
    _name = 'user.goal'

    user_id = fields.Many2one('res.users', required=True, ondelete="cascade")

    sequence = fields.Integer(string="Sequence")
    name = fields.Char(string="Name", store=True, compute="_compute_name")
    description = fields.Text(string="Description", required=True)

    @api.depends('sequence')
    def _compute_name(self):
        for record in self:
            record.name = "Objetivo %s" % str(record.sequence + 1)