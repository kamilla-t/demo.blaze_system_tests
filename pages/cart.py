from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class Cart(BasePage):

    @property 
    def place_order_button(self):
        return self.browser.find_element(By.XPATH, "//button[contains(text(), \"Place Order\")]")