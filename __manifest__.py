{
    'name': 'APPDominales',
    'version': '1.0',
    'description': '',
    'summary': '',
    'author': 'APPDominales S.L',
    'website': '',
    'license': 'LGPL-3',
    'category': 'Fitness',
    'depends': [
        'base'
    ],
    'data': [
        'data/routine_dayofweek.xml',
        'data/user_rol.xml',
        'data/exercise_bar.xml',
        'data/exercise_grip.xml',
        'data/exercise_group.xml',
        'data/exercise_range.xml',
        'data/exercise_stance.xml',
        'data/exercise_tempo.xml',

        'security/ir.model.access.csv',

        'views/menus.xml',
        'views/exercise_exercise_views.xml',
        'views/routine_exercise_views.xml',
        'views/routine_routine_views.xml',
        'views/trainer_survey_question_views.xml',
        'views/trainer_survey_views.xml',
        'views/user_measures_views.xml',
        'views/user_rol_views.xml',
        'views/user_user_views.xml',
        'views/training_training_views.xml',
        
    ],
    'application': True,
}