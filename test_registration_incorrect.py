from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://xn--80aairftm.xn--d1acvi.xn--80aswg/index.php?route=account/register&language=ru-ru')

driver.find_element(By.ID, 'input-firstname').send_keys('Никита')
driver.find_element(By.ID, 'input-lastname').send_keys('Никитенко')
driver.find_element(By.ID, 'input-email').send_keys('i')
driver.find_element(By.ID, 'input-password').send_keys('sec')
driver.find_element(By.NAME, 'agree').click()

driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

# time.sleep(5)

driver.quit()