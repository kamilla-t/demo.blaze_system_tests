from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class Navbar(BasePage):

    @property
    def home_button(self):
        return self.browser.find_element(By.XPATH, "//a[contains(text(), \"Home\")]")
    
    @property
    def contact_button(self):
        return self.browser.find_element(By.XPATH, " //a[contains(text(), \"Contact\")]")

    @property 
    def about_us_button(self):
        return self.browser.find_element(By.XPATH, "//a[contains(text(), \"About us\")]")
    
    @property
    def cart_button(self):
        return self.browser.find_element(By.XPATH, "//a[contains(text(), \"Cart\")]")
    
    @property 
    def login_button(self):
        return self.browser.find_element(By.ID, "login2")
    
    @property 
    def signup_button(self):
        return self.browser.find_element(By.ID, "signin2")