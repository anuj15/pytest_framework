import selenium
from selenium.webdriver.common.by import By

from utilities.common_methods import common_methods

class HomePage(common_methods):
    # Defining locators
    this_is_a_link = "//a[text()='This is a link']"

    def __init__(self):
        super().__init__()


    def navigate_to_home_page(self):
        self.launch_browser()
        self.driver.get("https://artoftesting.com/samplesiteforselenium")




