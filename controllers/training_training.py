from odoo import http
from odoo.http import request

class TrainingController(http.Controller):

     @http.route(route="/api/users/<int:user_id>/trainings", type="json", auth="user", methods=['GET'])
     def getUserTrainingList(self, user_id=None):
         if user_id:
            training_ids = request.env['training.training'].search(['|',('owner_id','=',user_id),('client_id','=',user_id)])
            training_list = []
            for training_id in training_ids:
                training = {
                    'name': training_id.name,
                    'trainer':{
                        'id': training_id.owner_id.id,
                        'name': training_id.owner_id.name,
                    }
                }

                if training_id.client_id:
                    training['client'] = {
                        'id': training_id.client_id.id,
                        'name': training_id.client_id.name,
                    }
                
                training_list.append(training)
            
            return training_list
     