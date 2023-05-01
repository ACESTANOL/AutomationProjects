from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddProducts:

    # Locators
    products_button = By.XPATH, "//a[@href='/products']"
    first_product = By.XPATH, "//div[@class='features_items']//div[2]//div[1]//div[1]//div[2]//div[1]//a[1]"
    second_product = By.CSS_SELECTOR, "a[data-id-product='2']"
    view_cart_button = By.XPATH, "//a[normalize-space()='Cart']"


def test_tc12_add_products_to_cart(browser):
    # Step 1: Launch browser
    browser.maximize_window()

    # Step 2: Navigate to url 'http://automationexercise.com'
    browser.get('http://automationexercise.com')

    # Step 3: Verify that home page is visible successfully
    assert 'Automation Exercise' in browser.title

    # Step 4: Click 'Products' button

    products_button.click()

    # Step 5: Hover over first product and click 'Add to cart'
    first_product = browser.find_element(By.XPATH, "//div[@class='features_items']//div[2]//div[1]//div[1]//div[2]//div[1]//a[1]")
    actions = ActionChains(browser)
    actions.move_to_element(first_product).perform()
    add_to_cart_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='features_items']//div[2]//div[1]//div[1]//div[2]//div[1]//a[1]'][data-button-action='add-to-cart']"))
    )
    add_to_cart_button.click()

    # Step 6: Click 'Continue Shopping' button
    continue_shopping_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue Shopping']"))
    )
    continue_shopping_button.click()

    # Step 7: Hover over second product and click 'Add to cart'
    second_product = browser.find_element_by_css_selector("a[data-id-product='2']")
    actions.move_to_element(second_product).perform()
    add_to_cart_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-id-product='2'][data-button-action='add-to-cart']"))
    )
    add_to_cart_button.click()

    # Step 8: Click 'View Cart' button

    view_cart_button.click()

    # Step 9: Verify both products are added to Cart
    product_rows = browser.find_elements_by_css_selector(".cart_item")
    assert len(product_rows) == 2

    # Step 10: Verify their prices, quantity and total price
    product_1_price = float(product_rows[0].find_element_by_css_selector(".cart_unit .price").text.replace('$', ''))
    product_1_quantity = int(
        product_rows[0].find_element_by_css_selector(".cart_quantity_input").get_attribute('value'))
    product_2_price = float(product_rows[1].find_element_by_css_selector(".cart_unit .price").text.replace('$', ''))
    product_2_quantity = int(
        product_rows[1].find_element_by_css_selector(".cart_quantity_input").get_attribute('value'))

    assert product_1_price * product_1_quantity + product_2_price * product_2_quantity == float(
        browser.find_element_by_css_selector(".cart_total_price .price").text.replace('$', ''))
