import pytest
from selenium import webdriver



@pytest.fixture(scope='session', autouse=True)
def browser():
   driver = webdriver.Chrome("F:/Python/QAP/рageObject/yandexdriver.exe")

   driver.implicitly_wait(10)
   yield driver

   driver.quit()
