from pages.base_page import BasePage
from pages.home_page import HomePage
from helpers import users
from helpers.locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.saucedemo.com/')
        self.locator = LoginPageLocators

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def enter_username(self, username):
        return self.find_element(*self.locator.EMAIL).send_keys(username)

    def enter_password(self, password):
        return self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        return self.find_element(*self.locator.SUBMIT).click()
        # return LoginPage(self.driver)

    def validate_url(self):
        return self.get_url()

    def get_logo(self):
        return self.find_element(*self.locator.LOGO).is_displayed()

    def get_header(self):
        return self.get_title()

    def get_image(self):
        return self.find_element(*self.locator.IMAGE)

    def get_login_elements(self):
        self.find_element(*self.locator.EMAIL).is_displayed()
        self.find_element(*self.locator.EMAIL).is_enabled()
        self.find_element(*self.locator.PASSWORD).is_displayed()
        self.find_element(*self.locator.PASSWORD).is_enabled()
        self.find_element(*self.locator.SUBMIT).is_displayed()
        self.find_element(*self.locator.SUBMIT).is_enabled()

    def login(self, user):
        user = users.get_user(user)
        print(user)
        self.enter_username(user['email'])
        self.enter_password(user["password"])
        self.click_login_button()

    def login_with_valid_user(self, user):
        self.login(user)
        return HomePage(self.driver)

    def login_with_in_valid_user(self, user):
        self.login(user)
        return self.find_element(*self.locator.ERROR_MESSAGE).text

    def sign_out(self):
        self.find_element(*self.locator.MENU).click()
        self.driver.implicitly_wait(10)
        self.find_element(*self.locator.LOGOUT).click()
        self.driver.implicitly_wait(10)

    def get_username_exception(self, user):
        user = users.get_user(user)
        self.enter_password(user["password"])
        self.click_login_button()
        return self.find_element(*self.locator.ERROR_MESSAGE).text

    def get_password_exception(self, user):
        user = users.get_user(user)
        self.enter_username(user["email"])
        self.click_login_button()
        return self.find_element(*self.locator.ERROR_MESSAGE).text
