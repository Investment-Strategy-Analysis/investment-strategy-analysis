import unittest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from test.test_ui.login_test import LogInTests
from test.test_ui.signup_test import SignUpTests
from test.test_ui.help_test import HelpTests
from test.test_ui.title_test import TitleTests
from test.test_ui.analyzer_test import AnalyzerTests
from test.test_ui.user_account_test import UserAccountTests


class FirefoxTest(unittest.TestCase):
    def test_firefox(self):
        driver_options = FirefoxOptions()
        driver_options.add_argument("--headless")
        driver_options.add_argument("--no-sandbox")
        driver_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=driver_options)
        print('Starting tests for Firefox...')
        AnalyzerTests(driver)
        self.assertTrue(True)
        TitleTests(driver)
        self.assertTrue(True)
        HelpTests(driver)
        self.assertTrue(True)
        SignUpTests(driver)
        self.assertTrue(True)
        LogInTests(driver)
        self.assertTrue(True)
        UserAccountTests(driver)
        self.assertTrue(True)
        print('All tests passed')
        print('===')
        driver.close()
