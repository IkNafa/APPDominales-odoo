from odoo import _, api, fields, models

class DayOfWeek(models.Model):
    _name = 'appdominales.dayofweek'
    
    name = fields.Char(string="Nombre", translate=True)
    code = fields.Char(string="Code")

    rutina_ids = fields.Many2many("rutina.rutina", "rutina_dayofweek_rel", "rutina_id", "dayofweek_id")

class RutinaDaysRel(models.Model):
    _name = 'rutina.dayofweek.rel'
    _table = 'rutina_dayofweek_rel'

    dayofweek_id = fields.Many2one('appdominales.dayofweek', required=True)
    rutina_id = fields.Many2one('rutina.rutina', required=True)