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
wait = WebDriverWait(driver, 10)
driver.find_element(By.LINK_TEXT,"Log in").click()
driver.find_element(By.ID,"Email").send_keys("johnAdams1@gmail.com")
driver.find_element(By.ID,"Password").send_keys("abc@123")
driver.find_element(By.CSS_SELECTOR,"input[value='Log in']").click()

wait= WebDriverWait(driver,15)
wait.until(EC.presence_of_element_located((By.XPATH,"//a[@class='account']")))
wait.until(EC.element_to_be_clickable((By.XPATH,"//li[@class='inactive']//a[normalize-space()='Jewelry']"))).click()

wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Black & White Diamond Heart"))).click()

price = driver.find_element(By.XPATH,"//span[@class='price-value-14']").text
print("The product price is:",price)

assert "130.00" in price

print("The product price is displayed successfully")

product_name = driver.find_element(By.XPATH,"//div[@class='product-name']").text
print("The product name is:",product_name)

assert "Black" ,"the product name is not displayed"
print("The product name is displayed successfully")

product_description = driver.find_element(By.XPATH,"//div[@class='full-description']").text

assert "Bold" in product_description
print("The product description is displayed successfully")
driver.quit()