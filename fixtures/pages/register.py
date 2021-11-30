import logging
from fixtures.locators.register import RegisterLocators
from fixtures.models.login import LoginData
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
        return self.get_text(locator=RegisterLocators.ERROR_FIRSTNAME)
    # def auth(self, data: LoginData, is_submit: bool = True):
    #     """
    #     Auth func
    #     Если мы не login  → login
    #     Если мы login → logout → login
    #     """
    #     logger.info(f"Login with user {data.login} and password {data.password}")
    #     self.fill_element(data=data., locator=LoginLocators.)
    #     self.fill_element(data=data.password, locator=LoginLocators.PASSWORD_INPUT)
    #     if is_submit:
    #         self.click_element(locator=LoginLocators.LOGIN_BTN)
    #
