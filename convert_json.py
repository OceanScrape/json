import json
import os

data_list = []
data_dict = {
     "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
 }
data_list.append(data_dict)
try:
    os.mkdir('json_files')
except FileExistsError:
    pass

with open('json_files/data.json', 'w+') as json_data:
    json.dump(data_list, json_data)
print('Json file has been created')

