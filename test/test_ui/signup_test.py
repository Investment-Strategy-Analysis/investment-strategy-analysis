import random
import string
import time
from selenium.webdriver.common.by import By


def generate_random_string(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    rand_string = ''.join(random.choice(alphabet) for i in range(length))
    return rand_string


class PageObjects:
    def __init__(self, driver):
        self.driver = driver

    def get_username_input(self):
        return self.driver.find_element(by=By.ID, value='username_field')

    def get_password_input(self):
        return self.driver.find_element(by=By.ID, value='password_field')

    def get_password_again_input(self):
        return self.driver.find_element(by=By.ID, value='password_again_field')

    def get_sign_up_button(self):
        return self.driver.find_element(by=By.CLASS_NAME, value='auth-button')

    def get_analyzer_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value='Analyzer')


class SignUpTests:
    def __init__(self, driver):
        self.driver = driver
        self.page_objects = PageObjects(self.driver)
        self.run_all_tests()

    def characteristic_inscriptions_test(self):
        """Проверяем, что на странице присутсвуют все характерные надписи:
           заголовок, названия кнопок, полей и т.д."""

        self.driver.get('http://localhost:5001/auth/signup/')
        time.sleep(10)

        assert 'Sign Up to HISA' in self.driver.page_source
        assert 'Password' in self.driver.page_source
        assert 'Password again' in self.driver.page_source
        assert 'Sign up' in self.driver.page_source
        assert 'Analyzer' in self.driver.page_source
        assert 'Help' in self.driver.page_source

    def password_mismatch_test(self):
        """Поле повторного ввода пароля подсвечивается красным, если пароли
           не совпадают"""
        username_input = self.page_objects.get_username_input()
        username_input.send_keys(generate_random_string(12))

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
        time.sleep(10)

        assert 'Log In to HISA' in self.driver.page_source

    def analyzer_link_test(self):
        """При нажатии на кнопку 'Analyzer' попадаем на главную страницу выбора стратегии"""
        self.driver.get('http://localhost:5001/auth/signup/')
        time.sleep(10)

        analyzer_link = self.page_objects.get_analyzer_link()
        analyzer_link.click()
        time.sleep(10)

        assert 'Strategy' in self.driver.page_source
        assert 'Settings' in self.driver.page_source
        assert 'Risk' in self.driver.page_source
        assert 'Profit' in self.driver.page_source
        assert 'Time period' in self.driver.page_source
        assert 'Find optimal configuration' in self.driver.page_source

    def run_all_tests(self):
        self.characteristic_inscriptions_test()
        self.password_mismatch_test()
        self.successful_sign_up_test()
        self.analyzer_link_test()
        print('Sign up tests passed')
