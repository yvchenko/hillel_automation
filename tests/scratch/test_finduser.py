import time

import requests
import json
import pytest


@pytest.mark.api
@pytest.mark.slow
def test_find_user(users, auth, headers):
    """
    Creates a user with a given username
    Comprises the full list of users from the /users endpoint
    Looks for a user with the given username in the resulting dictionary
    Then deletes the user
    Basically a different way to check whether the users are being created
    """
    payload = json.dumps({
        "username": "yvchenko"
    })
    response = requests.request("POST", users, auth=auth, data=payload, headers=headers)
    json_data = json.loads(response.text)
    user_url = json_data["url"]

    result = []

    response = requests.request("GET", users, auth=auth)
    json_data = json.loads(response.text)

    while True:
        next_url = json_data["next"]
        if not next_url:
            break
        next_response = requests.request("GET", next_url, auth=auth)
        json_data = json.loads(next_response.text)
        result += json_data["results"]

    for user in result:
        if user["username"] == "yvchenko":
            print("+++")
        else:
            print(user["username"])


    # assert "yvchenko" in result.values()

    time.sleep(200)
    requests.request("DELETE", user_url, auth=auth)

