from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        driver.implicitly_wait(1)
        try:
            WebDriverWait(driver, 1).until(EC.presence_of_element_located(locator))
        except Exception:
            element_found = False
        return element_found
