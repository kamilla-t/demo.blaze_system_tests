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

    @property 
    def cart_table(self):
        return self.browser.find_element(By.ID, "tbodyid")
    
    def cart_row(self, row_number):
        rows = self.cart_table.find_elements(By.TAG_NAME, "tr")
        return rows[row_number]
    
    def cart_cell(self, row_number, column_number):
        cells = self.cart_row(row_number).find_elements(By.TAG_NAME, "td")
        return cells[column_number]
    
    def delete_row(self, row_number):
        delete_cell = self.cart_cell(row_number, column_number=3)
        delete_cell.find_element(By.TAG_NAME, "a").click()
    