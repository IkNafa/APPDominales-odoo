from odoo import _, api, fields, models

class Routine(models.Model):
    _name = 'routine.routine'

    training_id = fields.Many2one('training.training', required=True)

    name = fields.Char(string="Name", required=True)
    start_date = fields.Date(string="Start date")
    end_date = fields.Date(string="End Date")

    routine_exercise_ids = fields.One2many('routine.exercise','routine_id', string="Exercises")
    dayofweek_ids = fields.Many2many('routine.dayofweek', 'routine_dayofweek_rel', 'dayofweek_id', 'routine_id', string="Days of week")
    dayofweek_string = fields.Char(string="Days of week", compute="_compute_dayofweek_string")

    def _compute_dayofweek_string(self):
        for record in self:
            day_array = []
            for day in record.dayofweek_ids:
                day_array.append(day.code)
            record.dayofweek_string = '-'.join(day_array)


class DayOfWeek(models.Model):
    _name="routine.dayofweek"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True)
    index = fields.Integer(string="Index", required=True)

class RoutineDayOfWeekREl:
    _table="routine_dayofweek_rel"

    dayofweek_id = fields.Many2one('routine.dayofweek', required=True)
    routine_id = fields.Many2one('routine.routine', required=True)