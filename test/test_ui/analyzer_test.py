import time
from selenium.webdriver.common.by import By

import test.test_ui.page_checkers as page_checkers


class PageObjects:
    def __init__(self, driver):
        self.driver = driver

    def get_help_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value='Help')

    def get_title_link(self):
        return self.driver.find_element(by=By.CLASS_NAME, value='navbar-brand')


class AnalyzerTests:
    def __init__(self, driver):
        self.driver = driver
        self.page_objects = PageObjects(self.driver)
        self.run_all_tests()

    def characteristic_inscriptions_test(self):
        """Проверяем, что на странице присутсвуют все характерные надписи:
           заголовок, названия кнопок, полей и т.д."""

        self.driver.get('http://localhost:5001/analyzer/')
        time.sleep(10)

        page_checkers.main_page_check(self.driver)

    def all_assets_test(self):
        """Все ожидаемые типы активов присутствуют на странице"""
        assert 'Only Russian assets' in self.driver.page_source
        assert 'Without assets' in self.driver.page_source
        assert 'Without bonds' in self.driver.page_source
        assert 'Without gold' in self.driver.page_source
        assert 'High diversification' in self.driver.page_source

    def all_periods_test(self):
        """Все ожидаемые периоды инвестирования присутствуют на странице"""
        assert '1 year' in self.driver.page_source
        assert '3 years' in self.driver.page_source
        assert '5 years' in self.driver.page_source
        assert '10 years' in self.driver.page_source

    def help_link_test(self):
        """При нажатии на кнопку 'Help' попадаем на страницу Help"""
        self.driver.get('http://localhost:5001/analyzer/')
        time.sleep(10)

        help_link = self.page_objects.get_help_link()
        help_link.click()
        time.sleep(10)

        page_checkers.help_page_check(self.driver)

    def logo_click_test(self):
        """При нажатии на логотип попадаем на титульную страницу"""
        self.driver.get('http://localhost:5001/analyzer/')
        time.sleep(10)

        title_link = self.page_objects.get_title_link()
        title_link.click()
        time.sleep(10)

        page_checkers.title_page_check(self.driver)

    def run_all_tests(self):
        self.characteristic_inscriptions_test()
        self.all_assets_test()
        self.help_link_test()
        self.logo_click_test()
        print('Analyzer tests passed')
