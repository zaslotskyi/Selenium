from web_tests.pages.base_page import BasePage
from web_tests.locators.change_password_page_locators import ChangePasswordLocators


class ChangePassword(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def dropdown_menu_button(self):
        return self.wait_for_element(ChangePasswordLocators.DROPDOWN_MENU)

    @property
    def change_password_button(self):
        return self.wait_for_element(ChangePasswordLocators.CHANGE_PASSWORD_BUTTON)

    @property
    def update_password_form(self):
        return self.wait_for_element(ChangePasswordLocators.UPDATE_PASSWORD_FORM)

    @property
    def current_password_field(self):
        return self.wait_for_element(ChangePasswordLocators.CURRENT_PASSWORD_FIELD)

    @property
    def new_password_field(self):
        return self.wait_for_element(ChangePasswordLocators.NEW_PASSWORD_FIELD)

    @property
    def confirm_password_field(self):
        return self.wait_for_element(ChangePasswordLocators.CONFIRM_NEW_PASSWORD_FIELD)

    @property
    def cancel_button(self):
        return self.wait_for_element(ChangePasswordLocators.CANCEL_BUTTON)

    @property
    def save_button(self):
        return self.wait_for_element(ChangePasswordLocators.SAVE_BUTTON)

    @property
    def error_message_for_current_password_field(self):
        return self.wait_for_element(ChangePasswordLocators.ERROR_MESSAGE_FOR_CURRENT_PASSWORD)

    @property
    def error_message_for_new_password_field(self):
        return self.wait_for_element(ChangePasswordLocators.ERROR_MESSAGE_FOR_NEW_PASSWORD)

    @property
    def error_message_for_confirm_password_field(self):
        return self.wait_for_element(ChangePasswordLocators.ERROR_MESSAGE_FOR_CONFIRM_PASSWORD)

    @property
    def error_passwords_do_not_match(self):
        return self.wait_for_element(ChangePasswordLocators.ERROR_PASSWORDS_DO_NOT_MATCH)

    @property
    def error_minimum_number_of_symbols(self):
        return self.wait_for_element(ChangePasswordLocators.ERROR_MINIMUM_NUMBER_OF_CHARACTERS)

    @property
    def error_no_letter_in_password(self):
        return self.wait_for_element(ChangePasswordLocators.ERROR_NO_LETTER_IN_PASSWORD)

    @property
    def incorrect_password_toast(self):
        return self.wait_for_element(ChangePasswordLocators.CURRENT_PASSWORD_INCORRECT)

    def change_password_page(self):
        self.dropdown_menu_button.click()
        self.change_password_button.click()
        return self

    def password_fields_filling(self, actual_password,
                                new_password,
                                confirm_password):
        self.current_password_field.send_keys(actual_password)
        self.new_password_field.send_keys(new_password)
        self.confirm_password_field.send_keys(confirm_password)
        self.save_button_click()

    def save_button_click(self):
        self.save_button.click()

    def empty_form_cant_be_send(self):
        self.save_button_click()
        return self.change_password_form_is_displayed()

    def change_password_form_is_displayed(self):
        return self.update_password_form.is_displayed()

    def error_message_for_current_password_is_displayed(self):
        return self.error_message_for_current_password_field.is_displayed()

    def error_message_for_new_password_is_displayed(self):
        return self.error_message_for_new_password_field.is_displayed()

    def error_message_for_confirm_password_is_displayed(self):
        return self.error_message_for_confirm_password_field.is_displayed()

    def incorrect_password_toast_is_displayed(self):
        return self.incorrect_password_toast.is_displayed()

    def passwords_do_not_match_error_message_is_displayed(self):
        return self.error_passwords_do_not_match.is_displayed()

    def minimum_number_of_symbols_error_message_is_displayed(self):
        return self.error_minimum_number_of_symbols.is_displayed()

    def no_letters_in_password_error_message_is_displayed(self):
        return self.error_no_letter_in_password.is_displayed()
