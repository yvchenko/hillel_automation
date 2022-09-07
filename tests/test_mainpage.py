import pytest
import requests

url = "https://www.aqa.science/"


@pytest.mark.mainpage
def test_mainpage_get():
    """
    Check if a GET request gets a 200 response
    """
    response = requests.get(url)
    assert response.status_code == 200, f"Test response : {response.text}"


@pytest.mark.mainpage
def test_mainpage_head():
    """
    Check if a HEAD request gets a 200 response
    """
    response = requests.head(url)
    assert response.status_code == 200, f"Test response : {response.text}"


@pytest.mark.mainpage
def test_mainpage_options():
    """
    Check if an OPTIONS request gets a 200 response
    """
    response = requests.options(url)
    assert response.status_code == 200, f"Test response : {response.text}"


@pytest.mark.mainpage
def test_mainpage_post():
    """
    Check if a POST request gets a 405 response
    """
    response = requests.post(url)
    assert response.status_code == 405, f"Test response : {response.text}"


@pytest.mark.mainpage
def test_mainpage_put():
    """
    Check if a PUT request gets a 405 response
    """
    response = requests.post(url)
    assert response.status_code == 405, f"Test response : {response.text}"