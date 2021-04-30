from odoo import _, api, fields, models, tools

class ResUsers(models.Model):
    _inherit = 'res.users'

    def _get_default_provider_id(self):
        return self.env['auth.provider'].search([('name','=','Odoo')],limit=1).id

    is_appdominales_user = fields.Boolean(default=True)

    is_trainer = fields.Boolean(default=False)
    birthday = fields.Date(string="Birthday")
    gender = fields.Selection([('masculino','Masculino'),('femenino','Femenino'),('otro','Otro')], string="Género")
    provider_id = fields.Many2one('auth.provider', string="Provider", default=_get_default_provider_id)
    
    rol_ids = trainer_ids = fields.Many2many('user.rol', 'res_users_rol_rel', 'rol_id','user_id',string="Rol")

    client_ids = fields.One2many('res.users', 'trainer_id', string="Clients")
    client_count = fields.Integer(compute="_compute_client_count", string="Clients")

    trainer_id = fields.Many2one('res.users',domain=[('is_trainer','=',True)],string="Trainer")
    rating_ids = fields.One2many('trainer.rating','trainer_id', string="Ratings")
    rating_mean = fields.Float(compute="_compute_rating_mean")

    firebase_token = fields.Char(string="Firebase token")

    measures_count = fields.Integer(compute="_compute_measures_count",string="Measures")
    training_count = fields.Integer(compute="_compute_training_count", string="trainings")
    survey_count = fields.Integer(compute="_compute_survey_count",string="Surveys")

    goal_ids = fields.One2many('user.goal', 'user_id', string="Goals")


    def _compute_rating_mean(self):
        for record in self:
            if not record.rating_ids:
                continue
            
            total = 0
            for rating_id in record.rating_ids:
                total += rating_id.rating
            record.rating_mean = total / len(record.rating_ids)
    
    def _compute_client_count(self):
        for record in self:
            record.client_count = len(record.client_ids)

    def _compute_measures_count(self):
        for record in self:
            record.measures_count = self.env['user.measures'].search_count([('user_id','=',record.id)])
    
    def _compute_training_count(self):
        for record in self:
            record.training_count = self.env['training.training'].search_count(['|',('owner_id','=',self.id),('client_id','=',self.id)])

    def _compute_survey_count(self):
        for record in self:
            record.survey_count = self.env['trainer.survey'].search_count([('user_id','=',self.id)])
    
    def open_user_trainings(self):
        return {
            'name': self.name + ' trainings',
            'view_mode': 'tree,form',
            'res_model': 'training.training',
            'type':'ir.actions.act_window',
            'domain':['|',('owner_id','=',self.id),('client_id','=',self.id)],
            'context':{'default_owner_id':self.id}
        }
    
    def open_user_measures(self):
        return {
            'name': self.name + ' measures',
            'view_mode': 'tree,form',
            'res_model': 'user.measures',
            'type':'ir.actions.act_window',
            'domain':[('user_id','=',self.id)],
            'context':{'default_user_id':self.id}
        }

    def open_user_surveys(self):
        return {
            'name': self.name + ' surveys',
            'view_mode': 'tree,form',
            'res_model': 'trainer.survey',
            'type':'ir.actions.act_window',
            'domain':[('user_id','=',self.id)],
            'context':{'default_user_id':self.id}
        }

    def setTrainer(self):
        for record in self:
            record.is_trainer = True

class UserMark(models.Model):
    _name = "user.mark"

    user_id = fields.Many2one('res.users', string="User", required=True)
    routine_exercise_id = fields.Many2one('routine.exercise', string="Exercise", required=True)
    rm = fields.Float(string="RM", required=True)