from selenium import webdriver
import pytest

from demoblaze import DemoBlaze

@pytest.fixture(scope = "function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    link = "https://www.demoblaze.com/"
    browser.get(link)
    yield browser
    print("\nquit browser..")


@pytest.fixture()
def demoblaze(browser):
    demoblaze_app = DemoBlaze(browser)
    yield demoblaze_app
    demoblaze_app.quit()
