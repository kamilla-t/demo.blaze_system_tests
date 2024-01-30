from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class Footer(BasePage):

    @property
    def address(self):
        return self.browser.find_element(By.XPATH, "//p[contains(text(), \"Address:\")]")
    
    @property
    def phone(self):
        return self.browser.find_element(By.XPATH, "//p[contains(text(), \"Phone:\")]")

    @property
    def email(self):
        return self.browser.find_element(By.XPATH, "//p[contains(text(), \"Email:\")]")
