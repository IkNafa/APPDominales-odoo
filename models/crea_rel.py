# -*- coding: utf-8 -*-
from odoo import _, api, fields, models

class CreaRel(models.Model):
    _name = 'entrenador.encuesta.rel'
    _table = "entrenador_encuesta_rel"

    entrenador_id = fields.Many2one("usuario.entrenador", string="Entrenador", required=True)
    encuesta_id = fields.Many2one("encuesta.encuesta", string="Encuesta", required=True)
    