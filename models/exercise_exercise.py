from odoo import _, api, fields, models

class Exercise(models.Model):
    _name = 'exercise.exercise'

    name = fields.Char(string="Name", required=True, translate=True)
    description = fields.Text(string="Description")
    external_video = fields.Char(string="URL")

    group_id = fields.Many2one('exercise.group', string="Group")

    image = fields.Binary(string="Image", attachment=True)
    image_medium = fields.Binary(string="Image medium", attachment=True)
    image_small = fields.Binary(string="Image small", attachment=True)

    @api.model
    def create(self, vals):
        if vals.get("image"):
            tools.image_resize_images(vals, sizes={'image': (1024, None)})
        
        return super(Exercise, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get("image"):
            tools.image_resize_images(vals, sizes={'image': (1024, None)}) 

        return super(Exercise, self).write(vals)

class ExerciseGroup(models.Model):
    _name = "exercise.group"

    name = fields.Char(string="Name", required=True)