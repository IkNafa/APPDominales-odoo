from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Session

class AppdominalesSession(Session):

     @http.route('/api/session/authenticate', type='json', auth="none")
     def apiAuthenticate(self, db, login, password, token=None,base_location=None):
        user_data = super(AppdominalesSession, self).authenticate(db, login, password, base_location)

        if token:
            user_id = user_data.get("uid")
            request.env['res.users'].search([('id','=',user_id)], limit=1).sudo().write({'firebase_token':token})

        return user_data