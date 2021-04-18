from odoo import _, api, fields, models

class TrainerRol(models.Model):
    _name = 'user.rol'

    name = fields.Char(string="Rol", required=True)
    trainer_ids = fields.Many2many('user.user', 'user_trainer_rol_rel', 'user_id', 'rol_id', string="Trainers")

class UserTrainerRolRel:
    _table = "user_trainer_rol_rel"

    rol_id = fields.Many2one('user.rol', string="Rol", required=True)
    user_id = fields.Many2one('user.user', string="Trainer", required=True)