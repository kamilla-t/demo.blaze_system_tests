from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignUpPage(BasePage):

    @property
    def is_open(self):
        try:
            WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.ID, "signInModal")))
            return True
        except:
            return False
    
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

