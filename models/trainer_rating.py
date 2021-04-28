from odoo import _, api, fields, models

class TrainerRating(models.Model):
    _name = 'trainer.rating'

    trainer_id = fields.Many2one('res.users', domain="[('is_appdominales_user','=',True)]", required=True)
    client_id = fields.Many2one('res.users', required=True)
    rating = fields.Integer(string="Rating",compute="_compute_rating")
    rating_selection = fields.Selection([('0', 'Very Low'),('1', 'Low'),('2', 'Normal'),('3', 'High'),('4', 'Very High')], required=True, string="Rating")

    @api.depends('rating_selection')
    def _compute_rating(self):
        for record in self:
            record.rating = int(record.rating_selection)