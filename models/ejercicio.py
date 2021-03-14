# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class Ejercicio(models.Model):
    _name = 'ejercicio.ejercicio'
    _rec_name = "nombre"

    nombre = fields.Char(string="Nombre", required=True)
    link = fields.Char(string="Video URL")

    grupo_id = fields.Many2one("ejercicio.grupo", string="Grupo muscular")

    image = fields.Binary(string="Foto", attachment=True)
    image_medium = fields.Binary(string="Foto (mediana)", attachment=True)
    image_small = fields.Binary(string="Foto (pequeña)", attachment=True)

class GrupoMuscular(models.Model):
    _name = 'ejercicio.grupo'
    _rec_name = "nombre"

    nombre = fields.Char(string="Nombre", required=True)

    @api.constrains('nombre')
    def _constrains_nombre(self):
        if self.env['ejercicio.grupo'].search([('nombre','=like',self.nombre),('id','!=',self.id)]):
            raise ValidationError("Ya existe un grupo con este nombre")
    