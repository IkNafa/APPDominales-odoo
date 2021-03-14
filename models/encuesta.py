# -*- coding: utf-8 -*-
from odoo import _, api, fields, models

class Encuesta(models.Model):
    _name = 'encuesta.encuesta'
    
    estado = fields.Selection([('inicial','Inicial'),('seguimiento',"Seguimiento")], string="Estado", default="seguimiento")
    pregunta_ids = fields.One2many("encuesta.pregunta", "encuesta_id", string="Preguntas")
    
    usuario_id = fields.Many2one("usuario.usuario", string="Usuario asignador", required=True)
    