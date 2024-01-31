from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    
    @property
    def slider(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".carousel-inner")
    
    @property
    def slider_left_arrow(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".carousel-control-prev-icon")
    
    @property
    def slider_right_arrow(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon")
    
    # categories
    @property
    def categories(self):
        return self.browser.find_elements(By.ID, "itemc")
    
    def category(self, category_name):
        for category in self.categories:
            if category_name.lower() in category.text.lower():
                return category
        return None
    
    # cards
    @property
    def cards(self):
        return self.browser.find_elements(By.CSS_SELECTOR, ".card")
    
    @property 
    def cards_name(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".card-title")
    
    @property 
    def cards_price(self):
        return self.browser.find_element(By.XPATH, "//div[@class=\"card-block\"]/h5")
    
    @property 
    def cards_description(self):
        return self.browser.find_element(By.XPATH, "//p[@id=\"article\"]")
    
    def card(self, name:str=None, price:str=None, description:str=None):
        if name is not None:
            for card in self.cards:
                card_name = card.find_element(By.CSS_SELECTOR, ".card-title a")
                if name.lower() in card_name.text.lower():
                    return card
    
        if price is not None:
            for card in self.cards:
                card_price = card.find_element(By.XPATH, "//div[@class=\"card-block\"]/h5")
                if price.lower() in card_price.text.lower():
                    return card
        
        if description is not None:
            for card in self.cards:
                card_description = card.find_element(By.XPATH, "//p[@id=\"article\"]")
                if description.lower() in card_description.text.lower():
                    return card
            
        return None
    
    def open_card(self, name:str=None, price:str=None, description:str=None):
        card = self.card(name, price, description)
        card.find_element(By.CSS_SELECTOR, ".card-title a").click()
