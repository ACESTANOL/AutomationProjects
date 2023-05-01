from Pages.register_user_page import SigUpPage
from Pages.login_page import LoginPage
from Utilities.config import *
from Utilities.common import *
import json
import time
import os
import pytest


# Load user credentials from JSON file
with open("C:\\Users\\Angelica\\PycharmProjects\\AutomationExercises\\Utilities\\testdata.json") as f:
    credentials = json.load(f)

logger = LogFunc().get_log()


def registered_user_name():
    name = credentials['signup']['name']
    return name


def enter_login_credentials(name, email, browser):
    login = SigUpPage(browser)
    login.username_entry(name)
    login.email_signup_entry(email)


def test_tc1_register_user(browser):
    # 1 & 2
    sign_up = SigUpPage(browser)
    browser.get(home_url)
    browser.maximize_window()
    # 3 ( Verify that home page is visible successfully)
    assert sign_up.get_title() == 'Automation Exercise'
    # 4 ( Click on 'Signup / Login' button)
    sign_up.click_login()
    # 5 (Verify 'New User Signup!' is visible)
    assert sign_up.get_title() == 'Automation Exercise - Signup / Login'
    # 6 (Enter name and email address)
    name, email = credentials['signup']['name'], credentials['signup']['email']
    enter_login_credentials(name, email, browser)
    # 7 (Click 'Signup' button)
    sign_up.click_signup_button()
    ss_name = os.path.join(screenshot_folder, timestamp + '_ss_signup.png')
    sign_up.take_screenshot(ss_name)
    time.sleep(1)
    # 8 (Verify that 'ENTER ACCOUNT INFORMATION' is visible)
    assert sign_up.get_title() == 'Automation Exercise - Signup'
    # 9 (Fill details: Title, Name, Email, Password, Date of birth)
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
    # 10 (Select checkbox 'Sign up for our newsletter!')
    sign_up.chk_newsletter()
    # 11 ( Select checkbox 'Receive special offers from our partners!')
    sign_up.chk_promotions_chk()
    # 12 (Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number)
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
    # 13  (Click 'Create Account button')
    sign_up.click_create_account()
    logger.info('Account successfully created')
    # Take screenshot of signup page
    ss_name = os.path.join(screenshot_folder, timestamp + '_ss_signup.png')
    sign_up.take_screenshot(ss_name)
    time.sleep(3)
    # 14 (Verify that 'ACCOUNT CREATED!' is visible)
    assert sign_up.get_title() == 'Automation Exercise - Account Created'
    time.sleep(1)
    # 15 (Click 'Continue' button)
    sign_up.click_cont_btn()
    # 16 ( Verify that 'Logged in as username' is visible)
    sign_up.view_login_msg()
    # 17 (Click 'Delete Account' button)
    sign_up.click_account_deleted()
    # 18 (Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button)
    expected_message = 'ACCOUNT DELETED!'
    assert sign_up.view_delete_msg() == expected_message, f"Expected: {expected_message}. Got: {delete_msg}"
    logger.info('Account successfully deleted')
    time.sleep(1)
    ss_name = os.path.join(screenshot_folder, timestamp + '_ss_deleted.png')
    sign_up.take_screenshot(ss_name)


def test_tc2_valid_login(browser):
    # Step 1 & 2
    login = LoginPage(browser)
    browser.get(home_url)
    browser.maximize_window()
    # step 3 ( Verify that home page is visible successfully)
    assert login.get_title() == 'Automation Exercise'
    # 4 (Click on 'Signup / Login' button)
    login.click_login()
    # 5 (Verify 'Login to your account' is visible)
    login.view_login_msg()
    # 6 (Enter correct email address and password)
    username, password = credentials['valid']['user'], credentials['valid']['pwd']
    login.username_entry(username)
    login.password_entry(password)
    # 7 (Click 'login' button)
    login.click_login_button()
    # 8 (Verify that 'Logged in as username' is visible)
    login.view_login_msg()
    # 9 (Click 'Delete Account' button)
    login.click_deleted()
    time.sleep(1)
    ss_name = os.path.join(screenshot_folder, timestamp + '_ss_deleted.png')
    login.take_screenshot(ss_name)
    # 10 (Verify that 'ACCOUNT DELETED!' is visible
    expected_message = 'ACCOUNT DELETED!'
    assert login.view_delete_msg == expected_message, f"Expected: {expected_message}. Got: {delete_msg}"
    logger.info('Account successfully deleted')


def test_tc3_invalid_login(browser):
    # Step 1 & 2
    login = LoginPage(browser)
    browser.get(home_url)
    browser.maximize_window()
    # step 3 ( Verify that home page is visible successfully)
    assert login.get_title() == 'Automation Exercise'
    # 4 (Click on 'Signup / Login' button)
    login.click_login()
    # 5 (Verify 'Login to your account' is visible)
    login.view_login_msg()
    # 6 (Enter incorrect email address and password)
    username, password = credentials['invalid']['user'], credentials['invalid']['pwd']
    login.username_entry(username)
    login.password_entry(password)
    # 7 & 8 (click and  Verify error 'Your email or password is incorrect!' is visible)
    login.click_login_button()
    time.sleep(1)
    expected_message = 'Your email or password is incorrect!'
    assert login.click_button_invalid_login() == expected_message, f"Expected: {expected_message}. Got: {invalid_login}"


def test_tc4_logout(browser):
    # Step 1 & 2
    login = LoginPage(browser)
    browser.get(home_url)
    browser.maximize_window()
    # step 3 ( Verify that home page is visible successfully)
    assert login.get_title() == 'Automation Exercise'
    # 4 (Click on 'Signup / Login' button)
    login.click_login()
    # 5 (Verify 'Login to your account' is visible)
    login.view_login_msg()
    # 6 (Enter correct email address and password)
    username, password = credentials['valid']['user'], credentials['valid']['pwd']
    login.username_entry(username)
    login.password_entry(password)
    # 7 (Click 'login' button)
    login.click_login_button()
    # 8 ( Verify that 'Logged in as username' is visible)
    # 9 ( Click 'Logout' button)
    login.get_logout()
    # 10 (Verify that user is navigated to login page)
    login.view_login_msg()


def test_tc5_existing_email(browser):
    # Step 1 & 2
    sign_up = SigUpPage(browser)
    browser.get(home_url)
    browser.maximize_window()
    # step 3 ( Verify that home page is visible successfully)
    assert sign_up.get_title() == 'Automation Exercise'
    # 4 (Click on 'Signup / Login' button)
    sign_up.click_login()
    # 5 (Verify 'New User Signup!' is visible)
    expected_message = 'New User Signup!'
    assert sign_up.view_new_user_signup_msg() == expected_message, f"Expected: {expected_message}. Got: {new_user}"

    # 6 (Enter name and already registered email address)
    name, email = credentials['signup']['name'], credentials['email']['email']
    sign_up.username_entry(name)
    sign_up.password_entry(email)
    # 7 (Click 'Signup' button)
    sign_up.click_signup_button()
    # 8 (Verify error 'Email Address already exist!' is visible)
    expected_message = 'Login to your account'
    assert sign_up.view_email_exist_msg() == expected_message, f"Expected: {expected_message}. Got: {email_exist}"

    ''' try:
           alert = browser.switch_to.alert
           alert.accept()
           logger.info('Alert accepted')
       except TimeoutException:
           logger.info('No alert found')'''
