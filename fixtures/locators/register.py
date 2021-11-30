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
    ERROR_FIRSTNAME = (By.ID, "id_error_firstname")