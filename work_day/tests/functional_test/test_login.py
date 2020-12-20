from time import sleep

from work_day.tests.functional_test.base_test_case import SeleniumBaseTestCase


class LoginTest(SeleniumBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.driver.get("http://127.0.0.1:8000/login/")

    def test_verify_login_with_valid_inputs(self):
        self.driver.find_element_by_xpath(
            "//input[@id='id_username']").send_keys('raulmanuel')
        self.driver.find_element_by_xpath(
            "//input[@id='id_password']").send_keys('raul1812')
        self.driver.find_element_by_xpath(
            "//button[contains(text(),'Sign In')]").click()
        self.assertEqual(
            self.driver.current_url, 'http://127.0.0.1:8000/home/'
        )
