import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton
from os import path

APP_DIR = path.dirname(path.abspath("../prep_work/"))
APP = path.join(APP_DIR, 'TheApp.app.zip')
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'iOS',
    'platformVersion': '15.5',
    'deviceName': 'iPhone 11 Pro Max',
    'automationName': 'XCUITest',
    'bundleId': 'com.apple.Maps',
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)


def press(driver, X, Y, duration):
    tap = ActionBuilder(driver)
    finger = tap.add_pointer_input(POINTER_TOUCH, 'finger')
    finger.create_pointer_move(duration=0, x=X, y=Y)
    finger.create_pointer_down(duration=duration)
    finger.create_pointer_up(MouseButton.LEFT)
    tap.perform()


def zoom(driver, X, Y):
    zoom: ActionBuilder = ActionBuilder(driver)
    finger1 = zoom.add_pointer_input(POINTER_TOUCH, 'finger1')
    finger1.create_pointer_move(duration=0, x=X - 50, y=Y - 50)
    finger1.create_pointer_down(button=MouseButton.LEFT)
    finger1.create_pointer_move(duration=250, x=-100, y=-150, origin="pointer")
    finger1.create_pointer_up(MouseButton.LEFT)
    finger2 = zoom.add_pointer_input(POINTER_TOUCH, 'finger2')
    finger2.create_pointer_move(duration=0, x=X + 50, y=X + 50)
    finger2.create_pointer_down(button=MouseButton.LEFT)
    finger2.create_pointer_move(duration=250, x=100, y=150, origin="pointer")
    finger2.create_pointer_up(MouseButton.LEFT)
    zoom.perform()


try:
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Search Maps')
    )).send_keys("Vancouver, BC")

    wait.until(ec.presence_of_element_located(
        (MobileBy.XPATH, '//XCUIElementTypeStaticText[@label="Vancouver, BC"]')
    )).click()

    rect = wait.until(ec.presence_of_element_located(
        (MobileBy.XPATH, '//XCUIElementTypeOther[@label="Stanley Park"]')
    )).rect

    X = int(rect["x"] + rect["width"] / 2)
    Y = int(rect["y"] + rect["height"] / 2)

    press(driver, X, Y, 500)

    preview = wait.until(ec.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Preview')
    ))

    assert preview

    press(driver, int(preview.rect['x'] + preview.rect['width'] + 100),
          int(preview.rect['y'] + preview.rect['height'] + 100), 0)

    zoom(driver, X, Y)

    time.sleep(5)

    driver.get_screenshot_as_base64()

finally:
    driver.quit()
