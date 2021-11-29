from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager import driver
from selenium import webdriver


class BasePage:
    def __init__(self, app):
        self.app = app

    def custom_find_element(self, locator, wait_time=10):
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Cant{locator}",
        )
        return element

    def click_element(self, locator, wait_time=10):
        """
        Click_element == click()
        """
        element = self.custom_find_element(locator, wait_time)
        element.click()

    def fill_element(self, data, locator, wait_time=10):
        """
        Fill element == send_keys()
        :param data: string to fill
        """
        element = self.custom_find_element(locator, wait_time)
        if data:
            element.send_keys(data)

    def get_text(self, locator, wait_time=10):
        """
        Get element text
        """
        element = self.custom_find_element(locator, wait_time)
        return element.text

    def is_element_present(self, locator):
        driver = self.app.driver
        element_found = True
        driver.implicitly_wait(5)
        try:
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(locator)
            )
        except:
            element_found = False
        return element_found

    def get_element(self, locator):

        self.app.driver.implicitly_wait(10)
        # if len(self.app.driver.find_element(By.ID, "single_button61a20145e9cc42")) > 0:
        #     self.app.driver.find_element(By.ID, "single_button61a20145e9cc42").click()

        #
        # try:
        #     self.app.driver.find_element(locator)
        # except:
        #     return False
        # else:
        #     return True

        # try:
        #     wait = WebDriverWait(self.app.driver, wait_time)
        #     element = wait.until(EC.element_to_be_clickable(locator))
        #     return True
        # except TimeoutError:
        #     return False

        # try:
        #     element = self.custom_find_element(locator, wait_time=5)
        #     return True
        # except TimeoutError:
        #     return False