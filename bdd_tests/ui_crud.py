import time

from pytest_bdd import scenarios, given, when, then, parsers
from resources.auth import get_credentials_dict
from resources.selen import driver
from resources.page_objects import LoginPage, AdminPage, LogoutPage
from selenium.webdriver.common.by import By

scenarios('../bdd_tests/features/ui_crud.feature')


@given("I opened the site")
def open():
    driver.get("https://www.aqa.science/admin/")


@given("I entered the admin's credentials")
def auth():
    creds = get_credentials_dict("data.json")
    name_field = driver.find_element(By.XPATH, LoginPage.name_field_id)

    password_field = driver.find_element(By.XPATH, LoginPage.password_field_id)

    name_field.send_keys(creds['name'])
    time.sleep(1)
    password_field.send_keys(creds['password'])


@given("I have logged in")
def auth():
    submit_button = driver.find_element(By.XPATH, LoginPage.submit_button_id)

    submit_button.click()
    time.sleep(1)

    element_fo_find = driver.find_element(By.XPATH, AdminPage.page_header_id)
    assert element_fo_find.text == 'Django administration'


@given("I opened the Users page")
def users():
    driver.get("https://www.aqa.science/admin/auth/user/")


@when(parsers.re("I enter '(?P<username>.*)' into the search bar"))
def enter_user(username):
    search_bar = driver.find_element(By.XPATH, AdminPage.search_bar_id)

    search_bar.send_keys(username)
    time.sleep(1)


@when("I press the Search button")
def search():
    search_button = driver.find_element(By.XPATH, AdminPage.search_button_id)

    search_button.click()
    time.sleep(1)


@then("The result entry is the user's name")
def username_found():
    result_entry = driver.find_element(By.XPATH, AdminPage.result_entry_id)
    assert result_entry.text == "admin"


@then("I log out of the site")
def log_out():
    logout_button = driver.find_element(By.XPATH, AdminPage.logout_button_id)

    logout_button.click()
    time.sleep(1)

    logout_header = driver.find_element(By.XPATH, LogoutPage.page_header_id)
    assert logout_header.text == "Logged out"