
from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    LOGO = (By.XPATH, "//*[@id='root']/div/div[1]")
    IMAGE = (By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div[2]")
    EMAIL = (By.ID, "user-name")
    PASSWORD = (By.ID, 'password')
    SUBMIT = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
    MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT = (By.ID, "logout_sidebar_link")

