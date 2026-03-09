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
search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
search_box.send_keys("Gift Card")


driver.find_element(By.CSS_SELECTOR,"input[class='button-1 search-box-button']").click()

wait = WebDriverWait(driver, 10)


sort_by=driver.find_element(By.ID,"products-orderby")
select = Select(sort_by)
select.select_by_visible_text("Price: Low to High")

price_elements = wait.until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR, "div.item-box span.price")))

prices = []

for price in price_elements:
    price_text = price.text.strip().replace("$","").replace(",","")
    prices.append(float(price_text))

if prices == sorted(prices):
    print("sorted from low to high")

else:
    print("Prices not sorted")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.quit()