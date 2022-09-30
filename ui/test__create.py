import time
import pytest

from selen import driver
from selenium.webdriver.common.by import By
from data.page_objects import AdminPage, CreatePage, UserPage

username = 'yvchenko'
password = '4b82iKJ2'


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
