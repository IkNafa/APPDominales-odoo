from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
import requests
import json

class Chat(models.Model):
    _name = 'app.chat'

    user1_id = fields.Many2one('res.users', string="Usuario", required=True, ondelete="cascade")
    user2_id = fields.Many2one('res.users', string="Usuario", required=True, ondelete="cascade")

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

    user_id = fields.Many2one('res.users', required=True, default=_get_default_user_id, ondelete="cascade")
    text = fields.Text(string="Mensaje", required=True)
    datetime = fields.Datetime(string="Fecha", required=True, default=fields.Datetime.now())

    @api.model
    def create(self, vals):
        message_id = super(Message, self).create(vals)

        receiver_id = message_id.chat_id.user1_id if message_id.chat_id.user1_id.id != message_id.user_id.id else message_id.chat_id.user2_id

        self._send_request(message_id.user_id, receiver_id,message_id.text)

        return message_id
    
    def _send_request(self,user_id,receiver_id, message_text):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "key=AAAA_V01gvk:APA91bGF5WOG7xRkEmD885iGsUnmX0R4i16xeSUV1t92y9ppiDrJaPFOGAAfD9vdKIeAAv_UPfF19NQy8lml0ZP_YjA82qsNFqzAAyiaNy1Z1lSh08f_YBAvaTskxqRjrgu5Dyt0W7HB"
        }

        body = {
            "registration_ids":[receiver_id.firebase_token],
            "notification": {
                "body": "%s" % (message_text),
                "title": user_id.name
            }
        }

        uri = "https://fcm.googleapis.com/fcm/send"

        requests.post(uri, headers=headers, data=json.dumps(body))

