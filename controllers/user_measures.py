from odoo import http
from odoo.http import request

class UserMeasuresController(http.Controller):

    @http.route(route="/api/users/measures", type="json", auth="public", methods=['GET'])
    def getUserMeasureData(self, user_id=None):
        return {
            "Message":"hola",
        }