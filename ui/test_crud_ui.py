import time
import pytest

from selen import driver
from selenium.webdriver.common.by import By
from data.page_objects import AdminPage, CreatePage, UserPage, DeletePage

username = 'yvchenko'
password = '4b82iKJ2'
admin = 'admin'
first_name = 'nat'
last_name = 'yuvchenko'
email = 'nat@example.com'

@pytest.mark.ui
def test_create():
    """
    Check if creating a new user is successful
    """
    create_button = driver.find_element(By.XPATH, AdminPage.create_button_id)

    create_button.click()
    time.sleep(1)

    username_field = driver.find_element(By.XPATH, CreatePage.username_field_id)
    password_field = driver.find_element(By.XPATH, CreatePage.password_field_id)
    confirm_password_field = driver.find_element(By.XPATH, CreatePage.confirm_password_field_id)
    save_button = driver.find_element(By.XPATH, CreatePage.save_button_id)

    username_field.send_keys(username)
    time.sleep(1)
    password_field.send_keys(password)
    time.sleep(1)
    confirm_password_field.send_keys(password)
    time.sleep(1)

    save_button.click()
    time.sleep(1)

    username_header = driver.find_element(By.XPATH, UserPage.username_header_id)
    assert username_header.text == username


@pytest.mark.ui
def test_read_created():
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
    assert result_entry.text == username

    
@pytest.mark.ui
def test_find_admin(authorization):
    """
    Check if the admin can be found in the user list
    """
    users_button = driver.find_element(By.XPATH, AdminPage.users_button_id)

    users_button.click()
    time.sleep(1)

    search_bar = driver.find_element(By.XPATH, AdminPage.search_bar_id)
    search_button = driver.find_element(By.XPATH, AdminPage.search_button_id)

    search_bar.send_keys(admin)
    time.sleep(1)
    search_button.click()
    time.sleep(1)

    result_entry = driver.find_element(By.XPATH, AdminPage.result_entry_id)
    assert result_entry.text == admin


@pytest.mark.ui
def test_check_filters(authorization):
    """
    Check if user filters exclude users correctly
    """
    users_button = driver.find_element(By.XPATH, AdminPage.users_button_id)

    users_button.click()
    time.sleep(1)

    superuser_filter = driver.find_element(By.XPATH, AdminPage.superuser_filter_id)

    superuser_filter.click()
    time.sleep(1)

    result_entry = driver.find_element(By.XPATH, AdminPage.result_entry_id)
    assert result_entry.text != admin
    
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
