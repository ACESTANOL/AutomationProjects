from Pages.Sign_up_page import SigUpPage
from Utilities.config import *
from Utilities.common import *
import pytest
import json
import time
import os
from selenium.common.exceptions import TimeoutException

# Load user credentials from JSON file
with open("C:\\Users\\Angelica\\PycharmProjects\\AutomationExercises\\Utilities\\testdata.json") as f:
    credentials = json.load(f)

logger = LogFunc().get_log()


def test_register_user(browser):
    sign_up = SigUpPage(browser)
    browser.get(login_url)
    browser.maximize_window()

    if sign_up.is_loaded():
        print("Login page loaded successfully")
    else:
        print("Failed to load login page")
    logger.info("----------------------------------")

    name, email = credentials['signup']['name'], credentials['signup']['email']

    sign_up.username_entry(name)
    sign_up.email_signup_entry(email)
    sign_up.click_signup_button()

    ss_name = os.path.join(screenshot_folder, timestamp + '_ss_signup.png')
    sign_up.take_screenshot(ss_name)
    time.sleep(1)

    assert sign_up.get_title() == 'Automation Exercise - Signup'
    logger.info('success')

    (
        password,
        firstname,
        lastname,
        company,
        add1,
        add2,
        state,
        city,
        zipcode,
        mobile
    ) = credentials['account_info'].values()

    # Test data
    sign_up.title_radio()
    sign_up.dd_day("20")
    sign_up.dd_month("9")
    sign_up.dd_year("1988")
    sign_up.chk_newsletter()
    sign_up.first_name(firstname)
    sign_up.new_password(password)
    sign_up.last_name(lastname)
    sign_up.company(company)
    sign_up.add1(add1)
    sign_up.add2(add2)
    sign_up.dd_country("Israel")
    sign_up.state(state)
    sign_up.city(city)
    sign_up.zipcode(zipcode)
    sign_up.mobile_number(mobile)

    ss_name = os.path.join(screenshot_folder, timestamp + '_ss_signup.png')
    sign_up.take_screenshot(ss_name)
    time.sleep(1)

    # Created account
    sign_up.click_create_account()
    logger.info('Account successfully created')

    # Take screenshot of signup page
    ss_name = os.path.join(screenshot_folder, timestamp + '_ss_signup.png')
    sign_up.take_screenshot(ss_name)
    time.sleep(3)

    # Check if account was created
    sign_up.click_cont_btn()
    assert sign_up.get_title() == 'Automation Exercise - Account Created'
    time.sleep(1)

    # Check if user is back on the main page
    assert sign_up.get_title() == 'Automation Exercise'

    # Delete user account
    sign_up.click_account_deleted()
    time.sleep(1)

    ss_name = os.path.join(screenshot_folder, timestamp + '_ss_deleted.png')
    sign_up.take_screenshot(ss_name)

    assert sign_up.get_title() == 'Automation Exercise - Account Created', "Account was not deleted successfully"

    sign_up.deleted_account_btn()
    logger.info('Account successfully deleted')
    assert sign_up.get_title() == 'Automation Exercise - Account Created', "Account was not created successfully"

    ''' try:
           alert = browser.switch_to.alert
           alert.accept()
           logger.info('Alert accepted')
       except TimeoutException:
           logger.info('No alert found')'''
