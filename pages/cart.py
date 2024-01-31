from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cart(BasePage):

    @property 
    def place_order_button(self):
        return self.browser.find_element(By.XPATH, "//button[contains(text(), \"Place Order\")]")
    
    def open_place_order(self):
        self.place_order_button.click()
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-content")))