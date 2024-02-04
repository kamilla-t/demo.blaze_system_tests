from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage(BasePage):

    @property
    def is_open(self):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located((By.ID, "exampleModal")))
            return True
        except:
            return False
    
    @property
    def contact_email(self):
        return self.browser.find_element(By.ID, "recipient-email")

    @property
    def contact_name(self):
        return self.browser.find_element(By.ID, "recipient-name")

    @property
    def contact_message(self):
        return self.browser.find_element(By.ID, "message-text")

    @property
    def send_message_button(self):
        return self.browser.find_element(By.XPATH, "//button[text()=\"Send message\"]")

    @property
    def close_button(self):
        return self.browser.find_element(By.XPATH, "//button[text()=\"Close\"]")
    
    def fill_contact(self, email, name, message):
        self.contact_email.send_keys(email)
        self.contact_name.send_keys(name)
        self.contact_message.send_keys(message)
        self.send_message_button.click()
        