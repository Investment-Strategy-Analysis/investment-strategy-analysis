from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromiumOptions
from selenium.webdriver.chrome.service import Service as СhromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

from test.test_ui.login_test import LogInTests
from test.test_ui.signup_test import SignUpTests
from test.test_ui.help_test import HelpTests

if __name__ == '__main__':
    driver_options = ChromiumOptions()
    # driver_options.add_argument("--headless")
    driver_options.add_argument("--no-sandbox")
    driver_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=СhromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
                              options=driver_options)
    print('Starting tests for Chromium...')
    HelpTests(driver)
    SignUpTests(driver)
    LogInTests(driver)
    print('All tests passed')
    print('===')
    driver.close()

    # driver_options = EdgeOptions()
    # driver_options.add_argument("--headless")
    # driver_options.add_argument("--no-sandbox")
    # driver_options.add_argument("--disable-dev-shm-usage")
    # driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=driver_options)
    # print('Starting tests for Edge...')
    # SignUpTests(driver)
    # print('All tests passed')
    # print('===')
    # driver.close()

    # driver_options = FirefoxOptions()
    # driver_options.add_argument("--headless")
    # driver_options.add_argument("--no-sandbox")
    # driver_options.add_argument("--disable-dev-shm-usage")
    # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=driver_options)
    # print('Starting tests for Firefox...')
    # SignUpTests(driver)
    # print('All tests passed')
    # print('===')
    # driver.close()
    #
    # driver_options = SafariOptions()
    # driver_options.add_argument("--headless")
    # driver_options.add_argument("--no-sandbox")
    # driver_options.add_argument("--disable-dev-shm-usage")
    # driver = webdriver.Safari(options=driver_options)
    # print('Starting tests for Safari...')
    # SignUpTests(driver)
    # print('All tests passed')
    # print('===')
    # driver.close()
    #
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

