import json

@staticmethod
def read_json():
    data = json.load('settings.json', 'r')
    return data

@staticmethod
def write_json(data):
    with open('settings.json', 'w') as f:
        f.write(data)

def check(id:int):
    data = read_json()
    for i in data['setting']:
        if i['user_id'] == id:
            return True 
    for i in data['setting']:
        pass






#class for modifying the settings.json file settings
class setting_data:
    #find the specific user by id and return the option 
    def find(id:int, option:str):
        data = read_json()
        if option == 'all':
            for i in data['setting']:
                if i['user_id'] == id:
                    result = json.dumps(i, indent=2)
        else:
            for i in data['setting']:
                if i['user_id'] == id:
                    result = i[option]
        return result 


    #refresh to the new data 
    def replace(id:int, option:str, content):
        data = read_json()
        for i in data['setting']:
            if i['user_id'] == id:
                i[option] = content
        data = json.dump(data, indent=2)
        write_json(data)
        return 'Done'




#class for modifying the in_session.json file 
class in_session_data:

    def find(id:int):
        pass