import json
import traceback
import sys
import os
import copy


def fetch_user():
    with open('./dal/user.json', mode='r', encoding='utf-8') as feedsjson:
        feeds = json.load(feedsjson)
        return feeds['user_data']


def create_new_board(user_details):
    try:
        with open('./dal/project.json', mode='r', encoding='utf-8') as readfeedsjson:
            feeds = json.load(readfeedsjson)
            latest_id = feeds['latest_id']
            feeds['latest_id'] = feeds['latest_id'] + 1
            name_list = [val['name']
                for val in list(feeds['user_data'][0].values())]
            if user_details['name'] not in name_list:
                feeds['user_data'][0].update({latest_id: user_details})
            else:
                raise Exception('Duplicate User Name')

        with open('./dal/project.json', mode='w', encoding='utf-8') as feedsjson:
            json.dump(feeds, feedsjson)
    except Exception as err_msg:
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname, lineno, fn, text = frame
            print(
                f"Error in create_new_board {text} on line {lineno} with error as {err_msg} ")
        latest_id = -1
    finally:
        return latest_id


def add_task_to_board_by_name(task_details):
    try:
        with open('./dal/project.json', mode='r', encoding='utf-8') as readfeedsjson:
            feeds = json.load(readfeedsjson)
            users_data = feeds['user_data']
            task_details_copy = copy.deepcopy(task_details)
            del task_details_copy['board_id']
            fetched_project_to_update = users_data[0][str(
                task_details['board_id'])]
            if(fetched_project_to_update['status'] == "OPEN"):
                latest_task_id = fetched_project_to_update['latest_task_id']
                tasks_list = [val['title'] for val in list(
                    fetched_project_to_update['tasks'].values())]
                if task_details['title'] not in tasks_list:
                    fetched_project_to_update['latest_task_id'] = latest_task_id + 1
                    fetched_project_to_update['tasks'].update(
                        {latest_task_id: task_details_copy})
                else:
                    raise Exception(
                        f"Duplicate Task Name in board_id {task_details['board_id']}")

                with open('./dal/project.json', mode='w', encoding='utf-8') as feedsjson:
                    json.dump(feeds, feedsjson)
                return latest_task_id
            else:
                raise Exception(
                    f"board_id {task_details['board_id']} has already been closed")

    except Exception as err_msg:
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname, lineno, fn, text = frame
            error = (
                f"Error in finding user {text} on line {lineno} with error as {err_msg} ")
        return error


def update_tasks_status(status_data):
    try:
        with open('./dal/project.json', mode='r', encoding='utf-8') as readfeedsjson:
            feeds = json.load(readfeedsjson)
            users_data = feeds['user_data']
            board = users_data[0][str(status_data['board_id'])]
            task = board['tasks'][status_data['task_id']]
            task['status'] = status_data['status']

        with open('./dal/project.json', mode='w', encoding='utf-8') as feedsjson:
            json.dump(feeds, feedsjson)
        return 'Success'
    except Exception as err_msg:
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname, lineno, fn, text = frame
            error = (
                f"Error in finding user {text} on line {lineno} with error as {err_msg} ")
        return error


def close_board(board_details):
    try:
        with open('./dal/project.json', mode='r', encoding='utf-8') as readfeedsjson:
            feeds = json.load(readfeedsjson)
            users_data = feeds['user_data']
            board = users_data[0][str(board_details['board_id'])]
            print('board==============',board)
            task_status_list = [each_task['status'] for each_task in list(board['tasks'].values())]
            print('task_status_list==========',task_status_list)
            boolean_task_status_list = []
            for each_status in task_status_list:
                if each_status in ["COMPLETE"]:
                    boolean_task_status_list.append(True)
                else:
                    boolean_task_status_list.append(False)
            if len(boolean_task_status_list) == 0:
                return f"No tasks inside board {board_details['board_id']} to update"
            if all(boolean_task_status_list):
                board['status'] = "COMPLETE"
                with open('./dal/project.json', mode='w', encoding='utf-8') as feedsjson:
                    json.dump(feeds, feedsjson)
                return "Updated board to complete"
            else:
                return f"Please update all tasks to status 'COMPLETE' before attempting to change the status of the board {board_details['board_id']}."

    except Exception as err_msg:
        for frame in traceback.extract_tb(sys.exc_info()[2]): 
            fname, lineno, fn, text = frame 
            error = (f"Error in finding user {text} on line {lineno} with error as {err_msg} ")
        return error


def instantiate_files():
    path = os.listdir(os.getcwd() + '/dal')
    if 'project.json' not in path:
        data_to_populate = {
        "user_data": 
                    [ {} ],
        "latest_id": 0
        }
        with open('./dal/project.json', 'w') as feedsjson:
            print("The json file is created")
            json.dump(data_to_populate, feedsjson)
