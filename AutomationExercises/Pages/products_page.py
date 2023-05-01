from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Utilities.common import LogFunc
from Utilities.config import *
import os
import time

logger = LogFunc().get_log()


class AllProducts:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators #
    PRODUCTS_BTN = (By.XPATH, "//a[@href='/products']")
    ALL_PRODUCTS_MSG = (By.XPATH, "//h2[normalize-space()='All Products']")
    VIEW_PRODUCT_BTN = (By.CSS_SELECTOR, "a[href='/product_details/1']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div[class='product-information'] h2")
    CATEGORY = (By.XPATH, "//h2[normalize-space()='Category']")
    PRICE = (By.CSS_SELECTOR, "div[class='product-information'] span span")
    AVAILABILITY = (By.XPATH, "//b[normalize-space()='Availability:']")
    CONDITION = (By.XPATH, "//b[normalize-space()='Condition:']")
    BRAND = (By.XPATH, "//b[normalize-space()='Brand:']")
    PRODUCT_LIST = (By.CLASS_NAME, "card")

    # Elements
    def get_all_products(self):
        return self.driver.find_element(*self.PRODUCTS_BTN)

    def get_all_products_msg(self):
        return self.driver.find_element(*self.ALL_PRODUCTS_MSG).text

    def get_view_products(self):
        return self.driver.find_element(*self.VIEW_PRODUCT_BTN)

    def get_product_name(self):
        return self.driver.find_element(*self.PRODUCT_NAME).text

    def get_category(self):
        return self.driver.find_element(*self.CATEGORY).text

    def get_price(self):
        return self.driver.find_element(*self.PRICE).text

    def get_availability(self):
        return self.driver.find_element(*self.AVAILABILITY).text

    def get_condition(self):
        return self.driver.find_element(*self.CONDITION).text

    def get_product_list(self):
        return self.driver.find_element(*self.PRODUCT_LIST)

    def get_brand(self):
        return self.driver.find_element(*self.BRAND).text

    def get_title(self):
        return self.driver.title

    # Methods

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        new_path = os.path.join(screenshot_folder, filename)
        os.rename(filename, new_path)
        time.sleep(2)

    def click_all_products(self):
        all_products = self.get_all_products()
        all_products.click()

    def click_view_products(self):
        view_products = self.get_view_products()
        view_products.click()









