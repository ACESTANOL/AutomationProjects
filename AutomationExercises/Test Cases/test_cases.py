import os
import pytest
from selenium import webdriver
from Pages.test_cases_page import TestCases
from Utilities.common import LogFunc
from Utilities.config import *

logger = LogFunc().get_log()


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_tc7_test_cases(browser):
    # 1 & 2
    test_page = TestCases(browser)
    browser.get(home_url)
    browser.maximize_window()
    # 2 (Verify that home page is visible successfully)
    expected_title = 'Automation Practice Website for UI Testing - Test Cases'
    logger.info("----------------------------------")
    # 4 (Click on 'Test Cases' button)
    test_page.click_test_cases()
    ss_name = os.path.join(screenshot_folder, timestamp + '_ss_test_page.png')
    test_page.take_screenshot(ss_name)
    browser.refresh()
    # 5 (Verify user is navigated to test cases page successfully)
    assert test_page.get_title() == expected_title


   # logger.info(f'Test case page passed: expected title - {expected_title}, actual title - {test_page.get_title()}')
