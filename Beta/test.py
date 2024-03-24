from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Navigate to the specified URL
driver.get("https://app.drivecentric.com/#/pipeline/sales")

# The try block is used to catch and handle exceptions
try:
    # Wait up to 10 seconds for the username field to become available
    # 'By.ID' is used to find the element by its ID
    # 'signInFormUsername' is the ID of the username field
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'signInFormUsername')))
    # Input the username into the username field
    username_field.send_keys('rhernandez@mbofcaldwell.com')

    # Wait up to 10 seconds for the password field to become available
    # 'signInFormPassword' is the ID of the password field
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'signInFormPassword')))
    # Input the password into the password field
    password_field.send_keys('wELCOME7')

    # Wait up to 10 seconds for the login button to become available
    # 'By.NAME' is used to find the element by its name
    # 'Login' is the name of the login button
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'Login')))
    # Click the login button
    login_button.click()
# If an exception occurs in the try block, it's caught and handled here
except Exception as e:
    # Print the exception
    print(f"An error occurred: {e}")
# The finally block is executed regardless of whether an exception occurred
login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'submitButton-customizable')))
login_button.click()

# After clicking the login button
time.sleep(10)  # Wait for the authenticator code input to appear

# Pause the script and wait for user input
auth_code = input("Please enter the authenticator code: ")

# Find the authenticator code input (replace 'authInputID' with its actual ID)
auth_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'authInputID')))

# Input the authenticator code
auth_input.send_keys(auth_code)

# Find and click the submit button (replace 'submitButtonID' with its actual ID)
submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'submitButtonID')))
submit_button.click()