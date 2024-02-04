from pages.about_us import AboutUs
from pages.cart import Cart
from pages.contact_page import ContactPage
from pages.footer import Footer
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.navbar import Navbar
from pages.place_order import PlaceOrder
from pages.sign_up import SignUpPage

class DemoBlaze():
    def __init__(self, browser) -> None:
        self.browser = browser

    @property
    def alert(self):
        return self.main_page.alert

    def quit(self):
        self.browser.quit()
    
    @property 
    def about_us(self):
        return AboutUs(self.browser)
    
    @property
    def cart(self):
        return Cart(self.browser)
    
    @property
    def contact_page(self):
        return ContactPage(self.browser)
    
    @property
    def footer(self):
        return Footer(self.browser)
    
    @property
    def login_page(self):
        return LoginPage(self.browser)
    
    @property
    def main_page(self):
        return MainPage(self.browser)
    
    @property 
    def navbar(self):
        return Navbar(self.browser)
    
    @property
    def place_order(self):
        return PlaceOrder(self.browser)
    
    @property 
    def sign_up(self):
        return SignUpPage(self.browser)

    
    