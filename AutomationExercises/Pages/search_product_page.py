from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Utilities.common import LogFunc
from Utilities.config import *
import os
import time

logger = LogFunc().get_log()


class SearchProducts:

    def __init__(self, driver):
        self.driver = driver
        #self.wait = WebDriverWait(driver, 10)

    # Locators
    ALL_PRODUCTS = (By.XPATH, "//h2[normalize-space()='All Products']")
    PRODUCTS_LINK = (By.XPATH, "//a[@href='/products']")
    SEARCH_BTN = (By.XPATH, "//button[@id='submit_search']")
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_PRODUCTS_MSG = (By.XPATH, "//h2[normalize-space()='Searched Products']")
    FEATURED_ITEMS = (By.XPATH, "//div[@class='features_items']")

    # Elements
    def get_product_link(self):
        return self.driver.find_element(*self.PRODUCTS_LINK)

    def get_all_products(self):
        return self.driver.find_element(*self.ALL_PRODUCTS)

    def get_search_btn(self):
        return self.driver.find_element(*self.SEARCH_BTN)

    def get_search_input(self):
        return self.driver.find_element(*self.SEARCH_INPUT)

    def get_search_products_msg(self):
        return self.driver.find_element(*self.SEARCH_PRODUCTS_MSG).text

    def get_featured_items(self):
        return self.driver.find_element(*self.FEATURED_ITEMS)

    def get_title(self):
        return self.driver.title

    # Methods

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        new_path = os.path.join(screenshot_folder, filename)
        os.rename(filename, new_path)
        time.sleep(2)

    def click_all_products(self):
        all_products = self.get_all_products().text
        print(all_products)
        return all_products

    def click_products(self):
        search_products = self.get_product_link()
        search_products.click()

    def input_products(self, products):
        self.get_search_input().send_keys(products)
        logger.info(f'Product: {products}')

    def click_search_btn(self):
        # search_products = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.get_search_btn()))
        search_products = self.get_search_btn()
        search_products.click()






