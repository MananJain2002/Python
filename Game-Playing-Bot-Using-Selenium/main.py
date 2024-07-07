import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException


# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.maximize_window()


eng = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "langSelect-EN"))
)
eng.click()

cookie = driver.find_element(By.CSS_SELECTOR, value="#bigCookie")

# Record the start time
start_time = time.time()

# Initialize the last time the items were clicked
last_items_click_time = 0

while time.time() - start_time < 300:  # 300 seconds = 5 minutes
    cookie.click()

    # Check if 7 seconds have passed since the last items click
    if time.time() - last_items_click_time >= 7:
        
        try:
            upgrades = driver.find_elements(By.CSS_SELECTOR, value=".crate.upgrade.enabled")
            for up in upgrades[::-1]:
                up.click()
        except StaleElementReferenceException:
            print("Encountered a stale element, retrying...")
            continue
        
        items = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
        for item in items[::-1]:
            item.click()
        # Update the last items click time
        last_items_click_time = time.time()
