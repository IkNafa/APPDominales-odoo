# -*- coding: utf-8 -*-
from odoo import _, api, fields, models

class Medidas(models.Model):
    _name = 'usuario.medidas'
    _rec_name = "fecha"
    

    user_id = fields.Many2one('usuario.usuario', string="Usuario", required=True)

    fecha = fields.Date(string="Fecha", required=True)
    peso = fields.Float(string="Peso (kg)", required=True)
    altura = fields.Integer(string="Altura (cm)", required=True)
    porGrasa = fields.Float(string = "Porcentaje de grasa")
    masaMuscular = fields.Float(string="Masa muscular")

    contorno_brazo = fields.Float(string="Brazo")
    contorno_cintura = fields.Float(string="Cintura")
    contorno_muslo = fields.Float(string="Muslo")
    contorno_cuello = fields.Float(string="Cuello")
    contorno_pecho = fields.Float(string="Pecho")
    contorno_gemelo = fields.Float(string="Gemelo")
    