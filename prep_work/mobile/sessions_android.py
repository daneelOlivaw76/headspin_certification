from appium import webdriver
from os import path

APP_DIR = path.dirname(path.abspath("../prep_work/"))
APP = path.join(APP_DIR, 'TheApp.apk')
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'Android',
    'deviceName': 'Pixel 5 API 31',
    'automationName': 'UiAutomator2',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

driver.quit()
