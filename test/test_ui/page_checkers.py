def sign_up_page_check(driver):
    assert 'Password' in driver.page_source
    assert 'Password again' in driver.page_source
    assert 'Sign up' in driver.page_source
    assert 'Analyzer' in driver.page_source
    assert 'Help' in driver.page_source


def log_in_page_check(driver):
    assert 'Password' in driver.page_source
    assert 'Log in' in driver.page_source
    assert 'Analyzer' in driver.page_source
    assert 'Help' in driver.page_source
    assert 'Do not have account?' in driver.page_source
    assert 'Create it!' in driver.page_source


def main_page_check(driver):
    assert 'Strategy' in driver.page_source
    assert 'Settings' in driver.page_source
    assert 'Risk' in driver.page_source
    assert 'Profit' in driver.page_source
    assert 'Time period' in driver.page_source
    assert 'Find optimal configuration' in driver.page_source


def help_page_check(driver):
    assert 'HISA Help' in driver.page_source
    assert 'Analyzer' in driver.page_source
    assert 'Sign up' in driver.page_source
    assert 'Log in' in driver.page_source


def title_page_check(driver):
    assert 'Historical' in driver.page_source
    assert 'Investment' in driver.page_source
    assert 'Strategy' in driver.page_source
    assert 'Analysis' in driver.page_source
    assert 'Try now' in driver.page_source
    assert 'Sign up' in driver.page_source
    assert 'Log in' in driver.page_source
    assert 'Analyzer' in driver.page_source
    assert 'Help' in driver.page_source
