from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")

# Specify the path to your user data directory
options = Options()
options.add_argument("--user-data-dir=C:\Users\pured\AppData\Local\Google\Chrome\User Data")

# Initialize the Chrome browser with the specified options
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the specified URL
driver.get("https://app.drivecentric.com/#/pipeline/sales")

# Pause the script and wait for you to manually log in
input("Press Enter after you manually log in...")

# Your automation code starts here...
