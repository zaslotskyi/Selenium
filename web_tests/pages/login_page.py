from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage


class LogiPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    USERNAME = (By.XPATH, '//div[@id="app"]//input[@name="username"]')
    PASSWORD = (By.XPATH, '//div[@id="app"]//input[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//div[@id="app"]//button[@type="submit"]')
    MAIN_PAGE = (By.XPATH, '//div[@id="app"]//input[@placeholder="Search"]')
    ERROR_MESSAGE = (By.XPATH, '//div[@id="app"]//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]')
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//div[@id="app"]//p[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]')
    RESET_PASSWORD_TEXT = (By.XPATH, '//div[@id="app"]//h6[@class="oxd-text oxd-text--h6 orangehrm-forgot-password-title"]')
    CANCEL_BUTTON = (By.XPATH, '//div[@id="app"]//button[@type="button"]')

    @property
    def username_field(self):
        return self.wait_for_element(LogiPage.USERNAME)

    @property
    def password_field(self):
        return self.wait_for_element(LogiPage.PASSWORD)

    @property
    def login_button(self):
        return self.wait_for_element(LogiPage.LOGIN_BUTTON)

    @property
    def search_field(self):
        return self.wait_for_element(LogiPage.MAIN_PAGE)

    @property
    def error_message(self):
        return self.wait_for_element(LogiPage.ERROR_MESSAGE)

    @property
    def forgot_password_button(self):
        return self.wait_for_element(LogiPage.FORGOT_PASSWORD_BUTTON)

    @property
    def reset_password_text(self):
        return self.wait_for_element(LogiPage.RESET_PASSWORD_TEXT)

    def logging_in(self, user):
        self.username_field.send_keys(user.username)
        self.password_field.send_keys(user.password)
        self.login_button.click()
        # self.driver.implicitly_wait(6)

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
        # self.driver.implicitly_wait(6)
        return self.reset_password_text.is_displayed()

    def navigate(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
