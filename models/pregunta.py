# -*- coding: utf-8 -*-
from odoo import _, api, fields, models

class Pregunta(models.Model):
    _name = 'encuesta.pregunta'

    encuesta_id = fields.Many2one("encuesta.encuesta", required=True)
    pregunta = fields.Char(string="Pregunta", required=True)
    