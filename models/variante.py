# -*- coding: utf-8 -*-
from odoo import _, api, fields, models

class Variante(models.Model):
    _name = 'variante.variante'


    bar_id = fields.Many2one("variante.bar", string="Tipo de Barra")
    rango = fields.Many2one("variante.rango", string="Rango")
    tempo = fields.Many2one("variante.tempo", string="Tempo")
    stance = fields.Many2one("variante.stance", string="Stance")
    grip = fields.Many2one("variante.grip", string="Grip")

    def name_get(self):
        result=[]
        for record in self:
            display_name = []
            if record.bar_id:
                display_name.append(record.bar_id.display_name)
            if record.rango:
                display_name.append(record.rango.display_name)
            if record.tempo:
                display_name.append(record.tempo.display_name)
            if record.stance:
                display_name.append(record.stance.display_name)
            if record.grip:
                display_name.append(record.grip.display_name)
            
            result.append((record.id, '%s' % ",".join(display_name)))
        
        return result

class Bar(models.Model):
    _name = 'variante.bar'

    name = fields.Char(string="Nombre", required=True)


class Rango(models.Model):
    _name = 'variante.rango'

    name = fields.Char(string="Rango", required=True)

class Tempo(models.Model):
    _name = "variante.tempo"

    name = fields.Char(string="Tempo", required=True)

class Stance(models.Model):
    _name = "variante.stance"

    name = fields.Char(string="Stance", required=True)

class Grip(models.Model):
    _name = "variante.grip"

    name = fields.Char(string="Grip", required=True)
    
    
    