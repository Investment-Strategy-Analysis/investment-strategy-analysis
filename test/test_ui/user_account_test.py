import time

from selenium.webdriver.common.by import By

import login_test
import page_checkers
import signup_test


class PageObjects:
    def __init__(self, driver):
        self.driver = driver

    def get_user_icon(self):
        return self.driver.find_element(by=By.XPATH, value='//*[@id="navbarHISA"]/a/i')

    def get_analyzer_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value='Analyzer')

    def get_help_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value='Help')


class UserAccountTests:
    def __init__(self, driver):
        self.driver = driver
        self.page_objects = PageObjects(self.driver)
        self.run_all_tests()

    def click_user_icon(self):
        user_icon = self.page_objects.get_user_icon()
        user_icon.click()

    def sign_up(self, name, password):
        sign_up_page_objects = signup_test.PageObjects(self.driver)
        sign_up_username = sign_up_page_objects.get_username_input()
        sign_up_username.send_keys(name)
        sign_up_email = sign_up_page_objects.get_email_input()
        sign_up_email.send_keys(name + '@gmail.com')
        sign_up_password = sign_up_page_objects.get_password_input()
        sign_up_password.send_keys(password)
        sign_up_password_again = sign_up_page_objects.get_password_again_input()
        sign_up_password_again.send_keys(password)
        sign_up_button = sign_up_page_objects.get_sign_up_button()
        sign_up_button.click()

    def log_in(self, name, password):
        log_in_page_objects = login_test.PageObjects(self.driver)
        log_in_username = log_in_page_objects.get_username_input()
        log_in_username.send_keys(name)
        log_in_password = log_in_page_objects.get_password_input()
        log_in_password.send_keys(password)
        log_in_button = log_in_page_objects.get_log_in_button()
        log_in_button.click()

    def access_from_title_page_test(self):
        """Проверяем, что можем войти в аккаунт с титульной страницы"""
        self.driver.get('http://localhost:5001')
        time.sleep(10)

        self.click_user_icon()
        time.sleep(10)

        page_checkers.log_in_page_check(self.driver)

    def access_from_help_page_test(self):
        """Проверяем, что можем войти в аккаунт со страницы Help"""
        self.driver.get('http://localhost:5001/help')
        time.sleep(10)

        self.click_user_icon()
        time.sleep(10)

        page_checkers.log_in_page_check(self.driver)

    def access_from_sign_up_page_test(self):
        """Проверяем, что можем войти в аккаунт со страницы регистрацией"""
        self.driver.get('http://localhost:5001/auth/signup')
        time.sleep(10)

        self.click_user_icon()
        time.sleep(10)

        page_checkers.log_in_page_check(self.driver)

    def access_from_log_in_page_test(self):
        """Проверяем, что можем войти в аккаунт со страницы входа"""
        self.driver.get('http://localhost:5001/auth/login')
        time.sleep(10)

        self.click_user_icon()
        time.sleep(10)

        self.log_in('Ivan', 'aaa')
        time.sleep(10)

        page_checkers.main_page_check(self.driver)

        self.click_user_icon()
        time.sleep(10)

        page_checkers.user_account_check(self.driver)
        assert 'Ivan' in self.driver.page_source

    def another_user_account_test(self):
        """Регистрируем другого пользователя, проверяем, что настройки аккаунта изменились"""
        self.driver.get('http://localhost:5001/auth/signup')
        time.sleep(10)

        name, password = 'z', 'z'

        self.sign_up(name, password)

        self.click_user_icon()
        time.sleep(10)

        page_checkers.log_in_page_check(self.driver)
        self.log_in(name, password)
        time.sleep(10)

        page_checkers.main_page_check(self.driver)

        self.click_user_icon()
        time.sleep(10)

        page_checkers.user_account_check(self.driver)
        assert 'z' in self.driver.page_source
        assert 'z@gmail.com' in self.driver.page_source

    def analyzer_link_test(self):
        """При нажатии на кнопку 'Analyzer' попадаем на главную страницу выбора стратегии"""
        analyzer_link = self.page_objects.get_analyzer_link()
        analyzer_link.click()
        time.sleep(10)

        page_checkers.main_page_check(self.driver)

    def help_link_test(self):
        """При нажатии на кнопку 'Help' попадаем на страницу Help"""
        help_link = self.page_objects.get_help_link()
        help_link.click()
        time.sleep(10)

        page_checkers.help_page_check(self.driver)

    def run_all_tests(self):
        self.access_from_title_page_test()
        self.access_from_help_page_test()
        self.access_from_sign_up_page()
        self.access_from_log_in_page_test()
        self.another_user_account_test()
        self.analyzer_link_test()
        self.help_link_test()
        print('Account access tests passed')
