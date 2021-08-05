import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = None


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='headless_chrome')


@pytest.fixture(scope='class')
def setup(request):
    # log file for chrome driver
    logger = ["--verbose", "--log-path=/Users/ajaysagar/ocean/SelPyFrame/chromedriver.log"]
    url = "https://rahulshettyacademy.com/angularpractice"
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        driver = webdriver.Chrome('/usr/local/share/chromedriver', service_args=logger)
    elif browser_name == 'headless_chrome':
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--start-maximized")  # maximized mode
        # chrome_options.add_argument("--ignore-certificate-errors")  # ignoring certificate errors
        driver = webdriver.Chrome('/usr/local/share/chromedriver', service_args=logger, options=chrome_options)
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()

    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
