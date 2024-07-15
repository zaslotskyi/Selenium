from web_tests.pages.base_page import BasePage
from web_tests.locators.login_page_locators import LoginPageLocators


class LogiPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def username_field(self):
        return self.wait_for_element(LoginPageLocators.USERNAME)

    @property
    def password_field(self):
        return self.wait_for_element(LoginPageLocators.PASSWORD)

    @property
    def login_button(self):
        return self.wait_for_element(LoginPageLocators.LOGIN_BUTTON)

    @property
    def search_field(self):
        return self.wait_for_element(LoginPageLocators.MAIN_PAGE)

    @property
    def error_message(self):
        return self.wait_for_element(LoginPageLocators.ERROR_MESSAGE)

    @property
    def forgot_password_button(self):
        return self.wait_for_element(LoginPageLocators.FORGOT_PASSWORD_BUTTON)

    @property
    def reset_password_text(self):
        return self.wait_for_element(LoginPageLocators.RESET_PASSWORD_TEXT)

    def logging_in(self, user):
        self.username_field.send_keys(user.username)
        self.password_field.send_keys(user.password)
        self.login_button.click()

    def successful_login(self, user):
        self.logging_in(user)
        return self.search_field.is_displayed()

    def unsuccessful_login(self, user):
        self.logging_in(user)
        return self.error_message.is_displayed()

    def reset_password(self, user):
        self.forgot_password_button.click()
        self.username_field.send_keys(user.username)
        self.login_button.click()
        return self.reset_password_text.is_displayed()

    def navigate(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
