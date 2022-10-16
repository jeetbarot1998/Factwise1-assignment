import json
import traceback
import sys
import os

def fetch_user():
    with open('./dal/user.json', mode='r', encoding='utf-8') as feedsjson:
        feeds = json.load(feedsjson)
        return feeds['user_data']

def create_new_user(user_details):
    try:
        with open('./dal/user.json', mode='r', encoding='utf-8') as readfeedsjson:
            feeds = json.load(readfeedsjson)
            latest_id = feeds['latest_id']
            feeds['latest_id'] = feeds['latest_id'] + 1
            name_list = [val['name'] for val in list(feeds['user_data'][0].values())]
            if user_details['name'] not in name_list:
                feeds['user_data'][0].update({ latest_id : user_details})
            else: 
                raise Exception('Duplicate User Name')
                
        with open('./dal/user.json', mode='w', encoding='utf-8') as feedsjson:
            json.dump(feeds, feedsjson)
    except Exception as err_msg:
        for frame in traceback.extract_tb(sys.exc_info()[2]): 
            fname, lineno, fn, text = frame 
            print(f"Error in create_new_user {text} on line {lineno} with error as {err_msg} ")
        latest_id = -1
    finally:
        return latest_id
    

def fetch_user_by_id(id_to_search):
    try:
        with open('./dal/user.json', mode='r', encoding='utf-8') as feedsjson:
            feeds = json.load(feedsjson)
            users_data = feeds['user_data']
            filtered_data = users_data[0][str(id_to_search)]
    except Exception as err_msg:
        for frame in traceback.extract_tb(sys.exc_info()[2]): 
            fname, lineno, fn, text = frame 
            print(f"Error in finding user {text} on line {lineno} with error as {err_msg} ")
        filtered_data = 'No Such Entry Found'
    finally:
        return filtered_data

def update_user_by_id(user_details):
    try:
        with open('./dal/user.json', mode='r', encoding='utf-8') as readfeedsjson:
            feeds = json.load(readfeedsjson)
            users_data = feeds['user_data']
            # users_data[0][str(user_details['id'])]['name'] = user_details['user']['name']
            users_data[0][str(user_details['id'])]['display_name'] = user_details['user']['display_name']

        with open('./dal/user.json', mode='w', encoding='utf-8') as feedsjson:
            json.dump(feeds, feedsjson)
        status = 'Succefully Updated'
    except Exception as err_msg:
        for frame in traceback.extract_tb(sys.exc_info()[2]): 
            fname, lineno, fn, text = frame 
            print(f"Error in finding user {text} on line {lineno} with error as {err_msg} ")
        status = 'No Such Entry exists'
    finally:
        return status


def instantiate_files():
    path = os.listdir(os.getcwd() + '/dal')
    if 'user.json' not in path:
        data_to_populate = {
        "user_data": 
                    [ {} ],
        "latest_id": 0
        }
        with open('./dal/user.json', 'w') as feedsjson:
            print("The json file is created")
            json.dump(data_to_populate, feedsjson)

