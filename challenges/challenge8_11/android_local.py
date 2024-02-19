import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton
from os import path
import math

APP_DIR = path.dirname(path.abspath('../../prep_work/**'))
APP = path.join(APP_DIR, 'ApiDemos.apk')
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'automationName': 'UiAutomator2',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)


def press(driver, X, Y, drag_duration, down_duration, draw_duration):
    tap = ActionBuilder(driver)
    finger = tap.add_pointer_input(POINTER_TOUCH, 'finger')
    finger.create_pointer_move(duration=drag_duration, x=X, y=Y)
    finger.create_pointer_down(duration=down_duration)
    finger.create_pointer_move(duration=draw_duration, x=-100, y=-150, origin="pointer")
    finger.create_pointer_up(MouseButton.LEFT)
    tap.perform()


def draw(driver):
    press(driver, 100, 100, 0, 0, 100)


def draw_lines(driver, center_x, center_y, radius):
    tap = ActionBuilder(driver)
    finger1 = tap.add_pointer_input(POINTER_TOUCH, 'finger1')
    finger1.create_pointer_move(duration=0, x=center_x, y=(center_y + radius))
    finger1.create_pointer_down()
    finger1.create_pointer_move(duration=150, x=0, y=-(2 * radius), origin="pointer")
    finger1.create_pointer_up(MouseButton.LEFT)
    tap.perform()

    tap2 = ActionBuilder(driver)
    finger2 = tap2.add_pointer_input(POINTER_TOUCH, 'finger2')
    finger2.create_pointer_move(duration=0, x=(center_x + radius), y=center_y)
    finger2.create_pointer_down()
    finger2.create_pointer_move(duration=150, x=-(2 * radius), y=0, origin="pointer")
    finger2.create_pointer_up(MouseButton.LEFT)
    tap2.perform()


def draw_circle(drive, center_x, center_y, radius):
    print("Starting to print circle")
    print(f"radius: {radius}")
    number_sides = 4
    line_length = math.pi / number_sides
    # tap_circle = ActionBuilder(driver)
    for k in range(number_sides):
        tap_circle = ActionBuilder(driver)
        arc_length = radius / 4
        print(f"drawing side {k} of {number_sides}")
        start_circle_x = center_x + math.trunc(radius * math.cos(line_length * k))
        start_circle_y = center_y + math.trunc(radius * math.sin(line_length * k))
        end_circle_x = center_x + math.trunc(radius * math.cos(line_length * (k + 1)))
        end_circle_y = center_y + math.trunc(radius * math.sin(line_length * (k + 1)))
        print(f"initial x coordinate: {start_circle_x}")
        print(f"initial y coordinate: {start_circle_y}")
        print(f"final x coordinate: {end_circle_x}")
        print(f"final y coordinate: {end_circle_y}")
        circle_arc = tap_circle.add_pointer_input(POINTER_TOUCH, f"circle_arc_{k}")
        circle_arc.create_pointer_move(duration=0, x=start_circle_x, y=start_circle_y)
        circle_arc.create_pointer_down()
        circle_arc.create_pointer_move(duration=150, x=end_circle_x, y=end_circle_y, origin="pointer")
        circle_arc.create_pointer_up(MouseButton.LEFT)
        tap_circle.perform()
    # tap_circle.perform()


try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Graphics')
    )).click()

    rect = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'BitmapMesh')
    )).rect

    press(driver, int(rect['x']), int(rect['y']), 150, 0, 0)

    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'FingerPaint')
    )).click()

    wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.TextView[@text="Graphics/FingerPaint"]')
    ))

    # draw function
    size = driver.get_window_rect()
    center_x = int(size['width'] / 2)
    center_y = int(size['height'] / 2)
    radius = int(size['width'] * 0.4)

    draw_lines(driver, center_x, center_y, radius)
    draw_circle(driver, center_x, center_y, radius)
    time.sleep(5)

finally:
    driver.quit()
