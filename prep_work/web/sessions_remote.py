from selenium import webdriver

caps = {
    'browserName': 'firefox'
}

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444',
    desired_capabilities=caps
)

try:
    driver.get()
finally:
    driver.quit()
