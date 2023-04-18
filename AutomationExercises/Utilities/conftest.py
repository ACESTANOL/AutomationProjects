import pytest
from selenium import webdriver
import pytest_html


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


'''@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("https://automationexercise.com/login"))
        if report.failed:
            # add screenshot on failure
            browser = item.funcargs['browser']
            ss_name = f"{item.name}.png"
            browser.save_screenshot(ss_name)
            with open(ss_name, 'rb') as f:
                img_html = f"<div><img src='data:image/png;base64,{pytest_html.extras._make_inlined(f.read())}'/></div>"
                extras.append(pytest_html.extras.html(img_html))
        report.extras = extras'''

'''@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        report.extras = getattr(report, "extras", [])
        report.extras.append(pytest_html.extras.url("https://automationexercise.com/login"))
        if (report.skipped and hasattr(report, "wasxfail")) or (report.failed and not hasattr(report, "wasxfail")):
            report.extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))'''



'''
@pytest.fixture(params=['chrome', 'firefox', 'edge'])
def browser(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'edge':
        driver = webdriver.Edge()
    else:
        raise ValueError(f'Unsupported browser: {request.param}')
    yield driver
   driver.quit()
'''



