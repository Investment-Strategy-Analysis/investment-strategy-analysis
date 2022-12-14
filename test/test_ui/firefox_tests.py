import logging
import time
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

logging.basicConfig(format='%(asctime)s.%(msecs)03dZ %(name)s %(levelname)s %(message)s',
                    datefmt="%Y-%m-%dT%H:%M:%S",
                    level=logging.INFO)


class UiTest(unittest.TestCase):
    def setUp(self) -> None:
        create_user_url = "http://localhost:8000/user"
        ping = "http://localhost:8000/ping"

        while True:
            r = requests.get(ping)
            time.sleep(10)
            if r.ok:
                break

        logging.info("Docker is alive")

        r = requests.post(
            create_user_url,
            json={
                "login": "Ivan",
                "password": "aaa"
            },
        )

        logging.info(f"User create status: {r.status_code}")

        # self.driver_options = FirefoxOptions()
        # self.driver = webdriver.Firefox
        # self.service = FirefoxService(GeckoDriverManager().install())

        self.driver_options = ChromiumOptions()
        self.service = ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        self.driver = webdriver.Chrome

        self.driver_options.add_argument("--headless")
        self.driver_options.add_argument("--no-sandbox")
        self.driver_options.add_argument("--disable-dev-shm-usage")

    def test_analyzer(self):
        logging.info("Analyzer page test")
        driver = self.driver(service=self.service, options=self.driver_options)
        AnalyzerTests(driver)
        self.assertTrue(True)
        driver.close()

    def test_title(self):
        logging.info("Title page test")
        driver = self.driver(service=self.service, options=self.driver_options)
        TitleTests(driver)
        self.assertTrue(True)
        driver.close()

    def test_help(self):
        logging.info("Help page test")
        driver = self.driver(service=self.service, options=self.driver_options)
        HelpTests(driver)
        self.assertTrue(True)
        driver.close()

    def test_sign_up(self):
        logging.info("Sign up page test")
        driver = self.driver(service=self.service, options=self.driver_options)
        SignUpTests(driver)
        self.assertTrue(True)
        driver.close()

    def test_log_in(self):
        logging.info("Log in page test")
        driver = self.driver(service=self.service, options=self.driver_options)
        LogInTests(driver)
        self.assertTrue(True)
        driver.close()

    def test_account(self):
        logging.info("Account page test")
        driver = self.driver(service=self.service, options=self.driver_options)
        UserAccountTests(driver)
        self.assertTrue(True)
        driver.close()
