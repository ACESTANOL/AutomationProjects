from selenium.webdriver.common.by import By
from Utilities.common import LogFunc
from Utilities.config import *
import os
import time

logger = LogFunc().get_log()


class TestCases:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    TEST_PAGE = (By.XPATH, "//a[normalize-space()='Test Cases']")

    # Elements
    def get_test_page(self):
        return self.driver.find_element(*self.TEST_PAGE)

    def get_title(self):
        return self.driver.title

    # Methods

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        new_path = os.path.join(screenshot_folder, filename)
        os.rename(filename, new_path)
        time.sleep(2)

    def click_test_cases(self):
        test_cases = self.get_test_page()
        test_cases.click()




