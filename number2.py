from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EZ

# Initialize the WebDriver (in this example, we'll use Chrome)
driver = webdriver.Firefox()

# 2.1. Navigate to "https://www.example.com"
driver.get("https://www.example.com")

try:
    # Wait for the element with the ID "sampleElement" to be clickable (max 10 seconds)
    element = WebDriverWait(driver, 10).until(
        EZ.element_to_be_clickable((By.ID, "sampleElement"))
    )

    # Click the element with the ID "sampleElement"
    element.click()

    # Optionally, you can perform additional actions with the element here.

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser when done
    driver.quit()
