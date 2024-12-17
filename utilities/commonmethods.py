from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utilities.webdrivermanager import WebdriverManager


class CommonMethods(WebdriverManager):

    def __init__(self):
        super(CommonMethods, self).__init__()

    def wait_for_element(self, locator, timeout=10):
        try:

            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
            print(f"Locator: {locator} found")
            return element
        except (NoSuchElementException, TimeoutException):
            print(f"Locator: {locator} not found")
            return False

    def click_on_element(self, locator):
        try:
            element = self.wait_for_element(locator)
            element.click()
            print(f"Element: {element}  Clicked")
        except NoSuchElementException:
            print(f"Locator: {locator} not found")
            return False
