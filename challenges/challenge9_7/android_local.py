import time
from os import path
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'automationName': 'UiAutomator2',
    'appium:appPackage': 'com.appiumpro.the_app',
    'appium:appActivity': '.MainActivity'
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

url = 'https://the-internet.herokuapp.com/'
login_url = 'https://the-internet.herokuapp.com/login'


class webview_active(object):  # wait.until(webview.active())

    def __call__(self, driver):
        for context in driver.contexts:
            if context != 'NATIVE_APP':
                driver.switch_to.context(context)
                return True
        return False


def login(driver, wait):
    form_auth_link = wait.until(ec.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')
    ))

    form_auth_link.click()

    username = wait.until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, '#username')
    ))
    username.send_keys('tomsmith')

    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('SuperSecretPassword!')
    driver.hide_keyboard()

    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    # time.sleep(5)

    wait.until(ec.presence_of_element_located(
        (By.LINK_TEXT, 'Logout')
    )).click()

    wait.until(ec.url_to_be(login_url))

    flash = wait.until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, '#flash')
    ))

    assert 'logged out' in flash.text


try:
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Webview Demo'))).click()
    wait.until(ec.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'urlInput'))).send_keys(url)
    driver.find_element(MobileBy.ACCESSIBILITY_ID, 'navigateBtn').click()
    wait.until(ec.presence_of_element_located(
        (MobileBy.XPATH, '*//android.widget.Button[@text="OK"]'))).click()

    webview = wait.until(webview_active())
    driver.get(url)
    print(f'Current URL: {driver.current_url}')
    print(f'Title: {driver.title}')

    login(driver, wait)

    driver.switch_to.context('NATIVE_APP')
    driver.find_element(MobileBy.ACCESSIBILITY_ID, 'clearBtn').click()
    # time.sleep(5)
finally:
    driver.quit()