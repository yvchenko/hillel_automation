import time
import pytest

from selen import driver
from selenium.webdriver.common.by import By
from data.page_objects import AdminPage, DeletePage, UserPage

username = 'yvchenko'
first_name = 'nat'
last_name = 'yuvchenko'
email = 'nat@example.com'


@pytest.mark.ui
def test_delete_user():
    """
    Check if creating a new user is successful
    """
    users_button = driver.find_element(By.XPATH, AdminPage.users_button_id)

    users_button.click()
    time.sleep(1)

    search_bar = driver.find_element(By.XPATH, AdminPage.search_bar_id)
    search_button = driver.find_element(By.XPATH, AdminPage.search_button_id)

    search_bar.send_keys(username)
    time.sleep(1)
    search_button.click()
    time.sleep(1)

    result_entry = driver.find_element(By.XPATH, AdminPage.result_entry_id)
    result_entry.click()
    time.sleep(1)

    delete_button = driver.find_element(By.XPATH, UserPage.delete_button_id)
    delete_button.click()
    time.sleep(1)

    submit_button = driver.find_element(By.XPATH, DeletePage.submit_button_id)
    submit_button.click()
    time.sleep(1)

    success_notification = driver.find_element(By.XPATH, AdminPage.success_notification_id)
    assert success_notification.text == f"The user “{username}” was deleted successfully."


@pytest.mark.ui
def test_read_deleted():

    """
    Check if the deleted user is not found in the user list
    """
    users_button = driver.find_element(By.XPATH, AdminPage.users_button_id)

    users_button.click()
    time.sleep(1)

    search_bar = driver.find_element(By.XPATH, AdminPage.search_bar_id)
    search_button = driver.find_element(By.XPATH, AdminPage.search_button_id)

    search_bar.send_keys(username)
    time.sleep(1)
    search_button.click()
    time.sleep(1)

    search_results = driver.find_element(By.XPATH, AdminPage.search_results_id)
    assert '0 results' in search_results.text
