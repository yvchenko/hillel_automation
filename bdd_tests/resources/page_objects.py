class LoginPage:
    submit_button_id = '//*[@id="login-form"]/div[3]/input'
    name_field_id = '//*[@id="id_username"]'
    password_field_id = '//*[@id="id_password"]'


class AdminPage:
    page_header_id = '//*[@id="site-name"]/a'
    logout_button_id = '//*[@id="user-tools"]/a[3]'
    users_button_id = '//*[@id="content-main"]/div/table/tbody/tr[2]/th/a'
    create_button_id = '//*[@id="content-main"]/div/table/tbody/tr[2]/td[1]/a'
    search_bar_id = '//*[@id="searchbar"]'
    search_button_id = '//*[@id="changelist-search"]/div/input[2]'
    result_entry_id = '//*[@id="result_list"]/tbody/tr/th/a'
    superuser_filter_id = '//*[@id="changelist-filter"]/ul[2]/li[3]/a'
    success_notification_id = '//*[@id="main"]/div/ul/li'
    search_results_id = '//*[@id="changelist-search"]/div/span'


class CreatePage:
    username_field_id = '//*[@id="id_username"]'
    password_field_id = '//*[@id="id_password1"]'
    confirm_password_field_id = '//*[@id="id_password2"]'
    save_button_id = '//*[@id="user_form"]/div/div/input[1]'


class UserPage:
    username_header_id = '//*[@id="content"]/h2'
    first_name_field_id = '//*[@id="id_first_name"]'
    last_name_field_id = '//*[@id="id_last_name"]'
    email_field_id = '//*[@id="id_email"]'
    save_continue_button_id = '//*[@id="user_form"]/div/div/input[3]'
    success_notification_id = '//*[@id="main"]/div/ul/li'
    delete_button_id = '//*[@id="user_form"]/div/div/p/a'


class DeletePage:
    submit_button_id = '//*[@id="content"]/form/div/input[2]'


class LogoutPage:
    page_header_id = '//*[@id="content"]/h1'
