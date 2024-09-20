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
import channels
import contacts
import custom_filed


def save_channels_results(results, writer):
    df = pd.DataFrame(results)
    df.to_excel(writer, sheet_name='Channels Results', index=False)

def save_other_tests(results, writer):
    df = pd.DataFrame(results)
    df.to_excel(writer, sheet_name='Other tests', index=False)



def run_tests(driver, adminEmail, adminPassword, newWhatsTemp, newWhatsListOrPromo, newWhatsNumber, newContactListName, newContactCsvFile, createNewFiled_FiledName, createNewFiled_Example, newWhatsSendTime = None, newWhatsNameInList = None, newWhatsStartDate = None, newWhatsStartTime = None, newWhatsEndDate = None, newWhatsEndTime = None, newContactDetails = None):
    other_tests_results = []
    channels_results = []
    auth.loginAsAdmin(driver, adminEmail, adminPassword)
    time.sleep(20)

    # Going to the channels
    navigate.go_to_channels(driver)
    time.sleep(15)

    # Testing the new whatsapp message
    new_whatsapp_tests_res = channels.send_new_Whatsapp(driver, newWhatsTemp, newWhatsListOrPromo, newWhatsNumber, newWhatsSendTime, newWhatsNameInList, newWhatsStartDate, newWhatsStartTime, newWhatsEndDate, newWhatsEndTime)
    channels_results.append(new_whatsapp_tests_res)
    time.sleep(10)

    # Going to contacts
    navigate.go_to_contacts(driver)
    time.sleep(10)

    # Testing creating new contact
    contacts.create_new_contact_list(driver, newContactListName, newContactCsvFile, newContactDetails)
    time.sleep(15)
    create_new_contact_res = contacts.search_for_contact_list(newContactListName)
    other_tests_results.append(create_new_contact_res)

    # Going to the cutom filed section
    time.sleep(5)
    navigate.go_to_custom_filed(driver)
    time.sleep(15)

    # Testing creating new custom filed
    custom_filed.create_new_filed(driver, createNewFiled_FiledName, createNewFiled_Example)
    time.sleep(10)
    custom_filed_test_res = custom_filed.check_filed(driver, createNewFiled_FiledName)
    other_tests_results.append(custom_filed_test_res)

    # Ending the test
    logging.info("tests are finished")
    currentDate = datetime.now()
    # Format the date and time
    formatted_date_time = currentDate.strftime("%d-%m_%I.%M%p").lower()
    
    # Create the file name
    file_name = f'engagement_tests_results_{formatted_date_time}.xlsx'
    
    # Get the directory of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the full file path
    result_file = os.path.join(script_directory, file_name)
    
    with pd.ExcelWriter(result_file, mode='w', engine='openpyxl') as writer:
        save_channels_results(channels_results, writer)
        save_other_tests(other_tests_results, writer)

    return result_file
