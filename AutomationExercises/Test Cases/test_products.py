import os
import time
import pytest
from selenium import webdriver
from Pages.products_page import AllProducts
from Utilities.common import LogFunc
from Utilities.config import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException

logger = LogFunc().get_log()


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_tc8_all_products_page(browser):
    products_page = AllProducts(browser)

    # 1 & 2
    browser.get(home_url)
    browser.maximize_window()
    logger.info("----------------------------------")
    # 3
    assert products_page.get_title() == 'Automation Exercise'
    # 4
    products_page.click_all_products()
    ss_name = os.path.join(screenshot_folder, timestamp + '_ss_all_products.png')
    products_page.take_screenshot(ss_name)
    # 5
    assert products_page.get_all_products_msg() == 'All Products'
    # 6
    assert len(products_page.PRODUCT_LIST) > 0
    time.sleep(5)
    # 7
    while True:
        try:
            view_button = products_page.get_view_products()
            print(view_button)
            ActionChains(browser).move_to_element(view_button).click().perform()
            break
        except ElementClickInterceptedException:
            browser.refresh()
    # 8
    #  assert products_page.get_title() == 'Automation Exercise - Product Details'
    # 9
    # assert all(e.is_displayed() for e in [products_page.get_product_name(),
                                         # products_page.get_category(),
                                         # products_page.get_price(),
                                         # products_page.get_availability(),
                                         # products_page.get_condition(),
                                         # products_page.get_brand()])




'''def test_all_products_page_error(browser):
    products = AllProducts(browser)
    expected_title = 'Automation Exercise - All Products'

    browser.get(home_url)
    browser.maximize_window()
    logger.info("----------------------------------")

    products.click_all_products()
    ss_name = os.path.join(screenshot_folder, timestamp + '_ss_all_products.png')
    products.take_screenshot(ss_name)

    browser.refresh()
    actual_title = products.get_title()

    if actual_title != expected_title:
        logger.error(f'Test case page failed: expected title - {expected_title}, actual title - {actual_title}')
        pytest.fail(f'Test case page failed: expected title - {expected_title}, actual title - {actual_title}')

    logger.info(f'Test case page passed: expected title - {expected_title}, actual title - {actual_title}')'''
