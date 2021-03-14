# -*- coding: utf-8 -*-
from odoo import _, api, fields, models

class Entrenador(models.Model):
    _name = 'usuario.entrenador'
    _inherits = {"usuario.usuario":"usuario_id"}
    _rec_name = "login"

    usuario_id = fields.Many2one("usuario.usuario", string="Usuario")
    especialidad = fields.Many2one("entrenador.especialidad", string="Especialidad")

    cliente_ids = fields.Many2many("usuario.usuario", "usuario_entrenador_rel", "usuario_id", "entrenador_id")

    def open_medidas_usuario(self):
        return self.usuario_id.open_medidas_usuario()

    def open_rutinas_usuario(self):
        return self.usuario_id.open_rutinas_usuario()
    