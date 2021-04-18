from odoo import _, api, fields, models

class TrainerSurvey(models.Model):
    _name = 'trainer.survey'

    user_id = fields.Many2one('user.user', required=True)
    client_id = fields.Many2one('user.user', string="Client", required=True)
    estado = fields.Selection([('principal','Principal'),('semanal','Semanal')], string="Estado")
    question_ids = fields.One2many("trainer.survey.question",'survey_id', string="Questions")

class SurveyQuestion(models.Model):
    _name = "trainer.survey.question"
    _rec_name = "question"

    survey_id = fields.Many2one('trainer.survey', string="Survey", required=True)
    question = fields.Char(string="Question", required=True)
    answer_ids = fields.One2many('trainer.survey.answer','question_id',string="Answer")
    answer_count = fields.Integer(compute='_compute_answer_count', string='Answers')
    
    @api.depends('answer_ids')
    def _compute_answer_count(self):
        for record in self:
            record.answer_count = len(record.answer_ids)
    
class SurveyAnswer(models.Model):
    _name = "trainer.survey.answer"
    _rec_name = "answer"

    date = fields.Datetime(string="Date", default=fields.Datetime.now(), required=True)
    question_id = fields.Many2one('trainer.survey.question', string="Question", required=True)
    answer = fields.Char(string="Answer", required=True)
    