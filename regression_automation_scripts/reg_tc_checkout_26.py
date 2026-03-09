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
wait = WebDriverWait(driver,15)
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
wait.until(EC.presence_of_element_located((By.ID,"checkout-step-billing")))

wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@onclick='Billing.save()'])"))).click()

wait.until(EC.presence_of_element_located((By.ID,"checkout-shipping-load")))
wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@onclick='Shipping.save()'])"))).click()

wait.until(EC.presence_of_element_located((By.ID,"opc-shipping_method")))
wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@onclick='ShippingMethod.save()'])"))).click()

wait.until(EC.presence_of_element_located((By.ID,"checkout-step-payment-method")))
wait.until(EC.element_to_be_clickable((By.ID,"paymentmethod_2"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@onclick='PaymentMethod.save()'])"))).click()


wait.until(EC.visibility_of_element_located((By.ID, "checkout-step-payment-info")))
driver.find_element(By.ID,"CardholderName").send_keys("John")
driver.find_element(By.ID,"CardNumber").send_keys("111 333 44")

expiration_date = driver.find_element(By.ID,"ExpireMonth")
select = Select(expiration_date)
select.select_by_visible_text("07")

driver.find_element(By.ID,"CardCode").send_keys("223")
driver.find_element(By.XPATH,"(//input[@onclick='PaymentInfo.save()'])").click()

error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='message-error']//li"))).text

print("Error message:", error_message)

assert "Wrong" in error_message

print("Error message displayed!")

driver.quit()


