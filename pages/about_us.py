from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class AboutUs(BasePage):
    
    # to do: play video element

    @property
    def close_button(self):
        return self.browser.find_element(By.XPATH, "//button[text()=\"Close\"]")