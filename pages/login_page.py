from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    @property
    def is_open(self):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located((By.ID, "logInModal")))
            return True
        except:
            return False

    @property
    def login_username(self):
        return self.browser.find_element(By.ID, "loginusername")
    
    @property
    def password_username(self):
        return self.browser.find_element(By.ID, "loginpassword")

    @property
    def login_button(self):
        return self.browser.find_element(By.XPATH, "//button[text()=\"Log in\"]")
    
    @property
    def close_button(self):
        return self.browser.find_element(By.XPATH, "//button[text()=\"Close\"]")

    def fill_login(self, username, password):
        self.login_username.send_keys(username)
        self.password_username.send_keys(password)
        self.login_button.click()

