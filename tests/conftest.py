import os

import pytest

from selene import browser
from selenium import webdriver

from dotenv import load_dotenv

'''
@pytest.fixture(scope='function', autouse=True)
def browser_control():
    browser.config.hold_browser_open = True
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = '1240'
    browser.config.window_height = '768'
    browser.config.timeout = 6.0
'''


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_control():
    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = '1240'
    browser.config.window_height = '768'
    browser.config.timeout = 6.0

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASSWORD')

    browser.config.driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        desired_capabilities=selenoid_capabilities
    )

    yield
    browser.quit()
