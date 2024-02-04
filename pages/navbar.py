from pages.about_us import AboutUs
from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.contact_page import ContactPage
from pages.login_page import LoginPage
from pages.sign_up import SignUpPage

class Navbar(BasePage):

    @property
    def home_button(self):
        return self.browser.find_element(By.XPATH, "//a[contains(text(), \"Home\")]")
    
    @property
    def contact_button(self):
        return self.browser.find_element(By.XPATH, " //a[contains(text(), \"Contact\")]")

    def open_contact(self):
        self.contact_button.click()
        if not ContactPage(self.browser).is_open:
            raise "page is not open"

    @property 
    def about_us_button(self):
        return self.browser.find_element(By.XPATH, "//a[contains(text(), \"About us\")]")
    
    def open_about_us(self):
        self.about_us_button.click()
        if not AboutUs(self.browser).is_open:
            raise "page is not open"
    
    @property
    def cart_button(self):
        return self.browser.find_element(By.XPATH, "//a[contains(text(), \"Cart\")]")
    
    @property 
    def login_button(self):
        return self.browser.find_element(By.ID, "login2")
    
    def open_login(self):
        self.login_button.click()
        if not LoginPage(self.browser).is_open:
            raise "page is not open"
    
    @property 
    def signup_button(self):
        return self.browser.find_element(By.ID, "signin2")
    
    def open_signup(self):
        self.signup_button.click()
        if not SignUpPage(self.browser).is_open:
            raise "page is not open"

    