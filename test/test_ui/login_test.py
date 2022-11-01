import time

from selenium.webdriver.common.by import By

import page_checkers


class PageObjects:
    def __init__(self, driver):
        self.driver = driver

    def get_username_input(self):
        return self.driver.find_element(by=By.ID, value='username_field')

    def get_password_input(self):
        return self.driver.find_element(by=By.ID, value='password_field')

    def get_log_in_button(self):
        return self.driver.find_element(by=By.CLASS_NAME, value='auth-button')

    def get_sign_up_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value='Create it!')

    def get_analyzer_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value='Analyzer')


class LogInTests:
    def __init__(self, driver):
        self.driver = driver
        self.page_objects = PageObjects(self.driver)
        self.run_all_tests()

    def characteristic_inscriptions_test(self):
        """Проверяем, что на странице присутсвуют все характерные надписи:
           заголовок, названия кнопок, полей и т.д."""

        self.driver.get('http://localhost:5001/auth/login/')
        time.sleep(10)

        page_checkers.log_in_page_check(self.driver)

    def incorrect_username_test(self):
        """ВВодим имя пользователя, которого не существует в системе - должны получить предупреждение"""
        username_input = self.page_objects.get_username_input()
        username_input.send_keys('.' * 24)

        password_input = self.page_objects.get_password_input()
        password_input.send_keys('***')

        log_in_button = self.page_objects.get_log_in_button()
        log_in_button.click()
        time.sleep(2)

        assert 'Incorrect username or password' in self.driver.page_source

    def incorrect_password_test(self):
        """Вводим верное имя пользователя, но неверный пароль"""
        username_input = self.page_objects.get_username_input()
        username_input.clear()
        username_input.send_keys('Ivan')

        log_in_button = self.page_objects.get_log_in_button()
        log_in_button.click()
        time.sleep(2)

        assert 'Incorrect username or password' in self.driver.page_source

    def successful_log_in_test(self):
        """Успешный вход"""
        password_input = self.page_objects.get_password_input()
        password_input.clear()
        password_input.send_keys('aaa')

        log_in_button = self.page_objects.get_log_in_button()
        log_in_button.click()
        time.sleep(10)

        page_checkers.main_page_check(self.driver)

    def sign_up_link_test(self):
        """При клике на ссылку 'Create it' попадаем на страницу с регистрацией"""
        self.driver.get('http://localhost:5001/auth/login/')
        time.sleep(10)

        sign_up_link = self.page_objects.get_sign_up_link()
        sign_up_link.click()
        time.sleep(10)

        page_checkers.sign_up_page_check(self.driver)

    def analyzer_link_test(self):
        """При нажатии на кнопку 'Analyzer' попадаем на главную страницу выбора стратегии"""
        self.driver.get('http://localhost:5001/auth/login/')
        time.sleep(10)

        analyzer_link = self.page_objects.get_analyzer_link()
        analyzer_link.click()
        time.sleep(10)

        page_checkers.main_page_check(self.driver)

    def run_all_tests(self):
        self.characteristic_inscriptions_test()
        self.incorrect_username_test()
        self.incorrect_password_test()
        self.successful_log_in_test()
        self.sign_up_link_test()
        self.analyzer_link_test()
        print('Log in tests passed')
