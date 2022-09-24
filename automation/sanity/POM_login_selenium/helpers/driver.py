from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import logging


class DriverPO:

    @classmethod
    def get_driver(cls):
        try:
            global driver
            driver = webdriver.Chrome(ChromeDriverManager().install())
            return driver
        except TimeoutException:
            logging.info("YOU link not found ... breaking out")