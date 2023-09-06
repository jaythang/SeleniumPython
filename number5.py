from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (in this example, we'll use Chrome)
driver = webdriver.Chrome()

# 5.1. Navigate to "https://www.example.com/settings"
driver.get("https://www.example.com/settings")

try:
    # 5.1. Switch to a frame named "settingsFrame"
    driver.switch_to.frame("settingsFrame")

    # 5.1. Click a button with the ID "saveSettings"
    save_settings_button = driver.find_element(By.ID, "saveSettings")
    save_settings_button.click()

    # You can add additional interactions or validations here after clicking the button.

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Return to the default content
    driver.switch_to.default_content()

    # Close the browser when done
    driver.quit()
