import pytest
from fixtures.constans import Constants
from fixtures.models.login import LoginData
from fixtures.models.register import RegisterData
from fixtures.pages.register import RegisterPage


class TestRegistration:
    def test_registration_with_valid_data(self, app, user_data):
        """
        Steps:
        1. Open registration page
        2. Add valid data
        3. Check result
        """

        app.open_register_page()
        data = RegisterData.random()
        app.register.add_new_user(data)
        assert 1 == 1

    def test_registration_with_empty_name(self, app, user_data):
        """
        Steps:
        1. Open registration page
        2. Add empty data to the name
        3. Check result
        """

        app.open_register_page()
        data = RegisterData.random()
        setattr(data, 'name', None)
        app.register.add_new_user(data)
        error = app.register.get_name_error()
        assert error == Constants.FIRSTNAME_ERROR_MESSAGE, 'Check error FIRSTNAME'
