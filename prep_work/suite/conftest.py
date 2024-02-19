from appium import webdriver
from os import path
import pytest

APP_DIR = path.dirname(path.abspath(__file__))
APP = path.join(APP_DIR, '..', 'TheApp.app.zip')
APPIUM = 'http://localhost:4723'


@pytest.fixture
def driver_ios():
    CAPS = {
        'platformName': 'iOS',
        'plaformVersion': '16.4',
        'deviceName': 'iPhone 14',
        'automationName': 'XCUITest',
        'app': APP,
    }

    driver = webdriver.Remote(
        command_executor=APPIUM,
        desired_capabilities=CAPS
    )
    # using yield instead of return, so that after code using the driver is finished,
    # execution will return here
    yield driver
    driver.quit()
