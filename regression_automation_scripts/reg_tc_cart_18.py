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

driver.find_element(By.LINK_TEXT,"Books").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Computing and Internet")))

wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Computing and Internet"))).click()
wait.until(EC.element_to_be_clickable((By.ID,"add-to-cart-button-13"))).click()
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='cart-label']"))).click()
wait = WebDriverWait(driver, 10)
cart_qty = wait.until(EC.presence_of_element_located((By.XPATH,"//input[contains(@class,'qty-input')]")))
cart_qty.clear()
cart_qty.send_keys("3.5")
updated_qty = cart_qty.get_attribute("value")
driver.find_element(By.NAME, "updatecart").click()
if updated_qty != "3.5":
    print("Decimal value is rejected")

else:
    print("Decimal value is accepted")

assert updated_qty !="3.5", "Decimal value should not be accepted!"



