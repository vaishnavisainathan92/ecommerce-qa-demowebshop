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

driver.find_element(By.ID,"small-searchterms").click()
driver.find_element(By.ID,"small-searchterms").send_keys("50's Rockabilly Polka Dot Top JR Plus Size")

driver.find_element(By.CSS_SELECTOR,"input[class='button-1 search-box-button']").click()

driver.find_element(By.LINK_TEXT,"50's Rockabilly Polka Dot Top JR Plus Size").click()
Size = driver.find_element(By.ID,"product_attribute_5_7_1")
select = Select(Size)
select.select_by_visible_text("2X")

driver.find_element(By.ID,"add-to-cart-button-5").click()
driver.find_element(By.XPATH,"//span[@class='cart-label'][1]").click()

wait = WebDriverWait(driver,10)
items_check = wait.until(EC.presence_of_element_located((By.LINK_TEXT,"50's Rockabilly Polka Dot Top JR Plus Size")))

assert items_check.is_displayed()
print("Item is added to the cart successfully")