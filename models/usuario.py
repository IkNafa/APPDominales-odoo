# -*- coding: utf-8 -*-
from odoo import _, api, fields, models, tools

class Usuario(models.Model):
    _name = 'usuario.usuario'
    _inherits = {"res.users":"odoo_usuario_id"}
    _rec_name = "login"

    apellidos = fields.Char(string="Apellidos")
    
    bio = fields.Text(string="Biografia")
    fecha_nac = fields.Date(string="Fecha de nacimiento")
    genero = fields.Selection([('m','Maculino'),('f','Femenino'),('o',"Otro")], string="Género")

    entrenador_ids = fields.Many2many("usuario.entrenador", "usuario_entrenador_rel", "entrenador_id", "usuario_id")

    odoo_usuario_id = fields.Many2one("res.users", string="Usuario de Odoo")

    medidas_count = fields.Integer(compute='_compute_medidas_count', string='Medidas')
    rutinas_count = fields.Integer(compute='_compute_rutinas_count', string="Rutinas")
    
    @api.depends('medidas_count')
    def _compute_medidas_count(self):
        self.medidas_count = self.env['usuario.medidas'].search_count([('user_id.id','=',self.id)])
    
    @api.depends('rutinas_count')
    def _compute_rutinas_count(self):
        self.rutinas_count = self.env['rutina.rutina'].search_count(['|',('user_id.id','=',self.id),('client_user_id','=',self.id)])

    def open_medidas_usuario(self):
        return {
            'name': 'Medidas de ' + self.login,
            'view_mode': 'tree,form,graph',
            'res_model': 'usuario.medidas',
            'type':'ir.actions.act_window',
            'domain':[('user_id.id','=',self.id)],
            'context':{'default_user_id':self.id}
        }

    def open_rutinas_usuario(self):
        return {
            'name': 'Biblioteca de rutinas de ' + self.login,
            'view_mode': 'tree,form',
            'res_model': 'rutina.rutina',
            'type':'ir.actions.act_window',
            'domain':['|',('user_id.id','=',self.id),('client_user_id','=',self.id)],
            'context':{'default_user_id':self.id}
        }