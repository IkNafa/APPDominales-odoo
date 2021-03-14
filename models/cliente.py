# -*- coding: utf-8 -*-
from odoo import _, api, fields, models

class Cliente(models.Model):
    _name = 'usuario.cliente'
    _inherits = {"usuario.usuario":"usuario_id"}

    profesion = fields.Char(string="Profesión")
    usuario_id = fields.Many2one("usuario.usuario", string="Usuario")

    def open_medidas_usuario(self):
        return self.usuario_id.open_medidas_usuario()
    
    def open_rutinas_usuario(self):
        return self.usuario_id.open_rutinas_usuario()