import time
from typing import final

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options




chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=chrome_options)


driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
driver.find_element(By.LINK_TEXT,"Log in").click()
driver.find_element(By.CSS_SELECTOR,"[id='Email']").send_keys("johnAdams1@")
driver.find_element(By.CSS_SELECTOR,"[id='Password']").send_keys("abc@123")
driver.find_element(By.CSS_SELECTOR,"input[value='Log in']").click()

wait = WebDriverWait(driver,10)
warning_msg=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.field-validation-error"))).text
print("Warning message:", warning_msg)
assert "valid email address" in warning_msg
print("Proper validation message displayed")
