from selenium import webdriver
import pytest
import os
from dotenv import load_dotenv

from web_tests.pages.login_page import LogiPage
from web_tests.pages.change_password_page import ChangePassword
from web_tests.helpers.users import Users
from web_tests.helpers.passwords import Passwords

load_dotenv()


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def valid_user():
    return Users(os.getenv('VALID_USERNAME'), os.getenv('VALID_PASSWORD'))


@pytest.fixture(scope='session')
def invalid_user():
    return Users(os.getenv('VALID_USERNAME'), os.getenv('INVALID_PASSWORD'))


# @pytest.fixture(scope='session')
# def incorrect_current_password():
#     return Passwords(current_password=os.getenv('INVALID_PASSWORD'),
#                      new_password=os.getenv('NEW_PASSWORD'))
#
#
# @pytest.fixture(scope='session')
# def password_do_not_match():
#     return Passwords(current_password=os.getenv('VALID_PASSWORD'),
#                      new_password=os.getenv('NEW_PASSWORD'),
#                      confirm_password=os.getenv('INVALID_PASSWORD'))
#
#
# @pytest.fixture(scope='session')
# def minimum_number_of_characters_password():
#     return Passwords(current_password=os.getenv('VALID_PASSWORD'),
#                      new_password=os.getenv('MINIMUM_NUMBERS_6'),
#                      confirm_password=os.getenv('MINIMUM_NUMBERS_6'))
#
#
# @pytest.fixture(scope='session')
# def no_letters_in_password():
#     return Passwords(current_password=os.getenv('VALID_PASSWORD'),
#                      new_password=os.getenv('NO_LETTER_PASSWORD'),
#                      confirm_password=os.getenv('NO_LETTER_PASSWORD'))


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


@pytest.fixture()
def incorrect_current_password(driver, change_password_page):
    page = ChangePassword(driver)
    return page.password_fields_filling(os.getenv('INVALID_PASSWORD'),
                                        os.getenv('NEW_PASSWORD'),
                                        os.getenv('NEW_PASSWORD'))


@pytest.fixture()
def password_do_not_match(driver, change_password_page):
    page = ChangePassword(driver)
    return page.password_fields_filling(os.getenv('VALID_PASSWORD'),
                                        os.getenv('NEW_PASSWORD'),
                                        os.getenv('INVALID_PASSWORD'))

@pytest.fixture()
def minimum_numbers_of_symbols_password(driver, change_password_page):
    page = ChangePassword(driver)
    return page.password_fields_filling(os.getenv('VALID_PASSWORD'),
                                        os.getenv('MINIMUM_NUMBERS_6'),
                                        os.getenv('MINIMUM_NUMBERS_6'))

@pytest.fixture()
def no_letters_in_password(driver, change_password_page):
    page = ChangePassword(driver)
    return page.password_fields_filling(os.getenv('VALID_PASSWORD'),
                                        os.getenv('NO_LETTER_PASSWORD'),
                                        os.getenv('NO_LETTER_PASSWORD'))