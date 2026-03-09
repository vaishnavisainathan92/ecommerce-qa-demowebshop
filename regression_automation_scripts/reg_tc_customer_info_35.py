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

wait = WebDriverWait(driver, 10)
driver.find_element(By.LINK_TEXT,"Log in").click()
driver.find_element(By.ID,"Email").send_keys("johnAdams1@gmail.com")
driver.find_element(By.ID,"Password").send_keys("abc@123")
driver.find_element(By.CSS_SELECTOR,"input[value='Log in']").click()

wait= WebDriverWait(driver,15)
wait.until(EC.presence_of_element_located((By.XPATH,"//a[@class='account']"))).click()
First_name = wait.until(EC.presence_of_element_located((By.ID,"FirstName")))
First_name.clear()


driver.find_element(By.XPATH,"//input[@class='button-1 save-customer-info-button']").click()

validation_error = wait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='field-validation-error']"))).text

print("The validation message is:",validation_error)

assert "First", "No validation message"
print("Field validation error message is displayed")
driver.quit()

driver.quit()