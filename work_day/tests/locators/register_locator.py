from selenium.webdriver.common.by import By


class RegisterLocator:
    EMAIL_INPUT = (By.XPATH, "//input[@id='id_email']")
    USERNAME_INPUT = (By.XPATH, "//input[@id='id_username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='id_password1']")
    REPEAT_PASSWORD_INPUT = (By.XPATH, "//input[@id='id_password2']")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@id='id_first_name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='id_last_name']")
    PROFILE_PICTURE_INPUT = (By.XPATH, "//input[@id='id_profile_picture']")
    CITY_SELECT = (By.XPATH, "//select[@id='id_city']")
    PHONE_INPUT = (By.XPATH, "//input[@id='id_phone']")
    ID_NUMBER_INPUT = (By.XPATH, "//input[@id='id_id_number']")
    ID_PHOTO_INPUT = (By.XPATH, "//input[@id='id_id_image']")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Register')]")
    LOGIN_LINK = (By.LINK_TEXT, "I already have a membership")
