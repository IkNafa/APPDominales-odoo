# -*- coding: utf-8 -*-
from odoo import _, api, fields, models

class Marca(models.Model):
    _name = 'usuario.marca'

    usuario_id = fields.Many2one("usuario.usuario", string="Usuario", required=True)
    variante_id = fields.Many2one("variante.variante", string="Variante", required=True)
    ejercicio_id = fields.Many2one("ejercicio.ejercicio", string="Ejercicio", required=True)
    rm = fields.Float(string="Peso")
    
    