from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class HomeView(object):
    ECHO_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Echo Box')

    def __init__(self, driver):
        self.driver = driver

    def nav_to_echo_box(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located(self.ECHO_ITEM)).click()
