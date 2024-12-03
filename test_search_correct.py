from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Firefox()
driver.get('https://www.google.com')


try:
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'L2AGLb'))
    ).click()
except:
    pass


search_term = 'Python Selenium'


search_box = driver.find_element(By.NAME, 'q')
search_box.clear()
search_box.send_keys(search_term)
search_box.send_keys(Keys.RETURN)


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.g'))
)
results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
assert len(results) > 0  # Будет эррорка, если пусто
assert any(search_term.lower() in result.text.lower() for result in results)


# time.sleep(10)

driver.quit()
