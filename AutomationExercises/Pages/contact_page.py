from selenium.webdriver.common.by import By
from Utilities.common import LogFunc
from Utilities.config import *
from seleniumbase import BaseCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time


logger = LogFunc().get_log()


class UploadFile(BaseCase):
    # Locators
    FILE_UPLOAD_INPUT = (By.XPATH, "//input[@name='upload_file']")
    FILE_SUBMIT_BTN = (By.XPATH, "//input[@name='submit']")
    FILE_UPLOADED_TEXT = (By.XPATH, "//div[@class='status alert alert-success']")
    TIMEOUT_VALUE = 15.
    HOME_BTN = (By.XPATH, "//span[normalize-space()='Home']")


class ContactUs:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    CONTACT_US = (By.XPATH, "//a[normalize-space()='Contact us']")
    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.NAME, "email")
    SUBJECT_FIELD = (By.XPATH, "//input[@placeholder='Subject']")
    MESSAGE_FIELD = (By.XPATH, "//textarea[@id='message']")
    UPLOAD_BTN = (By.XPATH, "//input[@name='upload_file']")
    SUBMIT_BTN = (By.XPATH, "//input[@name='submit']")
    HOME_BTN = (By.XPATH, "//span[normalize-space()='Home']")
    CONFIRMATION_MESSAGE = (By.XPATH, "//div[@class='status alert alert-success']")
    GET_IN_TOUCH_MSG = (By.XPATH, "//h2[normalize-space()='Get In Touch']")

    # Elements
    def get_name_field(self):
        return self.driver.find_element(*self.NAME_FIELD)

    def get_email_field(self):
        return self.driver.find_element(*self.EMAIL_FIELD)

    def get_subject_field(self):
        return self.driver.find_element(*self.SUBJECT_FIELD)

    def get_message_field(self):
        return self.driver.find_element(*self.MESSAGE_FIELD)

    def get_submit_button(self):
        return self.driver.find_element(*self.SUBMIT_BTN)

    def get_upload_input(self):
        return self.driver.find_element(*self.UPLOAD_BTN)

    def get_home_btn(self):
        return self.driver.find_element(*self.HOME_BTN)

    def confirmation_message(self):
        return self.driver.find_element(*self.CONFIRMATION_MESSAGE)

    def get_contact_us(self):
        return self.wait.until(EC.element_to_be_clickable(self.CONTACT_US))

    def get_intouch_msg(self):
        return self.driver.find_element(*self.GET_IN_TOUCH_MSG)

    def get_title(self):
        return self.driver.title

    # Methods

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        new_path = os.path.join(screenshot_folder, filename)
        os.rename(filename, new_path)
        time.sleep(2)

    def fill_contact_form(self, name, email, subject,  message):
        self.get_name_field().send_keys(name)
        logger.info(f'Name: {name}')
        self.get_email_field().send_keys(email)
        logger.info(f'Email: {email}')
        self.get_subject_field().send_keys(subject)
        logger.info(f'Subject: {subject}')
        self.get_message_field().send_keys(message)
        logger.info(f'Message: {message}')

    def click_contact_us(self):
        contact = self.get_contact_us()
        contact.click()

    def click_submit_btn(self):
        contact = self.get_submit_button()
        contact.click()

    def upload_file(self, filepath):
        self.choose_file(self.FILE_UPLOAD_INPUT, filepath)

    def click_upload_button(self):
        self.click(self.FILE_SUBMIT_BUTTON)

    def assert_file_uploaded_text(self):
        self.assert_text(self.FILE_UPLOADED_TEXT, timeout=self.TIMEOUT_VALUE)

    def view_get_exist_msg(self):
        get_intouch = self.get_intouch_msg().text
        return get_intouch







