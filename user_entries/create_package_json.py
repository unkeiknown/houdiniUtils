import json
import sys
import os

with open("user_data.json","r") as file:
    user_data = json.load(file)

import os

try:
    user_machine = os.getlogin()
except OSError:
    user_machine = os.environ.get('USER') or os.environ.get('USERNAME') or os.environ.get('LOGNAME')

json_dict = {}
print(user_machine)
with open("packages/company_vars.json","w") as env_file:
    for user in user_data:
        if user_machine in user_data[user].values():
            print("User found, setting env variables")
            print(user_data[user])
            json_dict["env"] = [{"USER_ID":str(user_data[user]["id"])}]
            json.dump(json_dict, env_file, indent = 4)









