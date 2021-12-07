from selenium.webdriver.common.by import By


class LoginLocators():
    LOGIN_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginbtn")
    LOGIN_ERROR = (By.ID, "loginerrormessage")
    LOGIN_CONFIRM_ELEM = (By.ID, "action-menu-toggle-1")
    LOGOUT_BTN = (By.XPATH, "//*[@id=\"action-menu-1-menu\"]/a[6]")
    LOGIN_ENTER = (By.XPATH, "//*[@id=\"page-wrapper\"]/nav/ul[2]/li[2]/div/span/a")
    LOGOUT_BTN_2 = (By.XPATH, "//button[text()='Выход']")
