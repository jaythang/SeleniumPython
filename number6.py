from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login(driver, username: str):
    # Navigate to the login page
    driver.get("https://www.example.com/login")

    # Find the username input element and fill it with the provided username
    username_input = driver.find_element(By.ID, "username")
    username_input.clear()  # Clear any existing text
    username_input.send_keys(username)

    # Find the password input element and fill it with a default password
    password_input = driver.find_element(By.ID, "password")
    password_input.clear()  # Clear any existing text
    password_input.send_keys("password123")

    # Find and click the submit button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

# Example usage:
from selenium import webdriver

# Initialize a WebDriver instance (e.g., ChromeDriver)
driver = webdriver.Chrome()

# Call the login function with a username
login(driver, "your_username")

# Close the WebDriver when done
driver.quit()
