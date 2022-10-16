from flask_restx import Namespace, reqparse, fields, inputs

api = Namespace('TeamsModule', description='Teams Data Model')

create_team = api.model(
    'create_team', {
          "name" : fields.String(attribute='name'),
          "description" : fields.String(attribute='description'),
          "admin": fields.String(attribute='admin'),
    }
)

list_teams = api.model(
    'list_teams',{
            "name" : fields.String(attribute='name'),
            "description" : fields.String(attribute='description'),
            'creation_time': fields.String(attribute='creation_time'),
            "admin": fields.String(attribute='admin')
        }
)

get_team_by_id = api.model(
    'get_team_by_id',{
        'id': fields.Integer(attribute='id')
    }
)

update_team_by_id_model = api.model(
    'update_team_by_id_model',{
          "id" :  fields.Integer(attribute='id'),
          "team" : fields.Nested(create_team)
    }
)

users_to_team_model = api.model(
    'users_to_team_model',{
          "id" :  fields.Integer(attribute='id'),
          "users" : fields.List(fields.String)
    }
)