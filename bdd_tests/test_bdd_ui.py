import time

from pytest_bdd import scenarios, given, when, then, parsers
from resources.auth import get_credentials_dict
from resources.selen import driver
from resources.password import generate_password
from resources.page_objects import LoginPage, AdminPage, LogoutPage, CreatePage, UserPage, DeletePage
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
    time.sleep(3)


@given(parsers.re("I enter '(?P<username>.*)' into the search bar"))
def enter_user(username):
    search_bar = driver.find_element(By.XPATH, AdminPage.search_bar_id)

    search_bar.send_keys(username)
    time.sleep(1)


@given("I press the Search button")
def search():
    search_button = driver.find_element(By.XPATH, AdminPage.search_button_id)

    search_button.click()
    time.sleep(1)


@given("I click on the result entry")
def click_user():
    result_entry = driver.find_element(By.XPATH, AdminPage.result_entry_id)

    result_entry.click()
    time.sleep(1)


@when(parsers.re("I fill in the username field with '(?P<username>.*)'"))
def username(username):
    username_field = driver.find_element(By.XPATH, CreatePage.username_field_id)

    username_field.send_keys(username)
    time.sleep(1)


@when("I fill in the password field")
def password(request):
    request.password = generate_password(8)

    password_field = driver.find_element(By.XPATH, CreatePage.password_field_id)

    password_field.send_keys(request.password)
    time.sleep(1)


@when("I fill in the confirm password field")
def confirm_password(request):
    confirm_password_field = driver.find_element(By.XPATH, CreatePage.confirm_password_field_id)

    confirm_password_field.send_keys(request.password)
    time.sleep(1)


@when(parsers.re("I fill in the Name field with '(?P<name>.*)'"))
def name(name):
    first_name_field = driver.find_element(By.XPATH, UserPage.first_name_field_id)

    first_name_field.send_keys(name)
    time.sleep(1)


@when(parsers.re("I fill in the Last name field with '(?P<lastname>.*)'"))
def lastname(lastname):
    last_name_field = driver.find_element(By.XPATH, UserPage.last_name_field_id)

    last_name_field.send_keys(lastname)
    time.sleep(1)


@when(parsers.re("I fill in the Email field with '(?P<email>.*)'"))
def email(email):
    email_field = driver.find_element(By.XPATH, UserPage.email_field_id)

    email_field.send_keys(email)
    time.sleep(1)


@when("I press the Save button")
def save():
    save_button = driver.find_element(By.XPATH, CreatePage.save_button_id)

    save_button.click()
    time.sleep(1)


@when("I press the Delete button")
def delete():
    delete_button = driver.find_element(By.XPATH, UserPage.delete_button_id)

    delete_button.click()
    time.sleep(1)


@when("I press the Submit button")
def submit():
    submit_button = driver.find_element(By.XPATH, DeletePage.submit_button_id)

    submit_button.click()
    time.sleep(1)


@when("I press the Create button")
def create():
    create_button = driver.find_element(By.XPATH, AdminPage.create_button_id)

    create_button.click()
    time.sleep(1)


@when("I press the Continue button")
def save_cont():
    save_continue_button = driver.find_element(By.XPATH, UserPage.save_continue_button_id)

    save_continue_button.click()


@when("I click on Superuser filter")
def superuser_filter():
    superuser_filter = driver.find_element(By.XPATH, AdminPage.superuser_filter_id)

    superuser_filter.click()
    time.sleep(1)


@then(parsers.re("The result entry is the '(?P<username>.*)' name"))
def username_found(username):
    result_entry = driver.find_element(By.XPATH, AdminPage.result_entry_id)
    assert result_entry.text == username


@then(parsers.re("A user '(?P<username>.*)' is created"))
def new_user(username):
    username_header = driver.find_element(By.XPATH, UserPage.username_header_id)
    assert username_header.text == username


@then(parsers.re("The result entries do not contain '(?P<username>.*)'"))
def new_user(username):
    result_entry = driver.find_element(By.XPATH, AdminPage.result_entry_id)
    assert result_entry.text != username


@then(parsers.re("I receive a notification that user '(?P<username>.*)' is changed"))
def user_changed(username):
    success_notification = driver.find_element(By.XPATH, UserPage.success_notification_id)
    assert success_notification.text == f"The user ???{username}??? was changed successfully. You may edit it again below."


@then(parsers.re("I receive a notification that user '(?P<username>.*)' is deleted"))
def user_deleted(username):
    success_notification = driver.find_element(By.XPATH, AdminPage.success_notification_id)
    assert success_notification.text == f"The user ???{username}??? was deleted successfully."


@then(parsers.re("The Name is '(?P<name>.*)'"))
def name_check(name):
    first_name_text = driver.find_element(By.XPATH, UserPage.first_name_field_id)

    assert first_name_text.get_attribute('value') == name


@then(parsers.re("The Last name is '(?P<lastname>.*)'"))
def lastname_check(lastname):
    last_name_text = driver.find_element(By.XPATH, UserPage.last_name_field_id)

    assert last_name_text.get_attribute('value') == lastname


@then(parsers.re("The Email is '(?P<email>.*)'"))
def email_check(email):
    email_text = driver.find_element(By.XPATH, UserPage.email_field_id)

    assert email_text.get_attribute('value') == email


@then(parsers.re("I can't find '(?P<username>.*)' in the list of users"))
def user_not_found(username):
    search_bar = driver.find_element(By.XPATH, AdminPage.search_bar_id)
    search_button = driver.find_element(By.XPATH, AdminPage.search_button_id)

    search_bar.clear()
    search_bar.send_keys(username)
    time.sleep(1)
    search_button.click()
    time.sleep(1)

    search_results = driver.find_element(By.XPATH, AdminPage.search_results_id)
    assert '0 results' in search_results.text


@then("I log out of the site")
def log_out():
    logout_button = driver.find_element(By.XPATH, AdminPage.logout_button_id)

    logout_button.click()
    time.sleep(1)

    logout_header = driver.find_element(By.XPATH, LogoutPage.page_header_id)
    assert logout_header.text == "Logged out"


@then("I close the browser")
def teardown():
    driver.close()
