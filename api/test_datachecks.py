import requests
import json
import pytest
from schema_validator import assert_schema


@pytest.mark.api
def test_read_users(users, auth):
    """Sends a GET request to the /users endpoint
    Checks that the response code and schema are correct
    """
    response = requests.request("GET", users, auth=auth)
    json_data = json.loads(response.text)

    assert response.status_code == 200, f"Test response : {response.text}"
    assert_schema(json_data, "users.json")


@pytest.mark.api
def test_read_groups(groups, auth):
    """Sends a GET request to the /groups endpoint
    Checks that the response code and schema are correct
    """
    response = requests.request("GET", groups, auth=auth)
    json_data = json.loads(response.text)

    assert response.status_code == 200, f"Test response : {response.text}"
    assert_schema(json_data, "groups.json")
