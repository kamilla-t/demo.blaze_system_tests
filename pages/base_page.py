from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage():

    def __init__(self, browser) -> None:
        self.browser = browser
