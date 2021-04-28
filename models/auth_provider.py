from odoo import _, api, fields, models

class AuthProvider(models.Model):
    _name = 'auth.provider'

    name = fields.Char(string="Provider name", required=True)
    