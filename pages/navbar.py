from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Navbar(BasePage):

    @property
    def home_button(self):
        return self.browser.find_element(By.XPATH, "//a[contains(text(), \"Home\")]")
    
    @property
    def contact_button(self):
        return self.browser.find_element(By.XPATH, " //a[contains(text(), \"Contact\")]")

    def open_contact(self):
        self.contact_button.click()
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-content")))

    @property 
    def about_us_button(self):
        return self.browser.find_element(By.XPATH, "//a[contains(text(), \"About us\")]")
    
    def open_about_us(self):
        self.about_us_button.click()
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
    
    @property
    def cart_button(self):
        return self.browser.find_element(By.XPATH, "//a[contains(text(), \"Cart\")]")
    
    @property 
    def login_button(self):
        return self.browser.find_element(By.ID, "login2")
    
    def open_login(self):
        self.login_button.click()
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-content")))
    
    @property 
    def signup_button(self):
        return self.browser.find_element(By.ID, "signin2")
    
    def open_signup(self):
        self.signup_button.click()
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))

    