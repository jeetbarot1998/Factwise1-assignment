from flask_restx import Resource
from pytz import timezone
from models.users_model import api, create_user, list_user, get_user_by_id, update_user_by_id_model
import datetime
from dal.user_query import create_new_user, fetch_user, fetch_user_by_id, update_user_by_id, instantiate_files


@api.route('/create_user')
class CreateUser(Resource):
    @api.expect(create_user)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        user_details = {
            "name" : api.payload['name'],
            "display_name" : api.payload['display_name'],
            "creation_time" : str(datetime.datetime.now(timezone("UTC")).strftime("%Y-%m-%d %H:%M:%S"))
        }
        res = create_new_user(user_details)
        if res != -1:
            return res
        else:
            return 'Duplicate User Name'


@api.route('/list_users')
class ListUsers(Resource):
    @api.expect(get_user_by_id)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    @api.marshal_with(list_user)
    def get(self):
        response = list(fetch_user()[0].values())
        return response


@api.route('/describe_user')
class DescribeUsers(Resource):
    @api.expect(get_user_by_id)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    @api.marshal_with(list_user)
    def post(self):
        response = fetch_user_by_id(api.payload['id'])
        return response


@api.route('/update_user')
class UpdateUser(Resource):
    @api.expect(update_user_by_id_model)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def patch(self):
        response = update_user_by_id(api.payload)
        return response


@api.route('/instantiate_files')
class IinstantiateFiles(Resource):
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        instantiate_files()
        return 1