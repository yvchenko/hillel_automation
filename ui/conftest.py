import pytest
from preconditions import get_credentials, open_site, log_in, login_assert, log_out, logout_assert, teardown


@pytest.fixture(autouse=True)
def authorization():
    get_credentials()
    open_site("https://www.aqa.science/admin/")
    log_in(get_credentials()['name'], get_credentials()['password'])
    login_assert('Django administration')
    yield
    log_out()
    logout_assert('Logged out')