import json


with open('../tests/response.json', 'r') as file:
    data = json.load(file)

for item in data:
    # print(item['username'])
    # print(item.keys())
    value = item.get('user_name', None)
    # if value:
    print(value) if value else print('not found')