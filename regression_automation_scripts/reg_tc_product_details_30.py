import time
from typing import final

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options



chrome_options = Options()

chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
prefs = {"credentials_enable_service": False,"profile.password_manager_enabled": False}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
wait=WebDriverWait(driver,10)

wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Books"))).click()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Computing and Internet"))).click()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Add your review"))).click()
validation_message = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='validation-summary-errors']"))).text
print("Validation message is:",validation_message)

assert "Only","No validation message"
print("Validation message is displayed successfully!")
driver.quit()