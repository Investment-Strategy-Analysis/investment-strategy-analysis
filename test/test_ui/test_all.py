from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromiumOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
# from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.chrome.service import Service as СhromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager

from test.test_ui.signup_test import SignUpTests
from test.test_ui.login_test import LogInTests


def run_tests_in_browser(_driver):
    print(f'Starting tests for {_driver.name}...')
    SignUpTests(_driver)
    LogInTests(_driver)
    print('All tests passed')
    print('===')
    _driver.close()


def test_ui():
    options = [
        "--headless",
        "--no-sandbox",
        "--disable-dev-shm-usage",
    ]
    drivers = [
        # (webdriver.Chrome, СhromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), ChromiumOptions()),
        # (webdriver.ChromiumEdge, EdgeService(EdgeChromiumDriverManager().install()), EdgeOptions()),
        (webdriver.Firefox, FirefoxService(GeckoDriverManager().install()), FirefoxOptions()),
        # (webdriver.Safari, None, SafariOptions()),
    ]

    for (web_driver, service, driver_options) in drivers:
        driver_options.add_argument("--headless")
        driver_options.add_argument("--no-sandbox")
        driver_options.add_argument("--disable-dev-shm-usage")
        if service is None:
            _driver = web_driver(options=driver_options)
        else:
            _driver = web_driver(service=service, options=driver_options)
        run_tests_in_browser(_driver)

    # driver_options = OperaOptions()
    # driver_options.add_argument("--headless")
    # driver_options.add_argument("--no-sandbox")
    # driver_options.add_argument("--disable-dev-shm-usage")
    # driver = webdriver.Opera(executable_path=OperaDriverManager().install(), options=driver_options)
    # print('Starting tests for Opera...')
    # SignUpTests(driver)
    # print('All tests passed')
    # print('===')
    # driver.close()

