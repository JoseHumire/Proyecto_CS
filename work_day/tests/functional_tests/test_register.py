from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from .base_test_case import SeleniumBaseTestCase
from ..pages.register_page import RegisterPage


class RegisterTest(SeleniumBaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.page = RegisterPage(self.driver)
        self.driver.get("http://127.0.0.1:8000/register/")

    def fill_register_inputs(self):
        self.page.get_email_input().send_keys('user_test@gmail.com')
        self.page.get_username_input().send_keys('myTestUsername')
        self.page.get_password_input().send_keys('ftws4567')
        self.page.get_password2_input().send_keys('ftws4567')
        self.page.get_firstname_input().send_keys('MyNameTest')
        self.page.get_lastname_input().send_keys('LastNameTest')
        self.page.get_profile_picture_input().send_keys(
            '/home/jhose/Nueva Carpeta/profile_photo.jpg'
        )
        select_city = Select(self.page.get_city_select())
        select_city.select_by_index(0)
        self.page.get_phone_input().send_keys('999999999')
        self.page.get_id_number_input().send_keys('12345678')
        self.page.get_id_photo_input().send_keys(
            '/home/jhose/Nueva Carpeta/id_card_photo.jpg'
        )
        sleep(3)

    def test_register_with_valid_inputs(self):
        self.fill_register_inputs()
        self.page.get_register_button().click()
        self.assertEqual(
            self.driver.current_url, 'http://127.0.0.1:8000/login/'
        )

    def test_register_with_blank_inputs(self):
        self.page.get_register_button().click()
        email_username = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 "input.cell.small-21.form-text.required#edit-name[name='name']")
            )
        )
        print(email_username.get_attribute("validationMessage"))
        self.assertEqual(
            self.driver.current_url, "http://127.0.0.1:8000/register/"
        )

