import time
import pytest

from selen import driver
from selenium.webdriver.common.by import By
from data.page_objects import AdminPage, UserPage

username = 'yvchenko'
first_name = 'nat'
last_name = 'yuvchenko'
email = 'nat@example.com'


@pytest.mark.ui
def test_update_user_info():
    """
    Check if updating user info is successful
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

    first_name_field = driver.find_element(By.XPATH, UserPage.first_name_field_id)
    last_name_field = driver.find_element(By.XPATH, UserPage.last_name_field_id)
    email_field = driver.find_element(By.XPATH, UserPage.email_field_id)
    save_continue_button = driver.find_element(By.XPATH, UserPage.save_continue_button_id)

    first_name_field.send_keys(first_name)
    time.sleep(1)
    last_name_field.send_keys(last_name)
    time.sleep(1)
    email_field.send_keys(email)
    time.sleep(1)
    save_continue_button.click()

    success_notification = driver.find_element(By.XPATH, UserPage.success_notification_id)
    assert success_notification.text == f"The user “{username}” was changed successfully. You may edit it again below."


@pytest.mark.ui
def test_read_updated():
    """
    Check if the user created in the previous test can be found in the list of users
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

    first_name_text = driver.find_element(By.XPATH, UserPage.first_name_field_id)
    last_name_text = driver.find_element(By.XPATH, UserPage.last_name_field_id)
    email_text = driver.find_element(By.XPATH, UserPage.email_field_id)

    assert first_name_text.get_attribute('value') == first_name
    assert last_name_text.get_attribute('value') == last_name
    assert email_text.get_attribute('value') == email
