import time
import os
import json
from selenium import webdriver
import pytest
from Utilities.common import LogFunc
from Utilities.config import *
from Pages.verify_subscription_in_cart_page import SubscriptionCart

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


def test_tc11_home_subscription(browser):
    1 & 2
    expected_title = 'Automation Exercise'
    test_cart = SubscriptionCart(browser)
    browser.get(home_url)
    # 3
    assert test_cart.get_title() == expected_title
    # 4
    test_cart.click_cart_btn()
    # 5
    test_cart.scroll_to_bottom_of_page()
    # 6
    assert test_cart.view_subscription_msg() == 'SUBSCRIPTION'
    # 7
    logger.info("----------------------------------")
    email = credentials['signup']['email']
    test_cart.email_subscription_field(email)
    time.sleep(2)
    ss_name = os.path.join(screenshot_folder, timestamp + '_ss_cart_subscription.png')
    test_cart.take_screenshot(ss_name)
    test_cart.subscribe_btn()
    time.sleep(2)
    # 8
    # assert test_cart.get_success_msg() == 'You have been successfully subscribed!'
    # logger.info(test_cart.get_success_msg())
    # test_cart.driver.quit()


