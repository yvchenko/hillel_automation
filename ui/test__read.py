import time
import pytest

from selen import driver
from selenium.webdriver.common.by import By
from data.page_objects import AdminPage

admin = 'admin'


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
