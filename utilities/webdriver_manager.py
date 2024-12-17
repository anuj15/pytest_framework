import os.path
import time

from selenium import webdriver
from utilities.config_reader import ConfigReader
class webdriver_manager(ConfigReader):
    def __init__(self):
        super(webdriver_manager, self).__init__()

    def launch_browser(self):
        dir_path = self.get_file_path("browsers")
        config_browser = self.fetch_data_from_config_file("current_execution_browser")
        match config_browser:
            case "chrome_driver":
                self.driver_name = self.fetch_data_from_config_file("chrome_driver")
                self.service = webdriver.ChromeService(os.path.join(dir_path,self.driver_name))
                self.driver = webdriver.Chrome(service=self.service)

            case "firefox_driver":
                self.driver_name = self.fetch_data_from_config_file("firefox_driver")
                self.service = webdriver.FirefoxService(os.path.join(dir_path,self.driver_name))
                self.driver = webdriver.Firefox(service=self.service)
            case "edge_driver":
                self.driver_name = self.fetch_data_from_config_file("edge_driver")
                self.service = webdriver.EdgeService(os.path.join(dir_path,self.driver_name))
                self.driver = webdriver.Edge(service=self.service)
            case _:
                self.driver_name = self.fetch_data_from_config_file("chrome_driver")
                self.service = webdriver.ChromeService(os.path.join(dir_path,self.driver_name))
                self.driver = webdriver.Chrome(service=self.service)

        # self.driver.implicitly_wait(int(self.fetch_data_from_config_file("default_implicit_wait"))
        self.driver.maximize_window()
        print("Browser Launch Completed")
        return self.driver


