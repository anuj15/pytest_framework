from utilities.commonmethods import CommonMethods


class HomePage(CommonMethods):
    # Defining locators
    this_is_a_link = "//a[text()='This is a link']"

    def __init__(self):
        super().__init__()

    def navigate_to_home_page(self):
        self.launch_browser()
        self.driver.get("https://artoftesting.com/samplesiteforselenium")


