from odoo import _, api, fields, models

class Training(models.Model):
    _name = 'training.training'

    owner_id = fields.Many2one('res.users', string="Owner User", required=True)
    client_id = fields.Many2one('res.users', string="Assigned to")

    name = fields.Char(string="Name", required=True)
    is_trainer = fields.Boolean(related="owner_id.is_trainer")

    routine_ids = fields.One2many('routine.routine','training_id',string="Routines")
    