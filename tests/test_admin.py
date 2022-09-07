import pytest
import requests

url = "https://www.aqa.science/admin/"


@pytest.mark.admin
def test_admin_get():
    """
    Check if a GET request gets a 200 response
    """
    response = requests.get(url)
    assert response.status_code == 200, f"Test response : {response.text}"


@pytest.mark.admin
def test_admin_head():
    """
    Check if a HEAD request gets a 302 response
    """
    response = requests.head(url)
    assert response.status_code == 302, f"Test response : {response.text}"


@pytest.mark.admin
def test_admin_options():
    """
    Check if an OPTIONS request gets a 200 response
    """
    response = requests.options(url)
    assert response.status_code == 200, f"Test response : {response.text}"


@pytest.mark.admin
def test_admin_post():
    """
    Check if a POST request gets a 403 response
    """
    response = requests.post(url)
    assert response.status_code == 403, f"Test response : {response.text}"


@pytest.mark.admin
def test_admin_put():
    """
    Check if a PUT request gets a 403 response
    """
    response = requests.post(url)
    assert response.status_code == 403, f"Test response : {response.text}"