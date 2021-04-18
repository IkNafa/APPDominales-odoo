from odoo import _, api, fields, models

class RoutineExerciseSet(models.Model):
    _name = 'routine.exercise.set'

    routine_exercise_id = fields.Many2one('routine.exercise', string="Exercise", required=True)

    reps = fields.Integer(string="Reps", required=True)
    weight = fields.Float(string="Weight")
    rpe = fields.Integer(string="RPE/RIR")
    