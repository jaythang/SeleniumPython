from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (in this example, we'll use Chrome)
driver = webdriver.Chrome()

# 4.1. Navigate to "https://www.example.com/dashboard"
driver.get("https://www.example.com/dashboard")

try:
    # 4.1. Wait until an element with the ID "data-loaded" is visible (max 10 seconds)
    wait = WebDriverWait(driver, 10)
    data_loaded_element = wait.until(EC.visibility_of_element_located((By.ID, "data-loaded")))

    # 4.1. Click a button with the ID "refreshData"
    refresh_button = driver.find_element(By.ID, "refreshData")
    refresh_button.click()

    # You can add additional interactions or validations here after clicking the button.

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # Close the browser when done
    driver.quit()
