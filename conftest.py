""" Fixtures and hooks for pytest """
import pytest
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@fixture(scope='function')
def browser(request):
    """ returns a webdriver of selected browser """
    s_b = request.config.getoption('--browser', default="chrome")
    if s_b == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif s_b == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif s_b == 'edge':
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    else:
        print(f"Undefined browser requested: {s_b}. Available options: chrome, firefox, edge.")
        raise Exception()
        return
    driver.maximize_window()
    yield driver
    driver.close()