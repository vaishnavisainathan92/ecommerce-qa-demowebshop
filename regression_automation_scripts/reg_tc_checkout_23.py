import time
from typing import final

from selenium import webdriver
from selenium.webdriver.common.by import By

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
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Books"))).click()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Computing and Internet"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button-13"))).click()

wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Apparel & Shoes"))).click()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Blue Jeans"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button-36"))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='cart-label']"))).click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.cart")))
wait.until(EC.element_to_be_clickable((By.ID, "termsofservice"))).click()
wait.until(EC.element_to_be_clickable((By.NAME, "checkout"))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Checkout as Guest']"))).click()

wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_FirstName")))
driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("John")
driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("Smith")
driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("j.smith@hotmail.com")
country = Select(driver.find_element(By.ID, "BillingNewAddress_CountryId"))
country.select_by_visible_text("United States")
driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Malden")
driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Florence Street")
driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("12345")
driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("1234567890")
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='Billing.save()']"))).click()

wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "ajax-loading-block-window")))

wait.until(EC.visibility_of_element_located((By.ID, "checkout-step-shipping")))

shipping_continue = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='Shipping.save()']")))

driver.execute_script("arguments[0].scrollIntoView(true);", shipping_continue)
shipping_continue.click()

wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "ajax-loading-block-window")))

wait.until(EC.visibility_of_element_located((By.ID, "opc-shipping_method")))

wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='ShippingMethod.save()']"))).click()

wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "ajax-loading-block-window")))

wait.until(EC.visibility_of_element_located((By.ID, "checkout-step-payment-method")))

wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='PaymentMethod.save()']"))).click()

wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "ajax-loading-block-window")))

wait.until(EC.visibility_of_element_located((By.ID, "checkout-step-payment-info")))

wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='PaymentInfo.save()']"))).click()

wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "ajax-loading-block-window")))

wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='ConfirmOrder.save()']"))).click()
order_details = wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[@class='details']"))).text

print("Actual message:", order_details)

assert "Order number" in order_details
print("Order placed successfully")

driver.quit()
