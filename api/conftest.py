import pytest
from auth import get_credentials


def shared_plugin():
    return 'shared'


@pytest.fixture()
def users():
    path = f"https://www.aqa.science/users/"
    return path


@pytest.fixture()
def groups():
    path = f"https://www.aqa.science/groups/"
    return path


@pytest.fixture()
def auth():
    credentials = get_credentials("data.json")
    return credentials


@pytest.fixture()
def headers():
    headers = {'Content-Type': 'application/json'}
    return headers
