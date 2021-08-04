import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='headless_chrome')


@pytest.fixture(scope='class')
def setup(request):
    # log file for chrome driver
    logger = ["--verbose", "--log-path=/Users/ajaysagar/ocean/SelPyFrame/chromedriver.log"]
    url = "https://rahulshettyacademy.com/angularpractice"
    driver = ''
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
