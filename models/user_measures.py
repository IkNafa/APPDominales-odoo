from odoo import _, api, fields, models

class UserMeasures(models.Model):
    _name = 'user.measures'

    user_id = fields.Many2one('user.user', required=True)
    date = fields.Date(string="Fecha", required=True)
    weight = fields.Float(string="Peso", required=True)
    height = fields.Float(string="Altura", required=True)

    porGrasa = fields.Float(string="Porcentaje de grasa")
    masaMuscular = fields.Float(string="Masa muscular")

    contornoBrazo = fields.Float(string="Contorno brazo")
    contornoCintura = fields.Float(string="Contorno cintura")
    contornoMuslo = fields.Float(string="Contorno Muslo")
    contornoCuello = fields.Float(string="Contorno cuello")
    contornoPecho = fields.Float(string="Contorno pecho")
    contornoGemelo = fields.Float(string="Contorno gemelo")
    