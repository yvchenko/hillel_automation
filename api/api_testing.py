import json

import requests

url = 'https://www.aqa.science/'
result = []

response = requests.get(url).json()

received_url = response['users']

response_new = requests.get(received_url, auth=("admin", "admin123")).json()



while True:
    next_url = response_new["next"]
    if not next_url:
        break
    response_new = requests.get(next_url, auth=("admin", "admin123")).json()
    result += response_new["results"]

with open('response.json', 'w') as r:
    json.dump(result, r)

