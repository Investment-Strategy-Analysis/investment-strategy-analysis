import unittest

import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromiumOptions
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from test.test_ui.login_test import LogInTests
from test.test_ui.signup_test import SignUpTests
from test.test_ui.help_test import HelpTests
from test.test_ui.title_test import TitleTests
from test.test_ui.analyzer_test import AnalyzerTests
from test.test_ui.user_account_test import UserAccountTests


class UiTest(unittest.TestCase):
    def setUp(self) -> None:
        create_user_url = "http://localhost:8000/user"
        ping = "http://localhost:8000/ping"

        while True:
            r = requests.get(ping)
            if r.ok:
                break

        requests.post(
            create_user_url,
            json={
                "login": "Ivan",
                "password": "aaa"
            },
        )

        self.driver_options = FirefoxOptions()
        self.driver = webdriver.Firefox
        self.driver_options.add_argument("--headless")
        self.driver_options.add_argument("--no-sandbox")
        self.driver_options.add_argument("--disable-dev-shm-usage")
        self.service = FirefoxService(GeckoDriverManager().install())

        # self.driver_options = ChromiumOptions()
        # self.service = ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        # self.driver = webdriver.Chrome

    def test_analyzer(self):
        driver = self.driver(service=self.service, options=self.driver_options)
        AnalyzerTests(driver)
        self.assertTrue(True)
        driver.close()

    def test_title(self):
        driver = self.driver(service=self.service, options=self.driver_options)
        TitleTests(driver)
        self.assertTrue(True)
        driver.close()

    def test_help(self):
        driver = self.driver(service=self.service, options=self.driver_options)
        HelpTests(driver)
        self.assertTrue(True)
        driver.close()

    def test_sign_up(self):
        driver = self.driver(service=self.service, options=self.driver_options)
        SignUpTests(driver)
        self.assertTrue(True)
        driver.close()

    def test_log_in(self):
        driver = self.driver(service=self.service, options=self.driver_options)
        LogInTests(driver)
        self.assertTrue(True)
        driver.close()

    def test_account(self):
        driver = self.driver(service=self.service, options=self.driver_options)
        UserAccountTests(driver)
        self.assertTrue(True)
        driver.close()
