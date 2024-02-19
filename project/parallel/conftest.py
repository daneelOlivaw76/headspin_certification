import pytest
from os import path
from appium import webdriver

from views.home_view import HomeView

CUR_DIR = path.dirname(path.abspath(__file__))
IOS_APP = path.join(CUR_DIR, '..', 'mobile', 'TheApp.app.zip')
ANDROID_APP = path.join(CUR_DIR, '..', 'mobile', 'TheApp.apk')
APPIUMS = ['http://localhost:4700', 'http://localhost:4701']

IOS_CAPS = [{
    'platformName': 'iOS',
    'platformVersion': '13.6',
    'deviceName': 'iPhone 11',
    'automationName': 'XCUITest',
    'app': IOS_APP,
}, {
    'platformName': 'iOS',
    'platformVersion': '13.6',
    'deviceName': 'iPhone 8',
    'automationName': 'XCUITest',
    'app': IOS_APP,
}]

ANDROID_CAPS = [{
    'platformName': 'Android',
    'platformVersion': '10.0',
    'deviceName': 'Android Emulator',
    'automationName': 'UiAutomator2',
    'app': ANDROID_APP,
}]


def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default='ios')


@pytest.fixture
def worker_num(worker_id):
    if worker_id == 'master':
        worker_id = 'gw0'
    return int(worker_id[2:])


@pytest.fixture
def platform(request):
    plat = request.config.getoption('platform').lower()
    if plat not in ['ios', 'android']:
        raise ValueError('--platform value must be ios or android')
    return plat


@pytest.fixture
def caps(platform, worker_num):
    cap_set = IOS_CAPS if platform == 'ios' else ANDROID_CAPS
    if worker_num >= len(cap_set):
        raise Exception('Too many workers for the number of capability options.')
    return cap_set[worker_num]


@pytest.fixture
def server(worker_num):
    if worker_num >= len(APPIUMS):
        raise Exception('Too many workers for the number of Appium servers')
    return APPIUMS[worker_num]


@pytest.fixture
def driver(server, caps, platform):
    driver = webdriver.Remote(server, caps)
    driver._platform = platform
    yield driver
    driver.quit()


@pytest.fixture
def home(driver):
    return HomeView.instance(driver)
