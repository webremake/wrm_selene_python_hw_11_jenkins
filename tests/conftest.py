import os

import pytest

from selene import browser
from selenium import webdriver

from dotenv import load_dotenv
from wrm_selene_python_hw_11_jenkins.utils import attach

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


def pytest_addoption(parser):
    parser.addoption(
        "--browser_mode",
        action="store",
        choices=["local", "selenoid"],
        default="local",
        help="Specify the browser mode: 'local' for local browser or 'selenoid' for Selenoid",
    )


@pytest.fixture(scope="session")
def browser_mode(request):
    return request.config.getoption("--browser_mode")


@pytest.fixture(scope='function', autouse=True)
def browser_control(browser_mode):
    browser.config.hold_browser_open = 'True'
    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = '1240'
    browser.config.window_height = '768'
    browser.config.timeout = 6.0

    if browser_mode == "selenoid":
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "100.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        login = os.getenv('SELENOID_LOGIN')
        password = os.getenv('SELENOID_PASSWORD')

        browser.config.driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
            desired_capabilities=selenoid_capabilities
        )

    yield browser
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)
    browser.quit()
