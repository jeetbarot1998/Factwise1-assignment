from flask_restx import Namespace, reqparse, fields, inputs

api = Namespace('ProjectModule', description='Project Data Model')

create_board = api.model(
    'create_board', {
        'name' : fields.String(attribute='name'),
        'description' : fields.String(attribute='description'),
        'team_id' : fields.String(attribute='description')
    }
)

add_task_toboard_by_id = api.model(
    'add_task_toboard_by_id', {
        "board_id" : fields.String(attribute='name'),
        "title" : fields.String(attribute='title'),
        "description" : fields.String(attribute='description'),
        "user_id" : fields.String(attribute='user_id'),
    }
)

update_task_status_by_id = api.model(
    'update_task_status_by_id', {
        "board_id" : fields.String(attribute='name'),
        "task_id" : fields.String(attribute='task_id'),
        "status" : fields.String(attribute='status')
    }
)

close_board_by_id = api.model(
    'close_board_by_id', {
        "board_id" : fields.String(attribute='name')
    }
)

list_user = api.model(
    'list_user',{
        'Name': fields.String(attribute='name'),
        'DisplayName': fields.String(attribute='display_name'),
        'CreationTime': fields.String(attribute='creation_time')
    }
)

get_user_by_id = api.model(
    'get_user_by_id',{
        'id': fields.Integer(attribute='id')
    }
)

update_user_by_id_model = api.model(
    'update_user_by_id_model',{
          "id" :  fields.Integer(attribute='id'),
          "user" : fields.Nested(create_board)
    }
)
