from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import os

# Custom Imports
from utils.login_utils import login
from utils.form_utils import fill_out_form, fill_out_form_read_only, fill_out_form_date
import utils.driver_utils as driver

# driver
driver = driver.driver()

def wait_for_element(driver, by, value):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))

def navigate_to_consultations():
    timeout = 10
    
    navdrawer = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content"))
    )
    navdrawer.click()
    
    consultations_div = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Consultations']"))
    )
    consultations_div.click()
    
def create_consultation_form():
    archived_button = driver.find_element(By.XPATH, "//span[text()='Archived']")
    archived_button.click()
    
    

# Load the environment variables
load_dotenv()
doctor_username = os.getenv("DOCTOR_USERNAME")
doctor_password = os.getenv("DOCTOR_PASSWORD")
    

def main():
    login(driver, doctor_username, doctor_password)
    navigate_to_consultations()
    create_consultation_form()