import os

import pytest

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions

from dotenv import load_dotenv
from wrm_selene_python_hw_11_jenkins.utils import attach

'''
@pytest.fixture(scope='function', autouse=True)
def browser_control():
    browser.config.hold_browser_open = True
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = '1240'
    browser.config.window_height = '768'
    browser.config.timeout = 6.0
'''
DEFAULT_BROWSER_MODE = 'selenoid'
DEFAULT_BROWSER = 'chrome'
DEFAULT_BROWSER_VERSION = '115.0'

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_mode",
        action="store",
        choices=["local", "selenoid"],
        default=DEFAULT_BROWSER_MODE,
        help="Specify the browser mode: 'local' for local browser or 'selenoid' for Selenoid",
    )

    parser.addoption(
        "--browser_name",
        action="store",
        choices=["chrome", "edge", "firefox", "safari"],
        default=DEFAULT_BROWSER,
        help="Specify the browser name: 'chrome', 'edge', 'firefox', safari",
    )

    parser.addoption(
        "--browser_version",
        action="store",
        default=DEFAULT_BROWSER_VERSION,
        help="Specify the browser version - chrome: 115.0, edge: 114.0, firefox: 115.0, safari: 15.0"
    )

@pytest.fixture(scope="session")
def get_option_browser_mode(request):
    return request.config.getoption("--browser_mode")

@pytest.fixture(scope='session')
def get_option_browser_name(request):
    return request.config.getoption('--browser_name')

@pytest.fixture(scope='session')
def get_option_browser_version(request):
    return request.config.getoption('--browser_name')

@pytest.fixture(scope='function', autouse=True)
def browser_control(get_option_browser_mode, get_option_browser_name, get_option_browser_version):
    browser.config.hold_browser_open = 'True'
    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = '1240'
    browser.config.window_height = '768'
    browser.config.timeout = 6.0

    browser_mode = get_option_browser_mode if get_option_browser_mode != '' \
        else DEFAULT_BROWSER_MODE
    browser_name = get_option_browser_name if get_option_browser_name != ''\
        else DEFAULT_BROWSER
    # browser_name = get_option_browser_name or DEFAULT_BROWSER
    browser_version = get_option_browser_version if get_option_browser_version != '' \
        else DEFAULT_BROWSER_VERSION

    if browser_mode == "selenoid":
        options = Options()
        selenoid_capabilities = {
            # "browserName": browser_name,
            # "browserVersion": browser_version,
            "browserName": 'firefox',
            "browserVersion": '115.0',
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)




        login = os.getenv('SELENOID_LOGIN')
        password = os.getenv('SELENOID_PASSWORD')

        browser.config.driver = webdriver.Remote(
            # command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
            command_executor="http://8.211.9.7:4444/wd/hub",
            # desired_capabilities=selenoid_capabilities
            options=options
        )

    yield browser
    # attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)
    browser.quit()

    # attach.add_html(browser)
    # attach.add_screenshot(browser)
    # attach.add_video(browser)
    # if browser_name == 'chrome':
    #     attach.add_logs(browser)
    # browser.quit()
