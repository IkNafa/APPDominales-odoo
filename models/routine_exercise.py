from odoo import _, api, fields, models

class RoutineExercise(models.Model):
    _name = 'routine.exercise'

    routine_id = fields.Many2one('routine.routine', string="Routine", required=True, ondelete="cascade")
    exercise_id = fields.Many2one('exercise.exercise', string="Exercise", required=True, ondelete="cascade")

    name = fields.Char(string="Name", related="exercise_id.name")
    description = fields.Text(string="Description", related="exercise_id.description")
    external_video = fields.Char(string="URL", related="exercise_id.external_video")
    group_id = fields.Many2one('exercise.group', related="exercise_id.group_id")

    image = fields.Binary(string="Image", related="exercise_id.image")
    image_medium = fields.Binary(string="Image medium", related="exercise_id.image_medium")
    image_small = fields.Binary(string="Image small", related="exercise_id.image_small")

    bartype_id = fields.Many2one('exercise.bar', string="Bar type")
    range_id = fields.Many2one('exercise.range', string="Range")
    tempo_id = fields.Many2one('exercise.tempo', string="Tempo")
    stance_id = fields.Many2one('exercise.stance', string="Stance")
    grip_id = fields.Many2one('exercise.grip', string="Grip")

    set_ids = fields.One2many('routine.exercise.set','routine_exercise_id', string="Sets")

class BarType(models.Model):
    _name = "exercise.bar"

    name = fields.Char(string="Name", required=True)

class RangeType(models.Model):
    _name = "exercise.range"

    name = fields.Char(string="Name", required=True)

class TempoType(models.Model):
    _name = "exercise.tempo"

    name = fields.Char(string="Name", required=True)

class StanceType(models.Model):
    _name = "exercise.stance"

    name = fields.Char(string="Name", required=True)

class GripType(models.Model):
    _name = "exercise.grip"

    name = fields.Char(string="Name", required=True)