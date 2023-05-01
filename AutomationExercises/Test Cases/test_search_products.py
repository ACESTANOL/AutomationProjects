import os
import time

import pytest
import json
from selenium import webdriver
from Pages.search_product_page import SearchProducts
from Utilities.common import LogFunc
from Utilities.config import *

logger = LogFunc().get_log()

with open("C:\\Users\\Angelica\\PycharmProjects\\AutomationExercises\\Utilities\\testdata.json") as f:
    credentials = json.load(f)


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_tc9_search_products(browser):
    # 1 & 2
    search_products = SearchProducts(browser)
    browser.get(home_url)
    browser.maximize_window()
    # 3
    assert search_products.get_title() == 'Automation Exercise'
    # 4
    search_products.click_products()
    browser.refresh()
    # 5
    # assert search_products.click_all_products() == 'ALL PRODUCTS'
    # 6
    search = credentials['search_products']['search']
    search_products.input_products(search)
    expected_result = [search]
    print(f"Expected result: {expected_result}")
    search_products.click_search_btn()
    # 7
    assert search_products.get_search_products_msg() == 'SEARCHED PRODUCTS'
    browser.refresh()
    # 8
    #  featured_items = search_products.get_featured_items()
    #  print(f"Featured items: {featured_items}")
    #  assert all(item in [elem.text for elem in featured_items] for item in expected_result)




''' try:
        browser.get(home_url)
        browser.maximize_window()
        search_products.click_all_products()
        logger.info("----------------------------------")
        search = credentials['search_products']['search']
        search_products.input_products(search)

        search_products.click_search_btn()

        ss_name = os.path.join(screenshot_folder, timestamp + '_ss_search_products.png')
        search_products.take_screenshot(ss_name)
        browser.refresh()
        assert search_products.get_title() == expected_title
    except Exception as e:
        logger.error(f'Test case page failed: {str(e)}')
        raise e
    finally:
        browser.quit()

    logger.info(f'Test case page passed: expected title - {expected_title}, actual title - {search_products.get_title()}')'''






























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































