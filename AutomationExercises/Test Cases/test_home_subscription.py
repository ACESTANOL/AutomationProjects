import time
import os
import json
from selenium import webdriver
import pytest
from Utilities.common import LogFunc
from Utilities.config import *
from Pages.home_subscription_page import SubscriptionHome

logger = LogFunc().get_log()
with open("C:\\Users\\Angelica\\PycharmProjects\\AutomationExercises\\Utilities\\testdata.json") as f:
    credentials = json.load(f)


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.ChromeOptions()
    driver.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=driver)
    driver.implicitly_wait(2)
    yield driver
    driver.quit()


def test_tc10_home_subscription(browser):
    # 1 & 2
    expected_title = 'Automation Exercise'
    test_subscription = SubscriptionHome(browser)
    browser.get(home_url)
    # 3
    assert test_subscription.get_title() == expected_title
    logger.info("----------------------------------")
    # 4
    test_subscription.scroll_to_bottom_of_page()
    # 5
    assert test_subscription.view_subscription_msg() == 'SUBSCRIPTION'
    # 6
    email = credentials['signup']['email']
    test_subscription.email_subscription_field(email)
    test_subscription.subscribe_btn()
    time.sleep(2)
    ss_name = os.path.join(screenshot_folder, timestamp + '_ss_home_subscription.png')
    test_subscription.take_screenshot(ss_name)
    # 7
    assert test_subscription.get_title() == expected_title
    test_subscription.driver.quit()


