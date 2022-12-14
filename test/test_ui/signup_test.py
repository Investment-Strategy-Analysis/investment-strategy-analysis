import random
import string
import time

from selenium.webdriver.common.by import By

from test.test_ui import page_checkers


def generate_random_string(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    rand_string = ''.join(random.choice(alphabet) for i in range(length))
    return rand_string


class PageObjects:
    def __init__(self, driver):
        self.driver = driver

    def get_username_input(self):
        return self.driver.find_element(by=By.ID, value='username_field')

    def get_email_input(self):
        return self.driver.find_element(by=By.ID, value='email_field')

    def get_password_input(self):
        return self.driver.find_element(by=By.ID, value='password_field')

    def get_password_again_input(self):
        return self.driver.find_element(by=By.ID, value='password_again_field')

    def get_sign_up_button(self):
        return self.driver.find_element(by=By.CLASS_NAME, value='auth-button')

    def get_analyzer_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value='Analyzer')

    def get_help_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value='Help')

    def get_title_link(self):
        return self.driver.find_element(by=By.CLASS_NAME, value='navbar-brand')


class SignUpTests:
    def __init__(self, driver):
        self.driver = driver
        self.page_objects = PageObjects(self.driver)
        self.run_all_tests()

    def characteristic_inscriptions_test(self):
        """Проверяем, что на странице присутсвуют все характерные надписи:
           заголовок, названия кнопок, полей и т.д."""

        self.driver.get('http://localhost:5001/auth/signup/')
        time.sleep(5)

        page_checkers.sign_up_page_check(self.driver)

    def password_mismatch_test(self):
        """Поле повторного ввода пароля подсвечивается красным, если пароли
           не совпадают"""
        username_input = self.page_objects.get_username_input()
        username_input.send_keys(generate_random_string(12))

        email_input = self.page_objects.get_email_input()
        email_input.send_keys('ivan@ya.ru')

        password_input = self.page_objects.get_password_input()
        password_input.send_keys('aaa')

        password_again_input = self.page_objects.get_password_again_input()
        password_again_input.send_keys('aa')

        sign_up_button = self.page_objects.get_sign_up_button()
        sign_up_button.click()
        time.sleep(2)

        assert str(password_again_input.value_of_css_property('border-color')) == 'rgb(175, 0, 0)'

    def successful_sign_up_test(self):
        """Вводим правильный пароль и успешно попадаем на страницу авторизации"""
        password_again_input = self.page_objects.get_password_again_input()
        password_again_input.send_keys('a')

        sign_up_button = self.page_objects.get_sign_up_button()
        sign_up_button.click()
        time.sleep(5)

        page_checkers.log_in_page_check(self.driver)

    def sign_up_once_again_fail_test(self):
        """Пробуем еще раз зарегистрировать пользователя, который уже есть"""
        self.driver.get('http://localhost:5001/auth/signup/')
        time.sleep(5)

        username_input = self.page_objects.get_username_input()
        username_input.send_keys('Ivan')

        email_input = self.page_objects.get_email_input()
        email_input.send_keys('ivan@ya.ru')

        password_input = self.page_objects.get_password_input()
        password_input.send_keys('aaa')

        password_again_input = self.page_objects.get_password_again_input()
        password_again_input.send_keys('aaa')

        sign_up_button = self.page_objects.get_sign_up_button()
        sign_up_button.click()
        time.sleep(5)

        assert 'Incorrect username, email or password' in self.driver.page_source

    def sign_up_once_again_success_test(self):
        username_input = self.page_objects.get_username_input()
        username_input.clear()
        username_input.send_keys('Kostya')

        sign_up_button = self.page_objects.get_sign_up_button()
        sign_up_button.click()
        time.sleep(5)

        page_checkers.log_in_page_check(self.driver)

    def analyzer_link_test(self):
        """При нажатии на кнопку 'Analyzer' попадаем на главную страницу выбора стратегии"""
        self.driver.get('http://localhost:5001/auth/signup/')
        time.sleep(5)

        analyzer_link = self.page_objects.get_analyzer_link()
        analyzer_link.click()
        time.sleep(5)

        page_checkers.main_page_check(self.driver)

    def help_link_test(self):
        """При нажатии на кнопку 'Help' попадаем на страницу Help"""
        self.driver.get('http://localhost:5001/auth/login/')
        time.sleep(5)

        help_link = self.page_objects.get_help_link()
        help_link.click()
        time.sleep(5)

        page_checkers.help_page_check(self.driver)

    def logo_click_test(self):
        """При нажатии на логотип попадаем на титульную страницу"""
        self.driver.get('http://localhost:5001/auth/signup')
        time.sleep(5)

        title_link = self.page_objects.get_title_link()
        title_link.click()
        time.sleep(5)

        page_checkers.title_page_check(self.driver)

    def run_all_tests(self):
        self.characteristic_inscriptions_test()
        self.password_mismatch_test()
        self.successful_sign_up_test()
        self.sign_up_once_again_fail_test()
        self.sign_up_once_again_success_test()
        self.analyzer_link_test()
        self.help_link_test()
        self.logo_click_test()
        print('Sign up tests passed')
