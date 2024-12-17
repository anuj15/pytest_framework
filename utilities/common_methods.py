import selenium
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utilities.webdriver_manager import webdriver_manager


class common_methods(webdriver_manager):

    def __init__(self):
        super(common_methods, self).__init__()

    def wait_for_element(self, locator, timeout=10):
        try:

            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
            print("Element Found")
            return element
        except NoSuchElementException:
            print("Element not found")
            return False

    def click_on_element(self, locator):
        try:
            element = self.wait_for_element(locator)
            element.click()
            print("Element Clicked")
        except selenium.common.exceptions.NoSuchElementException:
            print("Element not found")
            return False
