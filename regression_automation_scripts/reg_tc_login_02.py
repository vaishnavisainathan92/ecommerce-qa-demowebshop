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
driver.find_element(By.CSS_SELECTOR,"[id='Email']").send_keys("johnAdams1@gmail.com")
driver.find_element(By.CSS_SELECTOR,"[id='Password']").send_keys("abc@123")
driver.find_element(By.CSS_SELECTOR,"input[value='Log in']").click()
from selenium.webdriver.support import expected_conditions as EC


wait = WebDriverWait(driver,10)
logout_link = wait.until(presence_of_element_located((By.LINK_TEXT,"Log out")))


assert logout_link.is_displayed()

print("Log in successful")


