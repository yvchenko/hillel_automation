import requests
import json
import pytest
from schema_validator import assert_schema


@pytest.mark.api
def test_create_user(users, auth, headers):
    """
    Creates a new user with set name and email
    Checks that the response code and schema are correct
    Parses the json response and saves the user's url for further tests
    """
    payload = json.dumps({
        "username": "yvchenko",
        "email": "yvchenko@test.com"
    })
    response = requests.request("POST", users, auth=auth, data=payload, headers=headers)
    json_data = json.loads(response.text)

    assert response.status_code == 201, f"Test response : {response.text}"
    assert_schema(json_data, "user.json")

    user_url = json_data["url"]
    pytest.shared = user_url


@pytest.mark.api
def test_get_user(users, auth):
    """
    Sends a GET request to the url of the user that was created in the first test
    Checks that the response code and schema are correct
    Checks that the user's information is the same that was specified in the POST request
    """
    user_url = pytest.shared

    response = requests.request("GET", user_url, auth=auth)
    json_data = json.loads(response.text)

    assert response.status_code == 200, f"Test response : {response.text}"
    assert_schema(json_data, "user.json")

    assert json_data["username"] == "yvchenko"
    assert json_data["email"] == "yvchenko@test.com"


@pytest.mark.api
def test_change_user_email(users, auth, headers):
    """
    Changes the email of the user that was created in the first test
    Checks that the response code and schema are correct
    Checks that the user's email was changed
    """
    user_url = pytest.shared

    payload = json.dumps({
        "username": "yvchenko",
        "email": "new_email@example.com"
    })

    response = requests.request("PUT", user_url, auth=auth, headers=headers, data=payload)
    json_data = json.loads(response.text)

    assert response.status_code == 200, f"Test response : {response.text}"
    assert_schema(json_data, "user.json")

    assert json_data["username"] == "yvchenko"
    assert json_data["email"] == "new_email@example.com"


@pytest.mark.api
def test_change_user_group(users, groups, auth, headers):
    """
    Creates a new group
    Adds the user from the first test to the group
    Checks that the response code and schema are correct
    Checks that the user's list of groups has changes
    Deletes the group
    """
    payload = json.dumps({
        "name": "test_group"
    })

    response = requests.request("POST", groups, auth=auth, headers=headers, data=payload)
    json_data = json.loads(response.text)
    group_url = json_data["url"]

    user_url = pytest.shared

    payload = json.dumps({
        "username": "yvchenko",
        "groups": [group_url]
    })

    response = requests.request("PUT", user_url, auth=auth, headers=headers, data=payload)
    json_data = json.loads(response.text)

    assert response.status_code == 200, f"Test response : {response.text}"
    assert_schema(json_data, "user.json")

    assert json_data["username"] == "yvchenko"
    assert json_data["groups"] == [group_url]

    requests.request("DELETE", group_url, auth=auth)


@pytest.mark.api
def test_delete_user(users, auth):
    """
    Deletes the user that was created
    Checks that the response code is correct and the answer is empty
    """
    user_url = pytest.shared

    response = requests.request("DELETE", user_url, auth=auth)
    assert response.status_code == 204, f"Test response : {response.text}"
    assert not response.text
