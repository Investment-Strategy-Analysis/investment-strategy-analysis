import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import test.test_ui.page_checkers as page_checkers
import test.test_ui.login_test as login


class PageObjects:
    def __init__(self, driver):
        self.driver = driver

    def get_help_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value='Help')

    def get_title_link(self):
        return self.driver.find_element(by=By.CLASS_NAME, value='navbar-brand')

    def get_only_russian_checkbox(self):
        return self.driver.find_element(by=By.NAME, value='ONLY_RUSSIAN')

    def get_without_assets_checkbox(self):
        return self.driver.find_element(by=By.NAME, value='WITHOUT_ASSETS')

    def get_without_bonds_checkbox(self):
        return self.driver.find_element(by=By.NAME, value='WITHOUT_BONDS')

    def get_without_gold_checkbox(self):
        return self.driver.find_element(by=By.NAME, value='WITHOUT_GOLD')

    def get_high_diversification_checkbox(self):
        return self.driver.find_element(by=By.NAME, value='HIGH_DIVERSIFICATION')

    def get_strategy_options(self):
        return self.driver.find_element(by=By.ID, value='strategyOptionSelector')

    def get_profit_slider(self):
        return self.driver.find_element(by=By.ID, value='profitRange')

    def get_profit_input(self):
        return self.driver.find_element(by=By.ID, value='profitRangeNumber')

    def get_loader_identifier(self):
        return self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div/div/div')

    def get_optimal_config_button(self):
        return self.driver.find_element(By.CLASS_NAME, "run-button")
        # return self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[1]/button')


class AnalyzerTests:
    def __init__(self, driver):
        self.driver = driver
        self.page_objects = PageObjects(self.driver)
        self.run_all_tests()

    def characteristic_inscriptions_test(self):
        """Проверяем, что на странице присутсвуют все характерные надписи:
           заголовок, названия кнопок, полей и т.д."""

        self.driver.get('http://localhost:5001/analyzer/')
        time.sleep(5)

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

    def assets_checkboxes_test(self):
        """Все поля для проставления галочек успешно функционируют"""
        getters = [
            self.page_objects.get_only_russian_checkbox,
            self.page_objects.get_without_assets_checkbox,
            self.page_objects.get_without_bonds_checkbox,
            self.page_objects.get_without_gold_checkbox,
            self.page_objects.get_high_diversification_checkbox
        ]
        for getter in getters:
            checkbox = getter()
            checkbox.click()
            time.sleep(2)
            assert checkbox.get_attribute('checked')
            checkbox.click()

    def strategy_options_test(self):
        """Все опции для выбора стратегии успешно функционируют"""
        select = Select(self.page_objects.get_strategy_options())

        select.select_by_value('safety')
        time.sleep(2)
        assert 'Minimal risk' in self.driver.page_source

        select.select_by_value('risky')
        time.sleep(2)
        assert 'Maximal profit' in self.driver.page_source

        select.select_by_value('custom')
        time.sleep(2)
        assert 'You can create new strategy!' in self.driver.page_source

    def profit_slider_test(self):
        """Возможность двигать ползунок с прибылью"""
        profit_slider = self.page_objects.get_profit_slider()
        move = ActionChains(self.driver)

        move.click_and_hold(profit_slider).move_by_offset(20, 0).release().perform()
        time.sleep(3)
        assert '58' in self.driver.page_source

        move.click_and_hold(profit_slider).move_by_offset(122, 0).release().perform()
        time.sleep(3)
        assert '100' in self.driver.page_source

        move.click_and_hold(profit_slider).move_by_offset(-49, 0).release().perform()
        time.sleep(3)
        assert '29' in self.driver.page_source

    def manually_profit_input_test(self):
        """Возможность вводить значение прибыли вручную"""
        profit_input = self.page_objects.get_profit_input()

        profit_input.clear()
        profit_input.send_keys('0')
        time.sleep(2)
        assert '0' in self.driver.page_source

        profit_input.clear()
        profit_input.send_keys('87,2')
        time.sleep(2)
        assert '87' in self.driver.page_source
        assert '2' in self.driver.page_source

    def calculations_start_test(self):
        self.driver.get('http://localhost:5001/analyzer/')
        optimal_config_button = self.page_objects.get_optimal_config_button()
        optimal_config_button.click()
        time.sleep(5)

        page_checkers.log_in_page_check(self.driver)
        login_page_objects = login.PageObjects(self.driver)
        username_input = login_page_objects.get_username_input()
        username_input.send_keys('Ivan')
        password_input = login_page_objects.get_password_input()
        password_input.send_keys('aaa')
        log_in_button = login_page_objects.get_log_in_button()
        log_in_button.click()
        time.sleep(5)

        optimal_config_button = self.page_objects.get_optimal_config_button()
        optimal_config_button.click()
        time.sleep(5)
        loader = self.page_objects.get_loader_identifier()
        assert loader is not None

    def help_link_test(self):
        """При нажатии на кнопку 'Help' попадаем на страницу Help"""
        self.driver.get('http://localhost:5001/analyzer/')
        time.sleep(5)

        help_link = self.page_objects.get_help_link()
        help_link.click()
        time.sleep(5)

        page_checkers.help_page_check(self.driver)

    def logo_click_test(self):
        """При нажатии на логотип попадаем на титульную страницу"""
        self.driver.get('http://localhost:5001/analyzer/')
        time.sleep(5)

        title_link = self.page_objects.get_title_link()
        title_link.click()
        time.sleep(5)

        page_checkers.title_page_check(self.driver)

    def run_all_tests(self):
        self.characteristic_inscriptions_test()
        self.all_assets_test()
        self.assets_checkboxes_test()
        self.strategy_options_test()
        self.profit_slider_test()
        self.manually_profit_input_test()
        self.calculations_start_test()
        self.help_link_test()
        self.logo_click_test()

        print('Analyzer tests passed')
