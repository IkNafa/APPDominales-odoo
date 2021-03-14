# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class EntrenaRel(models.Model):
    _name = 'usuario.entrenador.rel'
    _table = "usuario_entrenador_rel"

    usuario_id = fields.Many2one('usuario.usuario', string="Usuario")
    entrenador_id = fields.Many2one('usuario.entrenador', string="Entrenador")