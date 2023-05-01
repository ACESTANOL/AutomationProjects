from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Utilities.config import *
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from Utilities.common import LogFunc
import os
import time

logger = LogFunc().get_log()


class SigUpPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators
    # Home page
    SIGNUP_LOGIN = (By.XPATH, "//a[normalize-space()='Signup / Login']")

    # Signup page
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BTN = (By.XPATH, "//button[normalize-space()='Signup']")
    NEW_USER_SIGNUP = (By.XPATH, "//h2[normalize-space()='New User Signup!']")

    # Account info page
    TITLE1 = (By.ID, "id_gender1")
    TITLE2 = (By.ID, "id_gender2")
    FIRST_NAME_INPUT = (By.ID, "first_name")
    LAST_NAME_INPUT = (By.ID, "last_name")
    COMPANY_INPUT = (By.ID, "company")
    PASSWORD_INPUT = (By.ID, "password")
    DOB_MONTH_DROPDOWN = (By.ID, "months")
    DOB_DAY_DROPDOWN = (By.ID, "days")
    DOB_YEAR_DROPDOWN = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.XPATH, "//input[@id='newsletter']")
    SPECIAL_OFFERS_CHECKBOX = (By.XPATH, "//input[@id='optin']")
    ADDRESS1_INPUT = (By.ID, "address1")
    ADDRESS2_INPUT = (By.ID, "address2")
    COUNTRY_DROPDOWN = (By.ID, "country")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    ZIPCODE_INPUT = (By.ID, "zipcode")
    MOBILE_INPUT = (By.ID, "mobile_number")
    CREATE_ACCT_BTN = (By.XPATH, "//button[normalize-space()='Create Account']")
    CONT_BTN = (By.XPATH, "//a[normalize-space()='Continue']")

    # Account created page
    SIGN_UP_BTN = (By.XPATH, "//a[normalize-space()='Signup / Login']")
    ACCOUNT_CREATED_BTN = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    CONTINUE_BTN = (By.XPATH, "//a[normalize-space()='Continue']")
    CONT_DELETED_BTN = (By.XPATH, "//a[normalize-space()='Continue']")
    EMAIL_EXIST = (By.XPATH, "//p[normalize-space()='Email Address already exist!']")

    # My account page
    LOGGED_IN_AS_MSG = (By.XPATH, "//p[contains(text(), 'Logged in as ')]")
    DELETE_ACCT_BTN = (By.XPATH, "//a[normalize-space()='Delete Account']")

    # Account deleted page
    ACCOUNT_DELETED_MSG = (By.XPATH, "//h1[contains(text(), 'ACCOUNT DELETED!')]")
    ACCOUNT_CREATED_MSG = (By.XPATH, "//a[normalize-space()='Signup / Login']")

    # Elements
    def is_loaded(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIGNUP_BTN))
            return True
        except TimeoutException:
            return False

    def title_drp1(self):
        return self.wait.until(EC.element_to_be_clickable(self.TITLE1))

    def title_drp2(self):
        return self.wait.until(EC.element_to_be_clickable(self.TITLE2))

    def enter_name(self):
        return self.driver.find_element(*self.NAME_INPUT)

    def enter_email(self):
        return self.driver.find_element(*self.EMAIL_INPUT)

    def click_signup(self):
        return self.driver.find_element(*self.SIGNUP_BTN)

    def enter_password(self):
        return self.driver.find_element(*self.PASSWORD_INPUT)

    def drp_day(self):
        return self.wait.until(EC.element_to_be_clickable(self.DOB_DAY_DROPDOWN))

    def drp_month(self):
        return self.wait.until(EC.element_to_be_clickable(self.DOB_MONTH_DROPDOWN))

    def drp_year(self):
        return self.wait.until(EC.element_to_be_clickable(self.DOB_YEAR_DROPDOWN))

    # def newsletter_chk(self):
       # return self.wait.until(EC.element_to_be_clickable(self.NEWSLETTER_CHECKBOX))

    # def offers_chk(self):
       # return self.wait.until(EC.element_to_be_clickable(self.SPECIAL_OFFERS_CHECKBOX))

    def f_name(self):
        return self.driver.find_element(*self.FIRST_NAME_INPUT)

    def l_name(self):
        return self.driver.find_element(*self.LAST_NAME_INPUT)

    def get_company(self):
        return self.driver.find_element(*self.COMPANY_INPUT)

    def address1(self):
        return self.driver.find_element(*self.ADDRESS1_INPUT)

    def address2(self):
        return self.driver.find_element(*self.ADDRESS2_INPUT)

    def drp_country(self):
        return self.wait.until(EC.element_to_be_clickable(self.COUNTRY_DROPDOWN))

    def get_state(self):
        return self.driver.find_element(*self.STATE_INPUT)

    def get_city(self):
        return self.driver.find_element(*self.CITY_INPUT)

    def get_zipcode(self):
        return self.driver.find_element(*self.ZIPCODE_INPUT)

    def mobile(self):
        return self.driver.find_element(*self.MOBILE_INPUT)

    def get_signup(self):
        return self.driver.find_element(*self.SIGN_UP_BTN)

    def create_account(self):
        return self.wait.until(EC.element_to_be_clickable(self.ACCOUNT_CREATED_BTN))

    def cont_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN))

    def deleted_account(self):
        return self.wait.until(EC.element_to_be_clickable(self.DELETE_ACCT_BTN))

    def deleted_account_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.CONT_DELETED_BTN))

    def get_email_exist_msg(self):
        return self.driver.find_element(*self.EMAIL_EXIST)

    def get_new_user_signup(self):
        return self.driver.find_element(*self.NEW_USER_SIGNUP)

    def get_title(self):
        return self.driver.title

    # Methods
    def username_entry(self, nameEntry):
        self.enter_name().send_keys(nameEntry)
        logger.info(f'UserName: {nameEntry}')

    def email_signup_entry(self, userEmail):
        self.enter_email().send_keys(userEmail)
        logger.info(f'UserEmail: {userEmail}')

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        new_path = os.path.join(screenshot_folder, filename)
        os.rename(filename, new_path)
        time.sleep(2)

    def click_signup_button(self):
        sign_up = self.click_signup()
        sign_up.click()

    # Fill up information
    def title_radio(self, select=True):
        try:
            title_chk = self.title_drp2()
        except TimeoutException:
            print(f"Radio button not clickable within timeout")
            return
        except NoSuchElementException:
            print(f"Radio button not found")
            return

        if select:
            if not title_chk.is_selected():
                title_chk.click()
        else:
            if title_chk.is_selected():
                title_chk.click()

    def new_password(self, userPass):
        self.enter_password().send_keys(userPass)

    def dd_day(self, value):
        day_dropdown = self.drp_day()
        day_select = Select(day_dropdown)
        day_select.select_by_value(value)

    def dd_month(self, value):
        month_dropdown = self.drp_month()
        month_select = Select(month_dropdown)
        month_select.select_by_value(value)

    def dd_year(self, value):
        year_dropdown = self.drp_year()
        year_select = Select(year_dropdown)
        year_select.select_by_value(value)

    def chk_newsletter(self, select=True):
        newsletter_chk = self.driver.find_element(*self.NEWSLETTER_CHECKBOX)
        promotions_chk = self.driver.find_element(*self.SPECIAL_OFFERS_CHECKBOX)
        if select:
            if not newsletter_chk.is_selected():
                newsletter_chk.click()
            # If the newsletter checkbox is already checked, uncheck it and check the promotions checkbox
            else:
                newsletter_chk.click()
                promotions_chk.click()
        # Uncheck the newsletter checkbox
        else:
            if newsletter_chk.is_selected():
                newsletter_chk.click()

    def dd_country(self, value):
        country_dropdown = self.drp_country()
        country_select = Select(country_dropdown)
        country_select.select_by_value(value)

    def first_name(self, userfname):
        self.f_name().send_keys(userfname)

    def last_name(self, userlname):
        self.l_name().send_keys(userlname)

    def company(self, usercompany):
        self.get_company().send_keys(usercompany)

    def add1(self, useradd1):
        self.address1().send_keys(useradd1)

    def add2(self, useradd2):
        self.address2().send_keys(useradd2)

    def state(self, userstate):
        self.get_state().send_keys(userstate)

    def city(self, usercity):
        self.get_city().send_keys(usercity)

    def zipcode(self, userzip):
        self.get_zipcode().send_keys(userzip)

    def mobile_number(self, usermobile):
        self.mobile().send_keys(usermobile)

    def click_login(self):
        log_in = self.get_signup()
        log_in.click()

    def click_create_account(self):
        sign_up = self.create_account()
        sign_up.click()

    def click_cont_btn(self):
        sign_up = self.cont_btn()
        sign_up.click()

    def click_account_deleted(self):
        sign_up = self.deleted_account()
        sign_up.click()

    def view_email_exist_msg(self):
        email_exist = self.get_email_exist_msg().text
        return email_exist

    def view_delete_msg(self):
        delete_msg = self.get_deleted_msg().text
        return delete_msg

    def view_new_user_signup_msg(self):
        new_user = self.get_new_user_signup().text
        return new_user






























