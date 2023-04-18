from Pages.login_page import LoginPage
from Utilities.common import LogFunc
from Utilities.config import *
from Utilities.conftest import browser
from selenium import webdriver
import time
import pytest
import json
import os


logger = LogFunc().get_log()

# Load user credentials from JSON file
with open("/Utilities/testdata.json") as f:
    credentials = json.load(f)


def test_login_success(browser):
    login_page = LoginPage(browser)
    browser.get(login_url)
    browser.maximize_window()

    if login_page.is_loaded():
        print("Login page loaded successfully")
    else:
        print("Failed to load login page")
    logger.info("----------------------------------")

    # Retrieve user credentials from the JSON format
    username, password = credentials['valid']['user'], credentials['valid']['pwd']

    login_page.username_entry(username)
    login_page.password_entry(password)
    login_page.take_screenshot("login_form.png")
    login_page.name_entry('Angel')
    login_page.email_signup_entry('angelestanol20@gmail.com')
    login_page.click_login_button()

    ss_name = os.path.join(screenshot_folder, timestamp + '_ss_dashboard.png')
    login_page.take_screenshot(ss_name)
    time.sleep(3)

    assert login_page.get_title() == 'Automation Exercise'
    logger.info('success')
