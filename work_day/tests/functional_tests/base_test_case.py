from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class SeleniumBaseTestCase(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()
