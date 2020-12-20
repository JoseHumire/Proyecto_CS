from time import sleep

from .base_test_case import SeleniumBaseTestCase


class LoginTest(SeleniumBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.driver.get("http://127.0.0.1:8000/login/")

    def test_verify_login_with_valid_inputs(self):
        self.driver.find_element_by_xpath(
            "//*[@id='id_username']").send_keys('nur1234')
        self.driver.find_element_by_xpath(
            "//input[@id='id_password']").send_keys('shamas5432')
        self.driver.find_element_by_xpath(
            "//button[contains(text(),'Sign In')]").click()
        self.assertEqual(
            self.driver.current_url, 'http://127.0.0.1:8000/home/'
        )

    def test_verify_login_with_invalid_inputs(self):
        self.driver.find_element_by_xpath(
            "//*[@id='id_username']").send_keys('jfioeajfoa')
        self.driver.find_element_by_xpath(
            "//input[@id='id_password']").send_keys('fewjiofwje')
        self.driver.find_element_by_xpath(
            "//button[contains(text(),'Sign In')]").click()
        self.assertEqual(
            self.driver.current_url, 'http://127.0.0.1:8000/login/'
        )

    def test_verify_login_with_empty_inputs(self):
        self.driver.find_element_by_xpath(
            "//*[@id='id_username']").send_keys('')
        self.driver.find_element_by_xpath(
            "//input[@id='id_password']").send_keys('')
        self.driver.find_element_by_xpath(
            "//button[contains(text(),'Sign In')]").click()
        self.assertEqual(
            self.driver.current_url, 'http://127.0.0.1:8000/login/'
        )

    def test_verify_password_recover_link(self):
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/p[2]/a").click()
        self.assertEqual(
            self.driver.current_url, 'http://127.0.0.1:8000/resetPassword/'
        )

    def test_verify_register_link(self):
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/p[3]/a").click()
        self.assertEqual(
            self.driver.current_url, 'http://127.0.0.1:8000/register/'
        )