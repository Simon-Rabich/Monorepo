from service.base_test import BaseTest
from pages.login_page import *
from common.configurations.get_config import get_config


class TestLoginPage(BaseTest):

    def test_page_load(self):
        login_page = LoginPage(self.driver)
        res = login_page.check_page_loaded()
        self.assertEqual(True, res)

    def test_sign_in_with_valid_user(self):
        login_page = LoginPage(self.driver)
        result = login_page.login_with_valid_user("valid_user")
        self.assertIn('https://www.saucedemo.com/inventory.html', result.get_url())

    def test_sign_in_with_in_valid_user(self):
        login_page = LoginPage(self.driver)
        result = login_page.login_with_in_valid_user("invalid_user")
        self.assertEqual(get_config()['expected_username_and_pass_exception'], result)

    def test_url_is_correct(self):
        login_page = LoginPage(self.driver)
        get_url = login_page.validate_url()
        assert get_url == get_config()['base_url']

    def test_top_logo_is_visible(self):
        login_page = LoginPage(self.driver)
        get_logo = login_page.get_logo()
        self.assertTrue(self, get_logo)

    def test_get_title(self):
        login_page = LoginPage(self.driver)
        get_header = login_page.get_header()
        self.assertEqual(get_header, 'Swag Labs')

    def test_image_is_visible(self):
        login_page = LoginPage(self.driver)
        get_img = login_page.get_image()
        self.assertTrue(self, get_img.size['width'] is not 0)
        self.assertTrue(self, get_img.is_displayed())

    def test_sign_out(self):
        login_page = LoginPage(self.driver)
        login_page.login_with_valid_user("valid_user")
        sign_out = login_page.sign_out()
        self.assertTrue(self, sign_out)

    def test_generic_exception(self):
        login_page = LoginPage(self.driver)
        get_username_and_password_error = login_page.login_with_in_valid_user("invalid_user")
        assert get_username_and_password_error == get_config()['expected_username_and_pass_exception']

    def test_username_exception(self):
        login_page = LoginPage(self.driver)
        result = login_page.get_username_exception("Admin0")
        assert result == get_config()['expected_username_exception']

    def test_password_exception(self):
        login_page = LoginPage(self.driver)
        result = login_page.get_password_exception("Staff2")
        assert result == get_config()['expected_password_exception']

    def test_visual_login_elements(self):
        login_page = LoginPage(self.driver)
        res = login_page.get_login_elements()
        self.assertTrue(self, res)
