from selenium.webdriver.common.by import By


class ChangePasswordLocators:
    DROPDOWN_MENU = (By.XPATH, '//div[@id="app"]//p[@class="oxd-userdropdown-name"]')
    CHANGE_PASSWORD_BUTTON = (By.XPATH, '//a[@href="/web/index.php/pim/updatePassword"]')
    UPDATE_PASSWORD_FORM = (By.XPATH, '//div[@id="app"]//h6[@class="oxd-text oxd-text--h6 orangehrm-main-title"]')
    CURRENT_PASSWORD_FIELD = (By.XPATH, '(//input[@type="password"])[1]')
    NEW_PASSWORD_FIELD = (By.XPATH, '(//input[@type="password" and @autocomplete="off"])[1]')
    CONFIRM_NEW_PASSWORD_FIELD = (By.XPATH, '(//input[@type="password" and @autocomplete="off"])[2]')
    CANCEL_BUTTON = (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--ghost"]')
    SAVE_BUTTON = (
        By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]')
    ERROR_MESSAGE_FOR_CURRENT_PASSWORD = (
        By.XPATH,
        '(//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message"])[1]')
    ERROR_MESSAGE_FOR_NEW_PASSWORD = (
        By.XPATH,
        '(//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message"])[2]')
    ERROR_MESSAGE_FOR_CONFIRM_PASSWORD = (
        By.XPATH,
        '(//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message"])[3]')
    ERROR_PASSWORDS_DO_NOT_MATCH = (By.XPATH, '//span[text()="Passwords do not match"]')
    ERROR_MINIMUM_NUMBER_OF_CHARACTERS = (By.XPATH, '//span[text()="Should have at least 7 characters"]')
    ERROR_NO_LETTER_IN_PASSWORD = (By.XPATH, '//span[text()="Your password must contain minimum 1 lower-case letter"]')
    CURRENT_PASSWORD_INCORRECT = (By.ID, 'oxd-toaster_1')
