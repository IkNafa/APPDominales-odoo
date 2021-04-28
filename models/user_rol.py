from odoo import _, api, fields, models

class TrainerRol(models.Model):
    _name = 'user.rol'

    name = fields.Char(string="Rol", required=True)
    user_ids = trainer_ids = fields.Many2many('res.users', 'res_users_rol_rel', 'user_id', 'rol_id', string="Users")


class ResUsersRolRel:
    _table = "res_users_rol_rel"

    rol_id = fields.Many2one('user.rol', string="Rol", required=True)
    user_id = fields.Many2one('res.users', string="Trainer", required=True)