from flask_restx import Resource
from pytz import timezone
from models.project_model import api, create_board, add_task_toboard_by_id, update_task_status_by_id, board_by_id_modal
import datetime
from dal.project_query import create_new_board, instantiate_files, add_task_to_board_by_name, update_tasks_status, get_all_active_boards_by_id, close_board

@api.route('/create_board')
class CreateUser(Resource):
    @api.expect(create_board)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        if len(api.payload['name']) > 64:
            return "board name can be max 64 characters", 400
        if len(api.payload['description']) > 128:
            return "description can be max 128 characters", 400
        user_details = {
            "name" : api.payload['name'],
            "description" : api.payload['description'],
            "team_id" : api.payload['team_id'],
            "creation_time" : str(datetime.datetime.now(timezone("UTC")).strftime("%Y-%m-%d %H:%M:%S")),
            "tasks" : {},
            "latest_task_id": 0,
            "status" : "OPEN"
        }
        res = create_new_board(user_details)
        if res != -1:
            return res
        else:
            return 'Duplicate Project Name'


@api.route('/add_task')
class AddTasks(Resource):
    @api.expect(add_task_toboard_by_id)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        if len(api.payload['title']) > 64:
            return "board name can be max 64 characters", 400
        if len(api.payload['description']) > 128:
            return "description can be max 128 characters", 400
        project_details = {
            "board_id" : api.payload['board_id'],
            "title" : api.payload['title'],
            "description" : api.payload['description'],
            "creation_time" : str(datetime.datetime.now(timezone("UTC")).strftime("%Y-%m-%d %H:%M:%S")),
            "status" : "OPEN"
        }
        res = add_task_to_board_by_name(project_details)
        return res


@api.route('/update_task_status')
class UpdateTaskStaus(Resource):
    @api.expect(update_task_status_by_id)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        if api.payload['status'] not in ["OPEN", "IN_PROGRESS" , "COMPLETE"]:
            return 'Invalid Status Option', 400
        res = update_tasks_status(api.payload)
        return res


@api.route('/close_board')
class CloseBoard(Resource):
    @api.expect(board_by_id_modal)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        res = close_board(api.payload)
        return res


@api.route('/list_boards')
class ListBoard(Resource):
    @api.expect(board_by_id_modal)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        res = get_all_active_boards_by_id(api.payload)
        return res


@api.route('/instantiate_files')
class IinstantiateFiles(Resource):
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        instantiate_files()
        return 1