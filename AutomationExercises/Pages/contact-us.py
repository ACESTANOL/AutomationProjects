from selenium.webdriver.common.by import By
from Utilities.common import LogFunc
from selenium.webdriver.support.ui import Select
from Utilities.config import file_path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


logger = LogFunc().get_log()


class ContactUsForm:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    CONTACT_US = (By.XPATH, "//a[normalize-space()='Contact us']")
    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.NAME, "email")
    SUBJECT_FIELD = (By.NAME, "subject")
    MESSAGE_FIELD = (By.ID, "message")
    UPLOAD_BTN = (By.XPATH, "//input[@name='upload_file']")
    SUBMIT_BTN = (By.XPATH, "//input[@name='submit']")
    HOME_BTN = (By.XPATH, "//span[normalize-space()='Home']")
    CONFIRMATION_MESSAGE = (By.XPATH, "//div[@class='status alert alert-success']")

    # Elements
    def get_name_field(self):
        return self.driver.find_element(*self.NAME_FIELD)

    def get_email_field(self):
        return self.driver.find_element(*self.EMAIL_FIELD)

    def get_subject_field(self):
        return Select(self.driver.find_element(*self.SUBJECT_FIELD))

    def get_message_field(self):
        return self.driver.find_element(*self.MESSAGE_FIELD)

    def get_submit_button(self):
        return self.driver.find_element(*self.SUBMIT_BTN)

    def get_upload_btn(self):
        return self.driver.find_element(*self.UPLOAD_BTN)

    def get_home_btn(self):
        return self.driver.find_element(*self.HOME_BTN)

    def confirmation_message(self):
        return self.driver.find_element(*self.CONFIRMATION_MESSAGE)

    # Methods
    def name_entry(self):
        self.get_name_field().send_keys("Angelica")

    def email_entry(self):
        self.get_email_field().send_keys("acestanol@gmail.com")

    def subject_entry(self):
        self.get_subject_field().send_keys("This is test subject")

    def message_entry(self):
        self.get_message_field().send_keys("This is test message")

    def upload_file(self, locator, file_path):
        element = locator.locate(self.driver)
        element.send_keys(file_path)

    def click_submit_btn(self):
        contact = self.get_submit_button()
        contact.click()













