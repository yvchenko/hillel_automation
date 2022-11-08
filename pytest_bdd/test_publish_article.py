from pytest_bdd import scenario, given, when, then
import requests

@scenario('publish_article.feature', 'Publishing the article')
def test_publish():
    pass


@given("I'm an user")
def user(request):
    request.user = {"user_name": "admin", "password": "password"}
    return user


@given("I have Endpoint")
def endpoint(request):
    request.endpoint = "https://www.aqa.science/admin/login/"


@when("I go to endpoint page")
def func(request):
    requests.get(request.endpoint, auth=(''))


@when("I press the submit button")
def func():
    pass


@then("I should see the error message")
def func():
    pass
