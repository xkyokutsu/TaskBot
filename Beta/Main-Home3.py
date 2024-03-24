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

def check_notifications(driver):
    # Find the notification element
    notification_element = driver.find_element_by_css_selector('span.driveStoreBarCount')

    # Check if there are any notifications
    if notification_element.text.strip() != '':
        # If there are notifications, click the element
        notification_element.click()

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

except Exception as e:
    # Print the exception
    print(f"An error occurred: {e}")

# Pause the script and wait for user input
input("Please finish logging in, proceed to the mining tab and open up the first client to begin the loop ...")

# Wait for the page to load
time.sleep(2)

# # # # # # # # # #
# begin loop
# # # # # # # # # #


