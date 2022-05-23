import datetime
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LocationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://127.0.0.1:8000/')
        username = self.driver.find_element(by=By.NAME, value='username')
        username.send_keys('cilicabogdan')
        password = self.driver.find_element(by=By.NAME, value='password')
        password.send_keys('bogdan123')
        submit = self.driver.find_element(by=By.CLASS_NAME, value='btn-info')
        submit.submit()
        self.logs = open('log.txt', mode='a')

    def test_form(self):
        if value:= 'table' in self.driver.page_source:
            self.logs.write(f'{value}, {datetime.datetime.now()}\n')
        assert value

    # def test_add_location(self):
