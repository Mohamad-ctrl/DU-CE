from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import openpyxl
import time
import pandas as pd
import logging
import os
import auth
import utils
import navigate
import engagement


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')# Function to compare responses

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window() 

# The website URL
chat_url = "https://d33si906ll1hcs.cloudfront.net"

# Open the website
driver.get(chat_url)


# Wait for the page to load and the chat button to be clickable
chat_button = WebDriverWait(driver, 30).until(  
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".chatbot-toggle-icon img.ng-star-inserted"))
)

# Click the chat button
chat_button.click()

# Add a short wait to ensure chat box is fully opened
time.sleep(5)

# Engagement tester

# Admin login
adminEmail = "maria+uat@thinglogix.com"
adminPassword = "MZ@12345"


# Arguments for new whatsapp message test (Note that this test costs money therfore if you wish to not do it just leave all its value empty)
# if you want to run the test just make sure to fill all arguments that has the '*' next to them
newWhatsTemp = None # *
newWhatsListOrPromo = None # *
newWhatsNumber = None # *
newWhatsSendTime = None
newWhatsNameInList = None
newWhatsStartDate = None
newWhatsStartTime = None
newWhatsEndDate = None
newWhatsEndTime = None

# Arguments for new contact test
newContactListName = ""
newContactCsvFile = ""
# optional argument
newContactDetails = None


# Arguments for new custom filed
createNewFiled_FiledName = ""
createNewFiled_Example = ""


engagement.run_tests(driver, adminEmail, adminPassword, newWhatsTemp, newWhatsListOrPromo, newWhatsNumber, newContactListName, newContactCsvFile,
                      createNewFiled_FiledName, createNewFiled_Example, newWhatsSendTime = None, newWhatsNameInList = None, newWhatsStartDate = None,
                        newWhatsStartTime = None, newWhatsEndDate = None, newWhatsEndTime = None, newContactDetails = None)

    
time.sleep(3000)
driver.quit()
