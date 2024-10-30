import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# Command-line option to specify the browser
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--hub_url", help="URL of the Selenium Grid Hub")
    parser.addoption("--node_url", action="store", default=None, help="Node URL for Selenium Grid")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def hub_url(request):
    return request.config.getoption("--hub_url")

@pytest.fixture()
def setup(browser, request, hub_url):
    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--start-maximized")
    elif browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
    elif browser == 'edge':
        options = EdgeOptions()
        options.add_argument("--start-maximized")
    else:
        options = ChromeOptions()
    driver = webdriver.Remote(command_executor=hub_url,options=options)
    driver.maximize_window()
    driver.get("https://ui.cogmento.com/")

    def teardown():
        driver.quit()
    request.addfinalizer(teardown)

    return driver

@pytest.fixture()
def setup_incorrect_url(browser, request, hub_url):
    if browser == 'chrome':
        options = ChromeOptions()
    elif browser == 'firefox':
        options = FirefoxOptions()
    elif browser == 'edge':
        options = EdgeOptions()
    else:
        options = ChromeOptions()

    driver = webdriver.Remote(command_executor=hub_url,options=options)

    driver.maximize_window()
    driver.get("https://invaliddomain.com/")
    time.sleep(5)

    def teardown():
        driver.quit()
    request.addfinalizer(teardown)

    return driver


#
# import time
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture()
# def setup(browser, request):
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#     elif browser == 'firefox':
#         driver = webdriver.Firefox()
#     elif browser == 'edge':
#         driver = webdriver.Edge()
#     else:
#         driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://ui.cogmento.com/")
#
#     def teardown():
#         driver.quit()
#     request.addfinalizer(teardown)
#     return driver
#
# @pytest.fixture()
# def setup_incorrect_url(browser, request):
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#     elif browser == 'firefox':
#         driver = webdriver.Firefox()
#     elif browser == 'edge':
#         driver = webdriver.Edge()
#     else:
#         driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://invaliddomain.com/")
#     time.sleep(10)
#
#     def teardown():
#         driver.quit()
#     request.addfinalizer(teardown)
#     return driver


