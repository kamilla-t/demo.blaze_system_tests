from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class PlaceOrder(BasePage):

    @property 
    def name(self):
        return self.browser.find_element(By.ID, "name")
    
    @property 
    def country(self):
        return self.browser.find_element(By.ID, "country")
    
    @property 
    def city(self):
        return self.browser.find_element(By.ID, "city")
    
    @property 
    def credit_card(self):
        return self.browser.find_element(By.ID, "card")
    
    @property 
    def month(self):
        return self.browser.find_element(By.ID, "month")
    
    @property 
    def year(self):
        return self.browser.find_element(By.ID, "year")
    
    @property 
    def purchase_button(self):
        return self.browser.find_element(By.XPATH, "//button[contains(text(), \"Purchase\")]")
    
    @property 
    def close_button(self):
        return self.browser.find_element(By.XPATH, "//button[contains(text(), \"Close\")]")
    
    def fill_place_order(self, name, country, city, card, month, year):
        self.name.send_keys(name)
        self.country.send_keys(country)
        self.city.send_keys(city)
        self.credit_card.send_keys(card)
        self.month.send_keys(month)
        self.year.send_keys(year)
        self.purchase_button.click()



