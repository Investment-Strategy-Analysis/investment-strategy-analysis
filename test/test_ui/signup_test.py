from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class SignUpTests:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('http://localhost:5001/auth/signup/')
        self.run_all_tests()

    def characteristic_inscriptions_test(self):
        """Проверяем, что на странице присутсвуют все характерные надписи:
           заголовок, названия кнопок, полей и т.д."""

        assert 'Sign Up to HISA' in self.driver.page_source
        assert 'Password' in self.driver.page_source
        assert 'Password again' in self.driver.page_source
        assert 'Sign up' in self.driver.page_source

        print('Characteristic inscriptions test passed')

    def run_all_tests(self):
        self.characteristic_inscriptions_test()
        self.driver.close()


if __name__ == '__main__':
    driver_options = Options()
    driver_options.add_argument("--headless")
    driver_options.add_argument("--no-sandbox")
    driver_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=driver_options)
    print('Starting tests for Chrome...')
    SignUpTests(driver)
    print('Chrome tests passed')
    print('===')
