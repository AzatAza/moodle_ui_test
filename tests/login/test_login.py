import pytest
from fixtures.constans import Constants
from fixtures.models.login import LoginData


class TestLogin:
    def test_login_with_valid_data(self, app, user_data):
        """
        Steps:
        1. Open login page
        2. Auth with valid data
        3. Check result
        """

        app.open_login_page()
        app.login.auth(data=user_data, is_submit=True)
        assert app.login.is_element_exist() == True, 'The element doesnt exist'

    def test_login_with_invalid_data(self, app):
        """
        Steps:
        1. Open login page
        2. Auth with invalid data
        3. Check result
        """
        app.open_login_page()
        data = LoginData.random()
        app.login.check_login()
        app.login.auth(data)
        assert app.login.get_error_text() == Constants.LOGIN_ERROR_MESSAGE, 'Check error message'
