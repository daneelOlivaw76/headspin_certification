from selenium import webdriver
from selenium.webdriver.common.by import By

page = 'https://the-internet.herokuapp.com/'

driver = webdriver.Firefox()

try:
    driver.get(page)

    driver.find_element(By.LINK_TEXT, 'Form Authentication')

    els = driver.find_elements(By.TAG_NAME, 'a')
    print(f'There were {len(els)} anchor elements')

    els = driver.find_elements(By.TAG_NAME, 'foo')
    print(f'There were {len(els)} foo elements')
finally:
    driver.quit()
