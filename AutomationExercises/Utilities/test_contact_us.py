import json
import os
import time
from Pages.contact_page import ContactUs, UploadFile
from Utilities.common import LogFunc
from Utilities.config import *


logger = LogFunc().get_log()

# Load user credentials from JSON file
with open("C:\\Users\\Angelica\\PycharmProjects\\AutomationExercises\\Utilities\\testdata.json") as f:
    credentials = json.load(f)

# For file uploading
filepath = os.path.join(os.getcwd(), "screenshot", "sample.png")


def test_tc6_contact_us(browser):
    # 1 & 2
    contact_us = ContactUs(browser)
    browser.get(home_url)
    browser.maximize_window()

    # 3 (Verify that home page is visible successfully)
    assert contact_us.get_title() == 'Automation Exercise'

    # 4 (Click on 'Contact Us' button
    contact_us.click_contact_us()

    # 5 (Verify 'GET IN TOUCH' is visible)
    expected_message = 'GET IN TOUCH'
    assert contact_us.view_get_exist_msg() == expected_message, f"Expected: {expected_message}. Got: {get_intouch}"

    # 6 (Enter name, email, subject and message)

    name, email, subject, message = credentials['contact_us'].values()
    contact_us.fill_contact_form(name, email, subject, message)
    time.sleep(5)
    ss_name = os.path.join(screenshot_folder, f"{timestamp}_ss_contact_us.png")
    contact_us.take_screenshot(ss_name)

    # 7 - 10 (Upload file)
    test_upload_file()


def test_upload_file(browser):
    file_upload = UploadFile(browser)
    browser.maximize_window()

    file_upload.click_contact_us()

    # Upload file
    file_upload.upload_file(filepath)

    # Click the upload button
    file_upload.click_upload_button()

    # Assert file uploaded text
    assert file_upload.get_file_uploaded_text() == "sample.png", "Failed to upload the file"

    # Submit the form
    file_upload.click_submit_btn()

    # 11 (Click 'Home' button and verify that landed to home page successfully)


