def test_successful_login(login_page, valid_user):
    assert login_page.successful_login(valid_user)


def test_unsuccessful_login(login_page, invalid_user):
    assert login_page.unsuccessful_login(invalid_user)


def test_password_can_be_reset(login_page,valid_user):
    assert login_page.reset_password(valid_user)
