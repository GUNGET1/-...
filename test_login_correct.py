from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Firefox()
driver.get('https://xn--80aairftm.xn--d1acvi.xn--80aswg/index.php?route=account/login&language=ru-ru')

driver.find_element(By.NAME, 'email').send_keys('15@gmail.com')
driver.find_element(By.NAME, 'password').send_keys('12345678')
driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

# time.sleep(5)

driver.quit()