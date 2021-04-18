from odoo import _, api, fields, models

class User(models.Model):
    _name = 'user.user'
    _inherits = {"res.users": "odoo_user_id"}

    odoo_user_id = fields.Many2one("res.users", string="Odoo user")

    first_name = fields.Char(string="Nombre", required=True)
    last_names = fields.Char(string="Apellidos", required=True)

    bio = fields.Text(string="Biografía")
    birthday = fields.Date(string="Fecha de nacimiento")
    
    gender = fields.Selection([('masculino','Masculino'),('femenino','Femenino'),('otro','Otro')], string="Género")

    measures_count = fields.Integer(compute="_compute_measures_count",string="Measures")
    routine_count = fields.Integer(compute="_compute_routine_count", string="Routines")

    # Client

    trainer_id = fields.Many2one('user.user', string="Trainer", domain=[('is_trainer','=',True)])
    profession = fields.Char(string="Profession")

    # Trainer

    is_trainer = fields.Boolean(string="Is Trainer", default=False)

    client_ids = fields.One2many('user.user','trainer_id', string="Clients")
    rol_ids = fields.Many2many('user.rol', 'user_trainer_rol_rel','rol_id','user_id', string="Trainers")

    def _compute_measures_count(self):
        for record in self:
            record.measures_count = self.env['user.measures'].search_count([('user_id','=',record.id)])
    
    def _compute_routine_count(self):
        for record in self:
            record.routine_count = self.env['routine.routine'].search_count(['|',('owner_id','=',self.id),('client_id','=',self.id)])
    
    def open_user_routines(self):
        return {
            'name': self.login + ' routines',
            'view_mode': 'tree,form',
            'res_model': 'routine.routine',
            'type':'ir.actions.act_window',
            'domain':['|',('owner_id','=',self.id),('client_id','=',self.id)],
            'context':{'default_owner_id':self.id}
        }
    
    def open_user_measures(self):
        return {
            'name': self.login + ' measures',
            'view_mode': 'tree,form',
            'res_model': 'user.measures',
            'type':'ir.actions.act_window',
            'domain':[('user_id','=',self.id)],
            'context':{'default_user_id':self.id}
        }

    def setTrainer(self):
        for record in self:
            record.is_trainer = True

    @api.model
    def create(self, vals):
        if 'first_name' in vals and 'last_names' in vals:
            vals['name'] = vals['first_name'] + " " + vals['last_names']
        
        return super(User, self).create(vals)

class UserMark(models.Model):
    _name = "user.mark"

    user_id = fields.Many2one('user.user', string="User", required=True)
    routine_exercise_id = fields.Many2one('routine.exercise', string="Exercise", required=True)
    rm = fields.Float(string="RM", required=True)