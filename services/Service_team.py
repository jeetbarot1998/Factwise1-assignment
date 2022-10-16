from flask_restx import Resource
from pytz import timezone
from models.teams_model import api, create_team, list_teams, get_team_by_id, update_team_by_id_model, users_to_team_model
import datetime
from dal.teams_query import create_new_teams, fetch_user, describe_team_by_id, update_team_by_id, instantiate_files , add_user_to_team, remove_users_from_team, list_team_users_by_team_id


@api.route('/create_team')
class CreateTeam(Resource):
    @api.expect(create_team)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        user_details = {
            "name" : api.payload['name'],
            "description" : api.payload['description'],
            "admin" : api.payload['admin'],
            "creation_time" : str(datetime.datetime.now(timezone("UTC")).strftime("%Y-%m-%d %H:%M:%S"))
        }
        res = create_new_teams(user_details)
        if res['latest_id'] == -1:
            return res['status']
        else:
            return res['latest_id']


@api.route('/list_teams')
class ListTeam(Resource):
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    @api.marshal_with(list_teams)
    def get(self):
        response = list(fetch_user()[0].values())
        return response


@api.route('/describe_team')
class DescribeTeam(Resource):
    @api.expect(get_team_by_id)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    @api.marshal_with(list_teams)
    def post(self):
        response = describe_team_by_id(api.payload['id'])
        return response


@api.route('/update_team')
class UpdateTeam(Resource):
    @api.expect(update_team_by_id_model)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def patch(self):
        response = update_team_by_id(api.payload)
        return response

@api.route('/add_users_to_team')
class AddUsersToTeam(Resource):
    @api.expect(users_to_team_model)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        response = add_user_to_team(api.payload)
        return response


@api.route('/remove_users_from_team')
class RemoveUsersToTeam(Resource):
    @api.expect(users_to_team_model)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        response = remove_users_from_team(api.payload)
        return response


@api.route('/list_team_users')
class ListTeamUsers(Resource):
    @api.expect(get_team_by_id)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        response = list_team_users_by_team_id(api.payload)
        return response



@api.route('/instantiate_files')
class IinstantiateFiles(Resource):
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        instantiate_files()
        return 1