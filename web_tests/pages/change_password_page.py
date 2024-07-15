from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage

class ChangePassword(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    DROPDOWN_MENU = (By.XPATH, '//div[@id="app"]//p[@class="oxd-userdropdown-name"]')
    CHANGE_PASSWORD_BUTTON = (By.XPATH, '//a[@href="/web/index.php/pim/updatePassword"]')
    UPDATE_PASSWORD_FORM = (By.XPATH, '//div[@id="app"]//h6[@class="oxd-text oxd-text--h6 orangehrm-main-title"]')
    CURRENT_PASSWORD_FIELD =(By.XPATH, '(//input[@type="password"])[1]')
    NEW_PASSWORD_FIELD = (By.XPATH, '(//input[@type="password" and @autocomplete="off"])[1]')
    CONFIRM_NEW_PASSWORD_FIELD = (By.XPATH, '(//input[@type="password" and @autocomplete="off"])[2]')
    CANCEL_BUTTON = (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--ghost"]')
    SAVE_BUTTON = (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]')
    ERROR_MESSAGE_FOR_CURRENT_PASSWORD = (By.XPATH, '(//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message"])[1]')
    ERROR_MESSAGE_FOR_NEW_PASSWORD = (By.XPATH, '(//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message"])[2]')
    ERROR_MESSAGE_FOR_CONFIRM_PASSWORD = (By.XPATH, '(//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message"])[3]')
    ERROR_PASSWORDS_DO_NOT_MATCH = (By.XPATH, '//span[text()="Passwords do not match"]')
    ERROR_MINIMUM_NUMBER_OF_CHARACTERS = (By.XPATH, '//span[text()="Should have at least 7 characters"]')
    ERROR_NO_LETTER_IN_PASSWORD = (By.XPATH, '//span[text()="Your password must contain minimum 1 lower-case letter"]')
    CURRENT_PASSWORD_INCORRECT = (By.ID, 'oxd-toaster_1')
    @property
    def dropdown_menu_button(self):
        return self.wait_for_element(ChangePassword.DROPDOWN_MENU)

    @property
    def change_password_button(self):
        return self.wait_for_element(ChangePassword.CHANGE_PASSWORD_BUTTON)

    @property
    def update_password_form(self):
        return self.wait_for_element(ChangePassword.UPDATE_PASSWORD_FORM)

    @property
    def current_password_field(self):
        return self.wait_for_element(ChangePassword.CURRENT_PASSWORD_FIELD)

    @property
    def new_password_field(self):
        return self.wait_for_element(ChangePassword.NEW_PASSWORD_FIELD)

    @property
    def confirm_password_field(self):
        return self.wait_for_element(ChangePassword.CONFIRM_NEW_PASSWORD_FIELD)

    @property
    def cancel_button(self):
        return self.wait_for_element(ChangePassword.CANCEL_BUTTON)

    @property
    def save_button(self):
        return self.wait_for_element(ChangePassword.SAVE_BUTTON)

    @property
    def error_message_for_current_password_field(self):
        return self.wait_for_element(ChangePassword.ERROR_MESSAGE_FOR_CURRENT_PASSWORD)

    @property
    def error_message_for_new_password_field(self):
        return self.wait_for_element(ChangePassword.ERROR_MESSAGE_FOR_NEW_PASSWORD)

    @property
    def error_message_for_confirm_password_field(self):
        return self.wait_for_element(ChangePassword.ERROR_MESSAGE_FOR_CONFIRM_PASSWORD)

    @property
    def error_passwords_do_not_match(self):
        return self.wait_for_element(ChangePassword.ERROR_PASSWORDS_DO_NOT_MATCH)

    @property
    def error_minimum_number_of_characters(self):
        return self.wait_for_element(ChangePassword.ERROR_MINIMUM_NUMBER_OF_CHARACTERS)

    @property
    def error_no_letter_in_password(self):
        return self.wait_for_element(ChangePassword.ERROR_NO_LETTER_IN_PASSWORD)

    @property
    def current_password_is_incorrect_toast(self):
        return self.wait_for_element(ChangePassword.CURRENT_PASSWORD_INCORRECT)


    def change_password_page(self):
        self.dropdown_menu_button.click()
        self.change_password_button.click()
        return self

    def change_password_form_is_displayed(self):
        return self.update_password_form.is_displayed()

    def save_button_click(self):
        self.save_button.click()

    def empty_form_cant_be_send(self):
        self.save_button_click()
        return self.change_password_form_is_displayed()

    def error_message_for_current_password_is_displayed(self):
        return self.error_message_for_current_password_field.is_displayed()

    def error_message_for_new_password_is_displayed(self):
        return self.error_message_for_new_password_field.is_displayed()

    def error_message_for_confirm_password_is_displayed(self):
        return self.error_message_for_confirm_password_field.is_displayed()

    def current_password_is_incorrect_toast_is_displayed(self, password):
        self.current_password_field.send_keys(password.current_password)
        self.new_password_field.send_keys(password.new_password)
        self.confirm_password_field.send_keys(password.new_password)
        self.save_button_click()
        return self.current_password_is_incorrect_toast.is_displayed()

    def error_message_passwords_do_not_match_is_displayed(self, password):
        self.current_password_field.send_keys(password.current_password)
        self.new_password_field.send_keys(password.new_password)
        self.confirm_password_field.send_keys(password.confirm_password)
        return self.error_passwords_do_not_match.is_displayed()

    def error_message_minimum_number_of_characters_is_displayed(self, password):
        self.current_password_field.send_keys(password.current_password)
        self.new_password_field.send_keys(password.new_password)
        self.confirm_password_field.send_keys(password.current_password)
        return self.error_minimum_number_of_characters.is_displayed()

    def error_message_no_letters_in_password_is_displayed(self, password):
        self.current_password_field.send_keys(password.current_password)
        self.new_password_field.send_keys(password.new_password)
        self.confirm_password_field.send_keys(password.current_password)
        return self.error_no_letter_in_password.is_displayed()



