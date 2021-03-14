# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class Especialidad(models.Model):
    _name = 'entrenador.especialidad'
    _rec_name = "nombre"

    nombre = fields.Char(string="Especialidad")
    