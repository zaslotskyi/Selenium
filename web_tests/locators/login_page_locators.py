from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME = (By.XPATH, '//div[@id="app"]//input[@name="username"]')
    PASSWORD = (By.XPATH, '//div[@id="app"]//input[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//div[@id="app"]//button[@type="submit"]')
    MAIN_PAGE = (By.XPATH, '//div[@id="app"]//input[@placeholder="Search"]')
    ERROR_MESSAGE = (By.XPATH, '//div[@id="app"]//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]')
    FORGOT_PASSWORD_BUTTON = (
        By.XPATH, '//div[@id="app"]//p[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]')
    RESET_PASSWORD_TEXT = (
        By.XPATH, '//div[@id="app"]//h6[@class="oxd-text oxd-text--h6 orangehrm-forgot-password-title"]')
    CANCEL_BUTTON = (By.XPATH, '//div[@id="app"]//button[@type="button"]')
