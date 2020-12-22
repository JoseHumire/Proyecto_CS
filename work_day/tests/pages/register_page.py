from selenium.webdriver.chrome.webdriver import WebDriver

from work_day.tests.locators.register_locator import RegisterLocator


class RegisterPage:
    """

    """
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_email_input(self):
        return self.driver.find_element(*RegisterLocator.EMAIL_INPUT)

    def get_username_input(self):
        return self.driver.find_element(*RegisterLocator.USERNAME_INPUT)

    def get_password_input(self):
        return self.driver.find_element(*RegisterLocator.PASSWORD_INPUT)

    def get_password2_input(self):
        return self.driver.find_element(*RegisterLocator.REPEAT_PASSWORD_INPUT)

    def get_firstname_input(self):
        return self.driver.find_element(*RegisterLocator.FIRST_NAME_INPUT)

    def get_lastname_input(self):
        return self.driver.find_element(*RegisterLocator.LAST_NAME_INPUT)

    def get_profile_picture_input(self):
        return self.driver.find_element(*RegisterLocator.PROFILE_PICTURE_INPUT)

    def get_city_select(self):
        return self.driver.find_element(*RegisterLocator.CITY_SELECT)

    def get_phone_input(self):
        return self.driver.find_element(*RegisterLocator.PHONE_INPUT)

    def get_id_number_input(self):
        return self.driver.find_element(*RegisterLocator.ID_NUMBER_INPUT)

    def get_id_photo_input(self):
        return self.driver.find_element(*RegisterLocator.ID_PHOTO_INPUT)

    def get_register_button(self):
        return self.driver.find_element(*RegisterLocator.REGISTER_BUTTON)

    def get_login_link(self):
        return self.driver.find_element()


