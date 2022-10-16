from flask_restx import Namespace, reqparse, fields, inputs

api = Namespace('UserModel', description='User Data Model')

create_user = api.model(
    'create_user', {
        'name' : fields.String(attribute='name'),
        'display_name' : fields.String(attribute='display_name'),
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
          "user" : fields.Nested(create_user)
    }
)
