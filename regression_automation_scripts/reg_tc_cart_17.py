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
driver.find_element(By.LINK_TEXT,"Log in").click()
driver.find_element(By.ID,"Email").send_keys("johnAdams1@gmail.com")
driver.find_element(By.ID,"Password").send_keys("abc@123")
driver.find_element(By.CSS_SELECTOR,"input[value='Log in']").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
search_box.send_keys("Blue Jeans")
driver.find_element(By.CSS_SELECTOR,"input[class='button-1 search-box-button']").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Blue Jeans"))).click()
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID,"add-to-cart-button-36"))).click()
driver.find_element(By.XPATH,"//span[@class='cart-label']").click()
wait = WebDriverWait(driver, 10)
cart_qty = wait.until(EC.presence_of_element_located((By.XPATH,"//input[contains(@class,'qty-input')]")))
cart_qty.clear()
cart_qty.send_keys("3")

updated_qty = cart_qty.get_attribute("value")

if updated_qty=="3":
    print("Quantity is updated" )
else:
    print("Quantity is not updated")


assert updated_qty =="3","update failed"