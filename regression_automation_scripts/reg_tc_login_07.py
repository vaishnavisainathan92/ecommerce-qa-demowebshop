from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)


chrome_options.add_argument(r"--user-data-dir=C:\selenium_profile")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")

wait = WebDriverWait(driver, 10)

try:
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log in"))).click()

    driver.find_element(By.ID, "Email").send_keys("johnAdams1@gmail.com")
    driver.find_element(By.ID, "Password").send_keys("abc@123")
    driver.find_element(By.ID, "RememberMe").click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Log in']"))).click()

except NoSuchElementException:
    print("User already logged in")

logout_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
assert logout_link.is_displayed()

print(" User is remembered and logged in")