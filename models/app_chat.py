from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class Chat(models.Model):
    _name = 'app.chat'

    user1_id = fields.Many2one('res.users', string="Usuario", required=True)
    user2_id = fields.Many2one('res.users', string="Usuario", required=True)

    chat_message_ids = fields.One2many('app.chat.message','chat_id', string="Messages")

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "%s - %s" % (record.user1_id.name, record.user2_id.name)))
        return result

    @api.model
    def create(self, vals):
        chat_users = [vals.get('user1_id'),vals.get('user2_id')]
        if chat_users[0] == chat_users[1]:
            raise ValidationError("Los usuarios no pueden ser el mismo")

        for chat_id in self.env['app.chat'].search([]):
            if chat_id.user1_id.id in chat_users and chat_id.user2_id.id in chat_users:
                raise ValidationError("Este chat ya existe")

        return super(Chat, self).create(vals)

class Message(models.Model):
    _name = "app.chat.message"

    def _get_default_user_id(self):
        return self.env.user.id

    chat_id = fields.Many2one('app.chat', required=True, ondelete="cascade")

    user_id = fields.Many2one('res.users', required=True, default=_get_default_user_id)
    text = fields.Text(string="Mensaje", required=True)
    datetime = fields.Datetime(string="Fecha", required=True, default=fields.Datetime.now())

