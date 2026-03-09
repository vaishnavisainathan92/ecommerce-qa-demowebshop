import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
driver.find_element(By.LINK_TEXT,"Log in").click()
driver.find_element(By.XPATH,"//input[@value='Register']").click()

driver.find_element(By.ID,"gender-male").click()

driver.find_element(By.ID,"FirstName").send_keys("John")
driver.find_element(By.ID,"LastName").send_keys("Adams")
driver.find_element(By.ID,"Email").send_keys("johnAdams57@gmail.com")
driver.find_element(By.ID,"Password").send_keys("abc@1233")
driver.find_element(By.XPATH,"//input[@id='ConfirmPassword']").send_keys("abc@1233")
driver.find_element(By.XPATH,"//input[@name='register-button']").click()

wait = WebDriverWait(driver,10)

success_msg = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "result"))
).text

print("Actual message:", success_msg)

assert "registration completed" in success_msg.lower()
print("Customer Registered successfully")

