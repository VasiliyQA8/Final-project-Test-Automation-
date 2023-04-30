from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://b2c.passport.rt.ru'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Cant find element by locator {locator}')

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Cant find elements by locator {locator}')

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element_until_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f'Element not clickable!')

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path