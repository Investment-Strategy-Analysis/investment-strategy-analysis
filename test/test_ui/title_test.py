import time
from selenium.webdriver.common.by import By

import test.test_ui.page_checkers as page_checkers


class PageObjects:
    def __init__(self, driver):
        self.driver = driver

    def get_analyzer_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value='Analyzer')

    def get_help_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value='Help')

    def get_sign_up_button(self):
        return self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[3]/div/button')

    def get_log_in_button(self):
        return self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[4]/div/button')

    def get_try_now_button(self):
        return self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div/button')


class TitleTests:
    def __init__(self, driver):
        self.driver = driver
        self.page_objects = PageObjects(self.driver)
        self.run_all_tests()

    def characteristic_inscriptions_test(self):
        """Проверяем, что на странице присутсвуют все характерные надписи:
           заголовок, названия кнопок, полей и т.д."""

        self.driver.get('http://localhost:5001')
        time.sleep(5)

        page_checkers.title_page_check(self.driver)

    def sign_up_button_test(self):
        """При нажатии на кнопку 'Sign up' попадаем на страницу с регистрацией"""
        sign_up_button = self.page_objects.get_sign_up_button()
        sign_up_button.click()
        time.sleep(5)

        page_checkers.sign_up_page_check(self.driver)

    def log_in_button_test(self):
        """При нажатии на кнопку 'Log in' попадаем на страницу со входом"""
        self.driver.get('http://localhost:5001')
        time.sleep(5)

        log_in_button = self.page_objects.get_log_in_button()
        log_in_button.click()
        time.sleep(5)

        page_checkers.log_in_page_check(self.driver)

    def try_now_button_test(self):
        """При нажатии на кнопку 'Try now' попадаем на главную страницу"""
        self.driver.get('http://localhost:5001')
        time.sleep(5)

        try_now_button = self.page_objects.get_try_now_button()
        try_now_button.click()
        time.sleep(5)

        page_checkers.main_page_check(self.driver)

    def analyzer_link_test(self):
        """При нажатии на кнопку 'Analyzer' попадаем на главную страницу выбора стратегии"""
        self.driver.get('http://localhost:5001')
        time.sleep(5)

        analyzer_link = self.page_objects.get_analyzer_link()
        analyzer_link.click()
        time.sleep(5)

        page_checkers.main_page_check(self.driver)

    def help_link_test(self):
        """При нажатии на кнопку 'Help' попадаем на страницу Help"""
        self.driver.get('http://localhost:5001/')
        time.sleep(5)

        help_link = self.page_objects.get_help_link()
        help_link.click()
        time.sleep(5)

        page_checkers.help_page_check(self.driver)

    def run_all_tests(self):
        self.characteristic_inscriptions_test()
        self.sign_up_button_test()
        self.log_in_button_test()
        self.try_now_button_test()
        self.analyzer_link_test()
        self.help_link_test()
        print('Title tests passed')
