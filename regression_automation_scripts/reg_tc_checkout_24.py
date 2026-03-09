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

wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Apparel & Shoes"))).click()
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Blue Jeans"))).click()
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID,"add-to-cart-button-36"))).click()
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='cart-label']"))).click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.cart")))
wait.until(EC.element_to_be_clickable((By.ID,"termsofservice"))).click()
wait.until(EC.element_to_be_clickable((By.NAME,"checkout"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@value='Checkout as Guest']"))).click()


driver.find_element(By.ID,"BillingNewAddress_LastName").send_keys("Smith")
driver.find_element(By.ID,"BillingNewAddress_Email").send_keys("j.smith@hotmail.com")
country = driver.find_element(By.ID,"BillingNewAddress_CountryId")
select = Select(country)
select.select_by_visible_text("United States")
driver.find_element(By.ID,"BillingNewAddress_City").send_keys("Malden")
driver.find_element(By.ID,"BillingNewAddress_Address1").send_keys("Florence street")
driver.find_element(By.ID,"BillingNewAddress_ZipPostalCode").send_keys("12345")
driver.find_element(By.ID,"BillingNewAddress_PhoneNumber").send_keys("123456789")
driver.find_element(By.ID,"BillingNewAddress_Company").send_keys("NONE")

driver.find_element(By.XPATH,"//input[@onclick='Billing.save()']").click()

error_msg = wait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='field-validation-error']"))).text
wait = WebDriverWait(driver,15)

print("message:", error_msg)

assert "First name" in error_msg
print("Error message displayed!")