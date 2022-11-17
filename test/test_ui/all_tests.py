from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromiumOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.chrome.service import Service as СhromiumService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.utils import ChromeType

from test.test_ui.login_test import LogInTests
from test.test_ui.signup_test import SignUpTests
from test.test_ui.help_test import HelpTests
from test.test_ui.title_test import TitleTests
from test.test_ui.analyzer_test import AnalyzerTests

if __name__ == '__main__':
    driver_options = ChromiumOptions()
    # driver_options.add_argument("--headless")
    driver_options.add_argument("--no-sandbox")
    driver_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=СhromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
                              options=driver_options)
    print('Starting tests for Chromium...')
    AnalyzerTests(driver)
    # TitleTests(driver)
    # HelpTests(driver)
    # SignUpTests(driver)
    # LogInTests(driver)
    print('All tests passed')
    print('===')
    driver.close()

    # driver_options = EdgeOptions()
    # driver_options.add_argument("--headless")
    # driver_options.add_argument("--no-sandbox")
    # driver_options.add_argument("--disable-dev-shm-usage")
    # driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=driver_options)
    # print('Starting tests for Edge...')
    # TitleTests(driver)
    # HelpTests(driver)
    # SignUpTests(driver)
    # LogInTests(driver)
    # print('All tests passed')
    # print('===')
    # driver.close()
    #
    # driver_options = FirefoxOptions()
    # driver_options.add_argument("--headless")
    # driver_options.add_argument("--no-sandbox")
    # driver_options.add_argument("--disable-dev-shm-usage")
    # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=driver_options)
    # print('Starting tests for Firefox...')
    # TitleTests(driver)
    # HelpTests(driver)
    # SignUpTests(driver)
    # LogInTests(driver)
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
    # TitleTests(driver)
    # HelpTests(driver)
    # SignUpTests(driver)
    # LogInTests(driver)
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
    # TitleTests(driver)
    # HelpTests(driver)
    # SignUpTests(driver)
    # LogInTests(driver)
    # print('All tests passed')
    # print('===')
    # driver.close()

