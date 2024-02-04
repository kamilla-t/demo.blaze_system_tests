from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AboutUs(BasePage):
    
    @property
    def is_open(self):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located((By.ID, "videoModal")))
            return True
        except:
            return False

    @property
    def close_button(self):
        return self.browser.find_element(By.XPATH, "//button[text()=\"Close\"]")