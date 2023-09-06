"""
Technical Test: Senior Automated Test Engineer - Selenium & Python

Complete the tasks below. Ensure you consider best practices, readability, and efficient code.

Your code will be evaluated based on correctness, usage of Selenium best practices, code cleanliness, and handling edge cases.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. WebDriver Initialization

# 1.1. Initialize a Firefox WebDriver instance with desired capabilities to run in headless mode.

# TODO: Initialize the Firefox WebDriver instance here.

# 2. Navigation and Element Interaction

# 2.1. Navigate to "https://www.example.com" and find an element with the ID "sampleElement", then click it.

# TODO: Write the navigation and interaction code here.


# 3. Assertions and Validations

# 3.1. Navigate to "https://www.example.com/profile" and ensure the title is "User Profile".

# TODO: Write the navigation and assertion code here.

# 3.2. On the same page, ensure a paragraph with the class "user-description" contains the text "Selenium Tester".

# TODO: Write the element validation code here.


# 4. Waiting Mechanisms

# 4.1. Navigate to "https://www.example.com/dashboard". Wait until an element with the ID "data-loaded" is visible, then click a button with the ID "refreshData".

# TODO: Write the navigation, waiting mechanism, and interaction code here.


# 5. Frames and Windows Handling

# 5.1. Navigate to "https://www.example.com/settings". Switch to a frame named "settingsFrame" and click a button with the ID "saveSettings".

# TODO: Write the navigation, frame switching, and interaction code here.

# 5.2. From the main window, click a button that opens a new browser window/tab. Switch to the new window/tab and assert its title is "New Window".

# TODO: Write the interaction, window switching, and assertion code here.


# 6. Practical Application

# 6.1. Write a function that accepts a WebDriver instance and a username, navigates to "https://www.example.com/login", fills in the username in an input with the ID "username", fills a default password "password123" in an input with the ID "password", and clicks a button with the ID "submit".

def login(driver, username: str):
    # TODO: Implement the login function here.

