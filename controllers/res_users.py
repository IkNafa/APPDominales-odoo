from odoo import http
from odoo.http import request
import base64
from odoo import fields
from pytz import utc
from pytz import timezone

class UserController(http.Controller):

    def getImageUrl(self, partner_id):
        url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        attachment_id = request.env['ir.attachment'].search([('res_model','=','res.partner'),('res_id','=',partner_id),('res_field','=','image_small')],limit=1).id
        return "%s/web/image/ir.attachment/%s/datas" % (url, str(attachment_id))


    def getUserData(self, user):
        user_data = {
            'id':user.id,
            'name':user.name,
            'email':user.login,
            'is_trainer':user.is_trainer,
            'provider': user.provider_id.name,
            'gender': user.gender or "",
            'birthday': user.birthday or "",
            'phone':user.phone or "",
            'function': user.function or ""
        }

        if user.image_small:
            user_data['image'] = self.getImageUrl(user.partner_id.id)

        last_measure = request.env['user.measures'].search([('user_id','=',user.id)],order="date desc",limit=1)
        if last_measure:
                user_data['current_measure'] = {
                'weight': last_measure.weight,
                'height': last_measure.height,
                'date': last_measure.date.strftime("%d %b."),
                'id': last_measure.id,
            }
        
        if user.trainer_id:
            user_data['trainer'] = {
                'id':user.trainer_id.id,
                'name':user.trainer_id.name,
                'email': user.trainer_id.login,
                'client_count':user.trainer_id.client_count,
                'rating_mean':user.trainer_id.rating_mean,
            }
        
        if user.goal_ids:
            goals = []
            for goal in user.goal_ids:
                goals.append({
                    'name': goal.name,
                    'description': goal.description,
                })
            
            user_data['goals'] = goals

        if user.category_id:
            tags = []
            for tag in user.category_id:
                tags.append({
                    'name': tag.name,
                })
            user_data['tags'] = tags
        
        if user.client_ids:
            clients = []
            for client_id in user.client_ids:

                clients.append({
                    'id': client_id.id,
                    'name': client_id.name,
                    'image': self.getImageUrl(client_id.partner_id.id) if client_id.image_small else "",
                    'email': client_id.login,
                })
            user_data['clients'] = clients

        return user_data


    @http.route(route="/api/users/<int:user_id>", type="json", auth="user", methods=['POST'])
    def getUserDataRoute(self, user_id=None):
        if user_id:
            user = request.env['res.users'].search([('is_appdominales_user','=',True),('id','=',user_id)], limit=1)
            if user:
                return self.getUserData(user)

        else:
            return {
                'message':"Nada"
            }

    @http.route(route="/api/users", type="json", auth="none", methods=['POST'])
    def getUserList(self, **kw):
        user_ids = request.env['res.users'].search([('is_appdominales_user','=',True)])
        users_data = []
        for user_id in user_ids:
            users_data.append({
                'id': user_id.id,
                'name': user_id.name,
                'email': user_id.login,
                'image_small':user_id.image_small,
            })
        return users_data
    
    @http.route(route="/api/users/me", type="json", auth="user", methods=['POST'])
    def getCurrentUserData(self):
        return self.getUserDataRoute(request.session.uid)
        
    @http.route(route="/api/users/register", type="json", auth="none", methods=['POST'])
    def createNewUser(self, **kw):
        user = request.env['res.users'].sudo().create(kw)
        if user:
            return {
                'Result':'OK',
                'id': user.id
            }
    
    @http.route(route="/api/chat/get", type="json", auth="user", methods=['POST'])
    def getUserChatMessages(self, user_id):
        message_ids = request.env['app.chat.message'].search(['|','&','|',('chat_id.user1_id','=',request.session.uid),('chat_id.user2_id','=',request.session.uid),('chat_id.user2_id','=',user_id),('chat_id.user1_id','=',user_id)], order="datetime asc")
        messages_data = []
        for message_id in message_ids:
            user_pytz = timezone('Europe/Madrid')
            datetime = utc.localize(message_id.datetime).astimezone(user_pytz)
            messages_data.append({
                'datetime': datetime,
                'text': message_id.text,
                'user': {
                    'id': message_id.user_id.id,
                    'name': message_id.user_id.name,
                    'email': message_id.user_id.login
                }
            })
        
        return messages_data
    
    @http.route(route="/api/chat/send", type="json", auth="user", methods=['POST'])
    def sendChatMessage(self, user_id, text):
        chat_id = request.env['app.chat'].search(['|','&','|',('user1_id','=',request.session.uid),('user2_id','=',request.session.uid),('user2_id','=',user_id),('user1_id','=',user_id)],limit=1)
        if not chat_id:
            chat_id = request.env['app.chat'].create({
                'user1_id': request.session.uid,
                'user2_id': user_id,
            })
        
        chat_id.write({
            'chat_message_ids': [(0,0,{
                'user_id': request.session.uid,
                'text': text,
                'datetime': fields.Datetime.now()})]
        })

        return "OK"