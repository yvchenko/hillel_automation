import requests

url = "https://aqa.science/users/"

payload={
    "username": "new_user_99998",
    "email": "email@example.com",
    "groups": []
}

headers = {

}

response = requests.request("POST", url, headers=headers, data=payload, auth=("admin","admin123"))

print(response.text)
