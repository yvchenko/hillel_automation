import json
import pytest
import requests

from pytest_bdd import scenarios, given, when, then, parsers
from resources.auth import get_credentials
from resources.schema_validator import assert_schema

scenarios('../bdd_tests/features/api_crud.feature')


@given("I am the admin")
def auth(request):
    request.credentials = get_credentials("data.json")


@given("I have the endpoint")
def users(request):
    request.users = "https://www.aqa.science/users/"


@when(parsers.re("User has name '(?P<username>.*)' and email '(?P<email>.*)'"))
def payload(request, username, email):
    request.payload = json.dumps({
        "username": f"{username}",
        "email": f"{email}"
    })
    request.username = username
    request.email = email


@when(parsers.re("I send a POST request"))
def post(request):
    headers = {'Content-Type': 'application/json'}
    request.response = requests.request("POST", request.users, auth=request.credentials, data=request.payload,
                                        headers=headers)


@then(parsers.re("I should get the '(?P<code>.*)' code"))
def status_code(request, code):
    response = request.response
    code = int(code)

    assert response.status_code == code, f"Test response : {response.text}"


@then(parsers.re("The '(?P<schema>.*)' schema is correct"))
def validate_schema(request, schema):
    response = request.response

    json_data = json.loads(response.text)
    assert_schema(json_data, f"{schema}.json")


@then("I receive the user's URL")
def get_user(request):
    response = request.response
    if response.status_code == 201:
        json_data = json.loads(response.text)

        request.user = json_data["url"]
        pytest.shared = request.user


@given("I have created a user")
def user_url(request):
    request.user = pytest.shared


@when("I send a GET request")
def get(request):
    request.response = requests.request("GET", request.user, auth=request.credentials)


@when("I send a DELETE request")
def delete(request):
    request.response = requests.request("DELETE", request.user, auth=request.credentials)


@when(parsers.re("I send a PUT request"))
def post(request):
    headers = {'Content-Type': 'application/json'}
    request.response = requests.request("PUT", request.user, auth=request.credentials, data=request.payload,
                                        headers=headers)


@when("I create a new group")
def group_add(request):
    groups = "https://www.aqa.science/groups/"
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({
        "name": "test_group"
    })

    response = requests.request("POST", groups, auth=request.credentials, headers=headers, data=payload)

    json_data = json.loads(response.text)
    request.group_url = json_data["url"]


@when("I add the group to the payload")
def group_put(request):
    request.payload = json.dumps({
        "username": f"{request.username}",
        "groups": [request.group_url]
    })


@then("The credentials match the payload")
def cred_check(request):
    response = request.response
    json_data = json.loads(response.text)

    assert json_data["username"] == request.username
    assert json_data["email"] == request.email


@then("The group was added")
def group_check(request):
    response = request.response
    json_data = json.loads(response.text)

    assert json_data["username"] == request.username
    assert json_data["groups"] == [request.group_url]


@then("I delete the group")
def delete_group(request):
    requests.request("DELETE", request.group_url, auth=request.credentials)


@then("The message says Not found")
def not_found(request):
    response = request.response
    json_data = json.loads(response.text)

    assert json_data["detail"] == "Not found."
