import time
from selenium.webdriver.common.by import By

import test.test_ui.page_checkers as page_checkers


class PageObjects:
    def __init__(self, driver):
        self.driver = driver

    def get_title_page_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value='here')

    def get_sign_up_page_link(self):
        return self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/ul/li[2]/a')

    def get_log_in_page_link(self):
        return self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/ul/li[3]/a')

    def get_analyzer_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value='Analyzer')

    def get_title_link(self):
        return self.driver.find_element(by=By.CLASS_NAME, value='navbar-brand')


class HelpTests:
    def __init__(self, driver):
        self.driver = driver
        self.page_objects = PageObjects(self.driver)
        self.run_all_tests()

    def characteristic_inscriptions_test(self):
        """Проверяем, что на странице присутсвуют все характерные надписи:
           заголовок, названия кнопок, полей и т.д."""

        self.driver.get('http://localhost:5001/help')
        time.sleep(10)

        page_checkers.help_page_check(self.driver)

    def title_page_link_test(self):
        """Проверяем, что работает ссылка на титульную страницу"""
        title_page_link = self.page_objects.get_title_page_link()
        title_page_link.click()
        time.sleep(10)

        page_checkers.title_page_check(self.driver)

    def sign_up_page_link_test(self):
        """Проверяем, что работает ссылка на страницу с регистрацией"""
        self.driver.get('http://localhost:5001/help')
        time.sleep(10)

        sign_up_page_link = self.page_objects.get_sign_up_page_link()
        sign_up_page_link.click()
        time.sleep(10)

        page_checkers.sign_up_page_check(self.driver)

    def log_in_page_link_test(self):
        """Проверяем, что работает ссылка на страницу со входом"""
        self.driver.get('http://localhost:5001/help')
        time.sleep(10)

        log_in_page_link = self.page_objects.get_log_in_page_link()
        log_in_page_link.click()
        time.sleep(10)

        page_checkers.log_in_page_check(self.driver)

    def analyzer_link_test(self):
        """При нажатии на кнопку 'Analyzer' попадаем на главную страницу выбора стратегии"""
        self.driver.get('http://localhost:5001/help')
        time.sleep(10)

        analyzer_link = self.page_objects.get_analyzer_link()
        analyzer_link.click()
        time.sleep(10)

        page_checkers.main_page_check(self.driver)

    def logo_click_test(self):
        """При нажатии на логотип попадаем на титульную страницу"""
        self.driver.get('http://localhost:5001/help')
        time.sleep(10)

        title_link = self.page_objects.get_title_link()
        title_link.click()
        time.sleep(10)

        page_checkers.title_page_check(self.driver)

    def run_all_tests(self):
        self.characteristic_inscriptions_test()
        self.title_page_link_test()
        self.sign_up_page_link_test()
        self.log_in_page_link_test()
        self.analyzer_link_test()
        self.logo_click_test()
        print('Help tests passed')
