# -*- coding: utf-8 -*-
from odoo import _, api, fields, models

class Rutina(models.Model):
    _name = 'rutina.rutina'

    name = fields.Char(string="Nombre", required=True)

    user_id = fields.Many2one("usuario.usuario", string="Creador", required=True)
    client_user_id = fields.Many2one("usuario.usuario", string="Cliente")

    rutina_ejercicio_ids = fields.One2many("rutina.ejercicio","rutina_id", string="Ejercicios")

    fecha_inicio = fields.Date(string="Fecha Inicio")
    fecha_fin = fields.Date(string="Fecha Fin")

    rutina_ids = fields.Many2many("appdominales.dayofweek", "rutina_dayofweek_rel", "dayofweek_id", "rutina_id")

class RutinaEjercicio(models.Model):
    _name = 'rutina.ejercicio'

    rutina_id = fields.Many2one("rutina.rutina", string="Rutina")
    
    ejercicio_id = fields.Many2one("ejercicio.ejercicio", string="Ejercicio")
    variante_id = fields.Many2one("variante.variante", string="Variante")
    set_ids = fields.One2many('ejercicio.set', "rutina_ejercicio_id", string="Sets")

    def name_get(self):
        result = []
        for record in self:
            display_name = []
            display_name.append(record.ejercicio_id.display_name)
            if record.variante_id:
                display_name.append(record.variante_id.display_name)
            if len(record.set_ids) > 0:
                display_name.append('%s x %s' % (str(len(record.set_ids)), "-".join(str(s.reps) for s in record.set_ids)))

            result.append((record.id, " | ".join(display_name)))

        return result

class Set(models.Model):
    _name = 'ejercicio.set'

    rutina_ejercicio_id = fields.Many2one("rutina.ejercicio", string="Ejercicio")

    orden = fields.Integer(string="Orden", required=True)
    peso = fields.Float(string="Peso")
    reps = fields.Integer(string="Reps", required=True)
    rpe = fields.Float(string="RPE/RIR")