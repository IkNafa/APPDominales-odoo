from odoo import http
from odoo.http import request

class TrainingController(http.Controller):

    @http.route(route="/api/users/<int:user_id>/trainings", type="json", auth="user", methods=['POST'])
    def getUserTrainingList(self, user_id=None):
        if user_id:
            training_ids = request.env['training.training'].search(['|',('owner_id','=',user_id),('client_id','=',user_id)])
            training_list = []
            for training_id in training_ids:
                training = {
                    'id': training_id.id,
                    'name': training_id.name,
                    'trainer':{
                        'id': training_id.owner_id.id,
                        'name': training_id.owner_id.name,
                        'email': training_id.owner_id.login,
                    }
                }

                if training_id.client_id:
                    training['client'] = {
                        'id': training_id.client_id.id,
                        'name': training_id.client_id.name,
                        'email': training_id.client_id.login,
                    }
                
                training_list.append(training)
            
            return training_list
    
    @http.route(route="/api/trainings/<int:training_id>", type="json", auth="user", methods=['POST'])
    def getUserTrainingRoutinesData(self, training_id):
        if not training_id:
            return
        
        training = request.env['training.training'].search([('id','=',training_id)], limit=1)
        if not training.routine_ids:
            return
        
        routines_data = []
        for index in range(0,7):
            routine = request.env['routine.routine'].search([('training_id','=',training_id),('dayofweek_ids.index','=',index)],limit=1)
            if routine:
                routine_data = {
                    'name':routine.name,
                    'id': routine.id,
                    'day': index,
                    'exercise_count': len(routine.routine_exercise_ids)
                }

                exercises_data = []
                for exercise_id in routine.routine_exercise_ids:

                    sets_data = []
                    for set_id in exercise_id.set_ids:
                        sets_data.append({
                            'reps': set_id.reps,
                            'weight': set_id.weight,
                            'rpe': set_id.rpe,
                        })
                    
                    exercises_data.append({
                        'name':exercise_id.name,
                        'description': exercise_id.description or "",
                        'external_video': exercise_id.external_video or "",
                        'group': exercise_id.group_id.name or "",
                        'image': exercise_id.image_small or "",
                        'bartype': exercise_id.bartype_id.name or "",
                        'range': exercise_id.range_id.name or "",
                        'tempo': exercise_id.tempo_id.name or "",
                        'stance': exercise_id.stance_id.name or "",
                        'grip': exercise_id.grip_id.name or "",
                        'sets': sets_data,
                    })

                    

                routine_data['exercises'] = exercises_data



                routines_data.append(routine_data)
        
        return routines_data

     