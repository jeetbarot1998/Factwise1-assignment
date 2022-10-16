import json
import traceback
import sys
import os

def fetch_user():
    with open('./dal/teams.json', mode='r', encoding='utf-8') as feedsjson:
        feeds = json.load(feedsjson)
        return feeds['user_data']

def create_new_teams(user_details):
    try:
        with open('./dal/teams.json', mode='r', encoding='utf-8') as readfeedsjson:
            feeds = json.load(readfeedsjson)
            latest_id = feeds['latest_id']
            feeds['latest_id'] = feeds['latest_id'] + 1
            name_list = [val['name'] for val in list(feeds['user_data'][0].values())]
            if user_details['name'] not in name_list:
                user_details['users'] = []
                feeds['user_data'][0].update({ latest_id : user_details})
                with open('./dal/teams.json', mode='w', encoding='utf-8') as feedsjson:
                    json.dump(feeds, feedsjson)
                return { "status": "Success", "latest_id" : latest_id}
            else: 
                raise Exception('Duplicate User Name')
        
    except Exception as err_msg:
        for frame in traceback.extract_tb(sys.exc_info()[2]): 
            fname, lineno, fn, text = frame 
            error = (f"Error in create_new_teams {text} on line {lineno} with error as {err_msg} ")
            print(error)
        return { "status": error, "latest_id" : -1 }
    

def describe_team_by_id(id_to_search):
    try:
        with open('./dal/teams.json', mode='r', encoding='utf-8') as feedsjson:
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

def update_team_by_id(user_details):
    try:
        with open('./dal/teams.json', mode='r', encoding='utf-8') as readfeedsjson:
            feeds = json.load(readfeedsjson)
            users_data = feeds['user_data']
            # users_data[0][str(user_details['id'])]['name'] = user_details['user']['name']
            users_data[0][str(user_details['id'])]['description'] = user_details['team']['description']
            users_data[0][str(user_details['id'])]['admin'] = user_details['team']['admin']


        with open('./dal/teams.json', mode='w', encoding='utf-8') as feedsjson:
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
    if 'teams.json' not in path:
        data_to_populate = {
        "user_data": 
                    [ {} ],
        "latest_id": 0
        }
        with open('./dal/teams.json', 'w') as feedsjson:
            print("The json file is created")
            json.dump(data_to_populate, feedsjson)

def add_user_to_team(user_team_details):
    try:
        with open('./dal/teams.json', mode='r', encoding='utf-8') as readfeedsjson:
            feeds = json.load(readfeedsjson)
            users_data = feeds['user_data']
            users_data[0][str(user_team_details['id'])]['users'] = list(set(user_team_details['users']))

        with open('./dal/teams.json', mode='w', encoding='utf-8') as feedsjson:
            json.dump(feeds, feedsjson)
        status = 'Succefully Updated'
    except Exception as err_msg:
        for frame in traceback.extract_tb(sys.exc_info()[2]): 
            fname, lineno, fn, text = frame 
            print(f"Error in finding user {text} on line {lineno} with error as {err_msg} ")
        status = 'No Such Entry exists'
    finally:
        return status

def remove_users_from_team(user_team_details):
    try:
        with open('./dal/teams.json', mode='r', encoding='utf-8') as readfeedsjson:
            feeds = json.load(readfeedsjson)
            users_data = feeds['user_data']
            existing_users = users_data[0][str(user_team_details['id'])]['users']
            users_to_remove =  user_team_details['users']
            final_list = list(set(existing_users) - set(users_to_remove))
            users_data[0][str(user_team_details['id'])]['users'] = final_list

        with open('./dal/teams.json', mode='w', encoding='utf-8') as feedsjson:
            json.dump(feeds, feedsjson)
        status = 'Succefully Updated'
    except Exception as err_msg:
        for frame in traceback.extract_tb(sys.exc_info()[2]): 
            fname, lineno, fn, text = frame 
            print(f"Error in finding user {text} on line {lineno} with error as {err_msg} ")
        status = 'No Such Entry exists'
    finally:
        return status

def list_team_users_by_team_id(team_id):
    try:
        final_user_list = []
        with open('./dal/teams.json', mode='r', encoding='utf-8') as readteamsfeedsjson:
            feeds = json.load(readteamsfeedsjson)
            users_data = feeds['user_data']
            users_list =  users_data[0][str(team_id['id'])]['users']

        with open('./dal/user.json', mode='r', encoding='utf-8') as readusersfeedsjson:
            feeds = json.load(readusersfeedsjson)
            users_data = feeds['user_data']
            filtered_user_data = list(users_data[0].values())
        for each_user in filtered_user_data:
           if each_user['name'] in users_list:
               final_user_list.append(each_user)
        return final_user_list
        
    except Exception as err_msg:
        for frame in traceback.extract_tb(sys.exc_info()[2]): 
            fname, lineno, fn, text = frame 
            print(f"Error in finding user {text} on line {lineno} with error as {err_msg} ")
        status = 'No Such Entry exists'
        return status
