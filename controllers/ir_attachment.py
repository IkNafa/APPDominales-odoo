from odoo import http
from odoo.http import request

class FilesController(http.Controller):

    @http.route(route="/api/content/<int:attachment_id>", type="http", auth="none", methods=['GET'])
    def getFile(self, attachment_id):
        if attachment_id:
            attachment = request.env['ir.attachment'].sudo().search([('id','=',attachment_id)], limit=1)
            if attachment:
                return attachment.datas
