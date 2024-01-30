from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class SignUpPage(BasePage):
    
    @property 
    def login_input(self):
        return self.browser.find_element(By.ID, "sign-username")
    
    @property 
    def password_input(self):
        return self.browser.find_element(By.ID, "sign-password")
    
    @property 
    def submit_button(self):
        return self.browser.find_element(By.XPATH, "//button[text()=\"Sign up\"]")
    
    def fill_signup(self, username, password):
        self.login_input.send_keys(username)
        self.password_input.send_keys(password)
        self.submit_button.click()

    # alert = browser.switch_to.alert
    # alert.accept()

