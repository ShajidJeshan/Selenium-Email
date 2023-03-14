from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://www.amazon.com")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='field-keywords']"))).send_keys("laptop")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type = 'submit']"))).click()
time.sleep(30)
driver.quit()