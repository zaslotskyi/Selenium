def test_change_password_form_is_displayed(change_password_page):
    assert change_password_page.change_password_form_is_displayed()


def test_empty_form_cant_be_send(change_password_page):
    assert change_password_page.empty_form_cant_be_send()


def test_error_messages(change_password_page):
    change_password_page.save_button_click()
    assert change_password_page.error_message_for_current_password_field
    assert change_password_page.error_message_for_new_password_field
    assert change_password_page.error_message_for_confirm_password_field


def test_incorrect_password_toast_is_displayed(change_password_page,
                                               incorrect_current_password):
    assert change_password_page.incorrect_password_toast_is_displayed()


def test_passwords_do_not_match_error_message_is_displayed(change_password_page,
                                                           password_do_not_match):
    assert change_password_page.passwords_do_not_match_error_message_is_displayed()


def test_minimum_number_of_symbols_error_message_is_displayed(change_password_page,
                                                              minimum_numbers_of_symbols_password):
    assert change_password_page.minimum_number_of_symbols_error_message_is_displayed()


def test_no_letters_in_password_error_message_is_displayed(change_password_page,
                                                           no_letters_in_password):
    assert change_password_page.no_letters_in_password_error_message_is_displayed()

