from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# open the website
link = "https://www.demoblaze.com/"
browser = webdriver.Chrome()
browser.get(link)

# process of sign up
signup_button = browser.find_element(By.ID, "signin2")
signup_button.click()

login_input = browser.find_element(By.ID, "sign-username")
login_input.send_keys("Kamilla")

password_input = browser.find_element(By.ID, "sign-password")
password_input.send_keys("admin123")

submit_button = browser.find_element(By.XPATH, "//button[text()=\"Sign up\"]")
submit_button.click()

alert = browser.switch_to.alert
alert.accept()

# process of log in
login_button = browser.find_element(By.ID, "login2")
login_button.click()

login_username = browser.find_element(By.ID, "loginusername")
login_username.send_keys("Kamilla")

password_username = browser.find_element(By.ID, "loginpassword")
password_input.send_keys("admin123")

login_button = browser.find_element(By.XPATH, "//button[text()=\"Log in\"]")
login_button.click()



browser.quit()


