from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://www.gmail.com")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='email']"))).send_keys("email.tester140@gmail.com")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']"))).send_keys("shajid1404046")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'T-I T-I-KE L3']"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='agP aFw']"))).send_keys("zaberayon@gmail.com")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='subjectbox']"))).send_keys("Selenium email")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Am Al editable LW-avf tS-tW']"))).send_keys("Hello, First email via selenium")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'T-I J-J5-Ji aoO v7 T-I-atl L3']"))).click()
time.sleep(30)
driver.quit()