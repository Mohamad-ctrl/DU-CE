from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import os


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
website_link = "https://d33si906ll1hcs.cloudfront.net"

def go_to_canned_messages(driver):
    logging.info("going to the canned messages page")
    link = f"{website_link}/home/chats/agent/canned-messages/list"
    driver.get(str(link))

def go_to_helpdesk(driver):
    logging.info("going to Helpdesk section")
    link = f"{website_link}/home/chats/agent/helpdesk/list"
    driver.get(str(link))

def go_to_channels(driver):
    logging.info("going to channels section")
    link = f"{website_link}/home/engagement/communication/channels"
    driver.get(str(link))

def go_to_contacts(driver):
    logging.info("going to contact section")
    link = f"{website_link}/home/engagement/communication/contacts"
    driver.get(str(link))

def go_to_custom_filed(driver):
    logging.info("Going to custom filed section")
    link = f"{website_link}/home/engagement/communication/custom-fields"
    driver.get(str(link))

def go_to_templates(driver):
    logging.info("Going to templates section")
    link = f"{website_link}/home/engagement/communication/template-list"
    driver.get(str(link))

def go_to_survey(driver):
    logging.info("Going to the survey in the engagement")
    link = f"{website_link}/home/engagement/survey"
    driver.get(str(link))