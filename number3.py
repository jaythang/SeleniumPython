from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

# Initialize the WebDriver (in this example, we'll use Chrome)
driver = webdriver.Firefox()

# 3.1. Navigate to "https://www.example.com/profile"
driver.get("https://www.example.com/profile")

try:
    # 3.1. Ensure the title is "User Profile"
    assert "User Profile" in driver.title, f"Expected title 'User Profile', but got '{driver.title}'."

    # 3.2. Ensure a paragraph with the class "user-description" contains the text "Selenium Tester"
    user_description = driver.find_element(By.CLASS_NAME, "user-description")
    assert "Selenium Tester" in user_description.text, "User description does not contain 'Selenium Tester'."

    print("Assertions and validations passed!")

except AssertionError as e:
    print(f"Assertion error: {e}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser after a brief pause (for demonstration purposes)
    time.sleep(3)
    driver.quit()
