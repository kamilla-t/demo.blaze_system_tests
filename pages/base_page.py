from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    def __init__(self, browser) -> None:
        self.browser = browser
    
    @property
    def alert(self):
        WebDriverWait(self.browser, 5).until(EC.alert_is_present())
        return self.browser.switch_to_alert()
