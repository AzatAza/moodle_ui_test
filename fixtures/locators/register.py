from selenium.webdriver.common.by import By


class RegisterLocators():
    LOGIN_INPUT = (By.ID, "id_username")
    PASSWORD_INPUT = (By.ID, "id_password")
    EMAIL_INPUT = (By.ID, "id_email")
    EMAIL2_INPUT = (By.ID, "id_email2")
    NAME_INPUT = (By.ID, "id_firstname")
    SURNAME_INPUT = (By.ID, "id_lastname")
    CITY_INPUT = (By.ID, "id_city")
    COUNTRY_INPUT = (By.XPATH, "//*[@id=\"id_country\"]/option[185]")
    LOGIN_BTN = (By.ID, "id_submitbutton")
    ERROR_USERNAME = (By.ID, "id_error_username")
    ERROR_PASSWORD = (By.ID, "id_error_password")
    ERROR_EMAIL = (By.ID, "id_error_email")
    ERROR_EMAIL2 = (By.ID, "id_error_email2")
    ERROR_FIRSTNAME = (By.ID, "id_error_firstname")
    ERROR_LASTNAME = (By.ID, "id_error_lastname")
    PASSWORD_LESS_THAN_8 = (By.XPATH, "//*[contains(text(), 'Passwords must be at least 8 characters long.')]")
    PASSWORD_NOT_A_DIGIT = (By.XPATH, "//*[contains(text(), 'Passwords must have at least 1 digit(s).')]")
    PASSWORD_NOT_LOWERCASE = (By.XPATH, "//*[contains(text(), 'Passwords must have at least 1 lower case letter(s).')]")
    PASSWORD_NOT_UPPERCASE = (By.XPATH, "//*[contains(text(), 'Passwords must have at least 1 upper case letter(s).')]")
    PASSWORD_NOT_A_SPEC_SYMBOL = (By.XPATH, "//*[contains(text(), 'Passwords must have at least 1 non-alphanumeric "
                                            "character(s) such as as *, -, or #.')]")
