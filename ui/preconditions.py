import time
import json

from selen import driver
from selenium.webdriver.common.by import By
from data.page_objects import LoginPage, AdminPage, LogoutPage


def get_credentials():
    with open('resources/data.json', "r") as f:
        secret_variables = json.load(f)
    return secret_variables


def open_site(path):
    driver.get(path)


def log_in(login, password):
    name_field = driver.find_element(By.XPATH, LoginPage.name_field_id)
    submit_button = driver.find_element(By.XPATH, LoginPage.submit_button_id)
    password_field = driver.find_element(By.XPATH, LoginPage.password_field_id)

    name_field.send_keys(login)
    time.sleep(1)
    password_field.send_keys(password)

    submit_button.click()
    time.sleep(1)


def login_assert(login_text):
    element_fo_find = driver.find_element(By.XPATH, AdminPage.page_header_id)
    assert element_fo_find.text == login_text


def log_out():
    logout_button = driver.find_element(By.XPATH, AdminPage.logout_button_id)

    logout_button.click()
    time.sleep(1)


def logout_assert(logout_text):
    logout_header = driver.find_element(By.XPATH, LogoutPage.page_header_id)
    assert logout_header.text == logout_text


def teardown():
    driver.close()
