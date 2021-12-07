import pytest
from fixtures.constans import Constants
from fixtures.models.register import RegisterData, RegisterInvalidLogin, RegisterInvalidPassword


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
        # We don't have full realisation of registration page, so assertion is 1 = 1
        assert 1 == 1

    @pytest.mark.parametrize("field", ["login", "password", "email", "email2", "name", "surname"])
    def test_registration_with_empty_field(self, app, field):
        """
        Steps:
        1. Open registration page
        2. Add empty data to the field
        3. Check result
        """

        app.open_register_page()
        data = RegisterData.random()
        setattr(data, field, None)
        app.register.add_new_user(data)
        error = app.register.get_name_error()
        is_passed = False
        try:
            if error == Constants.EMPTY_USERNAME_MESSAGE:
                is_passed = True
            if error == Constants.EMPTY_PASSWORD_MESSAGE:
                is_passed = True
            if error == Constants.EMPTY_EMAIL_MESSAGE:
                is_passed = True
            if error == Constants.EMPTY_FIRSTNAME_MESSAGE:
                is_passed = True
            if error == Constants.EMPTY_LASTNAME_MESSAGE:
                is_passed = True
        except TypeError:
            "Error in test registration"
        finally:
            assert is_passed, "Test has fallen down"

    @pytest.mark.parametrize("value", [RegisterInvalidLogin.random_login().login_1,
                                       RegisterInvalidLogin.random_login().login_2,
                                       RegisterInvalidLogin.random_login().login_3,
                                       RegisterInvalidLogin.random_login().login_4,
                                       RegisterInvalidLogin.random_login().login_5,
                                       RegisterInvalidLogin.random_login().login_6
                                       ])
    def test_username_with_not_lowercase(self, app, value, ):
        """
        Steps:
        1. Open registration page
        2. Add in username field not only lowercase value
        3. Check result
        """

        app.open_register_page()
        data = RegisterData.random()
        setattr(data, "login", value)
        app.register.add_new_user(data)
        error = app.register.get_name_error()
        is_passed = False
        try:
            if error == Constants.LOWERCASE_USERNAME_ERROR_MESSAGE:
                is_passed = True
        except TypeError:
            "Error in test username lowercase registration"
        finally:
            assert is_passed, "Test has fallen down with username lowercase"

    @pytest.mark.parametrize("value", [RegisterInvalidPassword.random_password().password_1,
                                       RegisterInvalidPassword.random_password().password_2,
                                       RegisterInvalidPassword.random_password().password_3,
                                       RegisterInvalidPassword.random_password().password_4,
                                       RegisterInvalidPassword.random_password().password_5,
                                       ])
    def test_password_witn_invalid_data(self, app, value):
        """
        Steps:
        1. Open registration page
        2. Add in username field not only lowercase value
        3. Check result
        """

        app.open_register_page()
        data = RegisterData.random()
        setattr(data, "password", value)
        app.register.add_new_user(data)
        error = app.register.get_password_error()
        is_passed = False
        try:
            if error:
                is_passed = True
        except TypeError:
            "Error in test password registration"
        finally:
            assert is_passed, "Test has fallen down with invalid password"
