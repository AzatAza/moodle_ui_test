import logging
from fixtures.locators.register import RegisterLocators
from fixtures.models.register import RegisterData
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("moodle")


class RegisterPage(BasePage):
    def add_new_user(self, data: RegisterData, is_submit: bool = True):
        """
        Register a new user
        """
        logger.info(f"Register a new user {data.login} and password {data.password}")
        self.fill_element(data=data.login, locator=RegisterLocators.LOGIN_INPUT)
        self.fill_element(data=data.password, locator=RegisterLocators.PASSWORD_INPUT)
        self.fill_element(data=data.email, locator=RegisterLocators.EMAIL_INPUT)
        self.fill_element(data=data.email2, locator=RegisterLocators.EMAIL2_INPUT)
        self.fill_element(data=data.name, locator=RegisterLocators.NAME_INPUT)
        self.fill_element(data=data.surname, locator=RegisterLocators.SURNAME_INPUT)
        self.fill_element(data=data.city, locator=RegisterLocators.CITY_INPUT)
        self.click_element(locator=RegisterLocators.COUNTRY_INPUT)
        if is_submit:
            self.click_element(locator=RegisterLocators.LOGIN_BTN)

    def get_name_error(self) -> str:
        try:
            if self.get_text(locator=RegisterLocators.ERROR_USERNAME) != '':
                return self.get_text(locator=RegisterLocators.ERROR_USERNAME)
            if self.get_text(locator=RegisterLocators.ERROR_USERNAME) != '':
                return self.get_text(locator=RegisterLocators.ERROR_USERNAME)
            if self.get_text(locator=RegisterLocators.ERROR_PASSWORD) != '':
                return self.get_text(locator=RegisterLocators.ERROR_PASSWORD)
            if self.get_text(locator=RegisterLocators.ERROR_EMAIL) != '':
                return self.get_text(locator=RegisterLocators.ERROR_EMAIL)
            if self.get_text(locator=RegisterLocators.ERROR_EMAIL2) != '':
                return self.get_text(locator=RegisterLocators.ERROR_EMAIL2)
            if self.get_text(locator=RegisterLocators.ERROR_FIRSTNAME) != '':
                return self.get_text(locator=RegisterLocators.ERROR_FIRSTNAME)
            if self.get_text(locator=RegisterLocators.ERROR_LASTNAME) != '':
                return self.get_text(locator=RegisterLocators.ERROR_LASTNAME)
        except BaseException:
            return "Something went wrong in getting error text"

    def get_password_error(self):
        try:
            if self.is_element_present(locator=RegisterLocators.PASSWORD_LESS_THAN_8):
                return True
            if self.is_element_present(locator=RegisterLocators.PASSWORD_NOT_A_DIGIT):
                return True
            if self.is_element_present(locator=RegisterLocators.PASSWORD_NOT_LOWERCASE):
                return True
            if self.is_element_present(locator=RegisterLocators.PASSWORD_NOT_UPPERCASE):
                return True
            if self.is_element_present(locator=RegisterLocators.PASSWORD_NOT_A_SPEC_SYMBOL):
                return True
        except BaseException:
            return "Something went wrong in getting error text"
