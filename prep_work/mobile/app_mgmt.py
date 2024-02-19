import time
from typing import Any, Dict
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from os import path

APP_DIR = path.dirname(path.abspath("../prep_work/"))
APP = path.join(APP_DIR, 'TheApp.apk')
APPIUM = 'http://localhost:4723'

CAPS: Dict[str, str] = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'automationName': 'UiAutomator2',
    'app': APP,
}

driver: Any = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

app: str = path.join(APP_DIR, 'ApiDemos.apk')
app_id = 'io.appium.android.apis'

try:
    #driver.remove_app(app_id)
    driver.install_app(app)
    driver.activate_app(app_id)
    time.sleep(3)
    driver.terminate_app(app_id)

finally:
    driver.quit()
