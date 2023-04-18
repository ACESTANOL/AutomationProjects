from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Utilities.common import LogFunc
from Utilities.data import *
from Utilities.config import *
import os
import time
import datetime


logger = LogFunc().get_log()


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # #LOCATORS##
    # Login Info
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")
    INVALID_LOGIN = (By.XPATH, "//p[normalize-space()='Your email or password is incorrect!']")
    # Sign up Info
    NAME_INPUT = (By.NAME, "name")
    EMAIL_SIGNUP_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[text()='Signup']")
    LOGIN_PAGE = (By.XPATH, "//a[normalize-space()='Signup / Login']")
    # Delete Account
    CREATE_ACCT_BTN = (By.XPATH, "//button[normalize-space()='Create Account']")
    CONT_BTN = (By.XPATH, "//a[normalize-space()='Continue']")

    LOGOUT = (By.XPATH, "//a[normalize-space()='Logout']")

    # #ELEMENTS##
    # Login user with waiting of loading page
    def is_loaded(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_BUTTON))
            return True
        except TimeoutException:
            return False

    def enter_email(self):
        return self.driver.find_element(*self.EMAIL_INPUT)

    def enter_password(self):
        return self.driver.find_element(*self.PASSWORD_INPUT)

    def click_login(self):
        return self.driver.find_element(*self.LOGIN_BUTTON)

    def enter_name(self):
        return self.driver.find_element(*self.NAME_INPUT)

    def email_signup(self):
        return self.driver.find_element(*self.EMAIL_SIGNUP_INPUT)

    def get_invalid_login(self):
        return self.driver.find_element(*self.INVALID_LOGIN)

    def deleted_account(self):
        return self.wait.until(EC.element_to_be_clickable(self.DELETE_ACCT_BTN))

    def deleted_account_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.CONT_DELETED_BTN))

    def get_logout(self):
        return self.driver.find_element(*self.LOGOUT)

    def get_title(self):
        return self.driver.title

    # #METHODS##
    # User Login Entry
    def username_entry(self, userEntry):
        self.enter_email().send_keys(userEntry)
        logger.info(f'Username: {userEntry}')

    def password_entry(self, userPass):
        self.enter_password().send_keys(userPass)
        logger.info(f'Userpass: {userPass}')

    def name_entry(self, nameEntry):
        self.enter_name().send_keys(nameEntry)

    def email_signup_entry(self, userEmail):
        self.email_signup().send_keys(userEmail)

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        new_path = os.path.join(screenshot_folder, filename)
        os.rename(filename, new_path)
        time.sleep(2)

    def click_button_invalid_login(self):
        self.click_login()
        time.sleep(2)
        invalid_message = self.get_invalid_login().text
        expected_message = validation_login.get('Invalid')
        assert invalid_message == expected_message, f"Expected: {expected_message}. Got: {invalid_message}"
        logger.info('Invalid credentials')

    def click_login_button(self):
        login_button = self.click_login()
        login_button.click()

    def click_cont_btn(self):
        login = self.cont_btn()
        login.click()

    def click_account_deleted(self):
        login = self.deleted_account()
        login.click()

    def click_logout(self):
        login = self.get_logout()
        login.click()


