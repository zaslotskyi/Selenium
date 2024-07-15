from selenium import webdriver
import pytest

from web_tests.pages.login_page import LogiPage
from web_tests.pages.change_password_page import ChangePassword
from web_tests.helpers.users import Users
from web_tests.helpers.passwords import Passwords

VALID_USERNAME = 'Admin'

VALID_PASSWORD = 'admin123'
INVALID_PASSWORD = 'admin124'
NEW_PASSWORD = 'Qwerty!12'
MINIMUM_NUMBERS_6 = '123456'
NO_LETTER_PASSWORD = '1234567'


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(6)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def valid_user():
    return Users(VALID_USERNAME, VALID_PASSWORD)


@pytest.fixture(scope='session')
def invalid_user():
    return Users(VALID_USERNAME, INVALID_PASSWORD)


@pytest.fixture(scope='session')
def incorrect_current_password():
    return Passwords(current_password=INVALID_PASSWORD,
                     new_password=NEW_PASSWORD)

@pytest.fixture(scope='session')
def password_do_not_match():
    return Passwords(current_password=VALID_PASSWORD,
                     new_password=NEW_PASSWORD,
                     confirm_password=INVALID_PASSWORD)

@pytest.fixture(scope='session')
def minimum_number_of_characters_password():
    return Passwords(current_password=VALID_PASSWORD,
                     new_password=MINIMUM_NUMBERS_6,
                     confirm_password=MINIMUM_NUMBERS_6)


@pytest.fixture(scope='session')
def no_letters_in_password():
    return Passwords(current_password=VALID_PASSWORD,
                     new_password=NO_LETTER_PASSWORD,
                     confirm_password=NO_LETTER_PASSWORD)

@pytest.fixture()
def login_page(driver):
    page = LogiPage(driver)
    page.navigate()
    return page


@pytest.fixture()
def change_password_page(driver, login_page, valid_user):
    login_page.logging_in(valid_user)
    page = ChangePassword(driver).change_password_page()
    return page
