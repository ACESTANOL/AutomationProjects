import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from Utilities.config import *
from Utilities.common import LogFunc

logger = LogFunc().get_log()


class SubscriptionCart:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    BODY_TAG_NAME = By.TAG_NAME, 'body'
    CART_BTN_XPATH = By.XPATH, "//a[normalize-space()='Cart']"
    SUBSCRIBE_BUTTON_XPATH = By.XPATH, "//button[@id='subscribe']"
    EMAIL_INPUT_XPATH = By.XPATH, "//input[@id='susbscribe_email']"
    SUBSCRIPTION = By.XPATH, "//h2[normalize-space()='Subscription']"
    SUCCESS_MSG = By.XPATH, "//div[@class='alert-success alert']"

    # Elements
    def get_success_msg(self):
        success_msg = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SUCCESS_MSG))
        return success_msg

    def get_cart(self):
        return self.driver.find_element(*self.CART_BTN_XPATH)

    def get_email(self):
        return self.driver.find_element(*self.EMAIL_INPUT_XPATH)

    def get_btn_subscribe(self):
        return self.driver.find_element(*self.SUBSCRIBE_BUTTON_XPATH)

    def subscription_success(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE_ID)

    def get_subscription(self):
        return self.driver.find_element(*self.SUBSCRIPTION)

    def get_title(self):
        return self.driver.title

    # Methods
    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        new_path = os.path.join(screenshot_folder, filename)
        os.rename(filename, new_path)
        time.sleep(2)

    def scroll_to_bottom_of_page(self):
        self.driver.find_element(*self.BODY_TAG_NAME).send_keys(Keys.END)
        time.sleep(2)

    def email_subscription_field(self, UserEmail):
        self.get_email().send_keys(UserEmail)
        logger.info(f'Email: {UserEmail}')

    def subscribe_btn(self):
        home_subscribe = self.get_btn_subscribe()
        home_subscribe.click()
        time.sleep(5)

    def click_cart_btn(self):
        cart_subscribe = self.get_cart()
        cart_subscribe.click()

    def view_subscription_msg(self):
        subscription = self.get_subscription().text
        return subscription

    def view_success_msg(self):
        success_msg = self.get_success_msg().text
        return success_msg

    def verify_subscription_success(self):
        try:
            success_message = self.get_success_msg()
            assert success_message.text == "You have been successfully subscribed!"
            logger.info(success_message.text)
        except TimeoutException:
            logger.error("Subscription success message was not found.")
            raise
