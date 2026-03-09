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

wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Apparel & Shoes"))).click()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"50's Rockabilly Polka Dot Top JR Plus Size"))).click()
Size=driver.find_element(By.ID,"product_attribute_5_7_1")
select = Select(Size)
select.select_by_visible_text("5X")

driver.find_element(By.ID,"add-to-cart-button-5").click()
driver.find_element(By.LINK_TEXT,"Shopping cart").click()
Selected_size=wait.until(EC.presence_of_element_located((By.XPATH,"(//div[@class='attributes'][normalize-space()='Size: 5X'])[2]"))).text
print("The selected size is:",Selected_size)

assert "5X",("Selected size not displayed")
print("Selected size displayed")

driver.quit()





