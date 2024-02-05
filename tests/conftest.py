from selenium import webdriver
import pytest
from configs.config import Config

from demoblaze import DemoBlaze


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="",
                     help="Choose env: dev or empty for production")


@pytest.fixture(scope = "function")
def config(request):
    return Config(env=request.config.getoption("env"))


@pytest.fixture(scope = "function")
def browser(config):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # get link from config.py file
    link = config.Url
    browser.get(link)
    yield browser
    print("\nquit browser..")


@pytest.fixture()
def demoblaze(browser):
    demoblaze_app = DemoBlaze(browser)
    yield demoblaze_app
    demoblaze_app.quit()
