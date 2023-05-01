import json
import os
import time

import pytest

from Pages.login_page import LoginPage
from Utilities.common import LogFunc
from Utilities.config import *

logger = LogFunc().get_log()

# Load user credentials from JSON file
with open("C:\\Users\\Angelica\\PycharmProjects\\AutomationExercises\\Utilities\\testdata.json") as f:
    credentials = json.load(f)


@pytest.fixture
def test_login_with_invalid_credentials(browser):
    login_page = LoginPage(browser)
    browser.get(home_url)
    browser.maximize_window()

    if login_page.is_loaded():
        print("Login page loaded successfully")
    else:
        print("Failed to load login page")
    logger.info("----------------------------------")

    login_page.click_signup()

    # Retrieve user credentials from the JSON format
    username, password = credentials['invalid']['user'], credentials['invalid']['pwd']

    login_page.username_entry(username)
    login_page.password_entry(password)

    ss_name = os.path.join(screenshot_folder, timestamp + '_ss_dashboard.png')
    login_page.take_screenshot(ss_name)
    time.sleep(1)
    assert login_page.get_title() == 'Automation Exercise - Signup / Login'

    login_page.click_login_button()
    logger.info("Invalid Log in")
    ss_name = os.path.join(screenshot_folder, timestamp + '_ss_invalid_login.png')
    login_page.take_screenshot(ss_name)
    time.sleep(1)
