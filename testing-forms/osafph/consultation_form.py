from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from faker import Faker
import time
import os

# Custom Imports
from utils.login_utils import login
from utils.form_utils import fill_out_form, fill_out_form_read_only, fill_out_form_date, fill_out_form_checkbox, fill_out_form_checkbox_same
from utils.scroll_utils import scroll_to_element_by_text
import utils.driver_utils as driver

# Import Test Functions
from tests.test_find_clickable_buttons import find_clickable_buttons

# Initialize Faker
fake = Faker()



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
    
def navigate_to_patients_consultation_view():
    timeout = 10
    # archived_button = WebDriverWait(driver, timeout).until(
    #     EC.element_to_be_clickable((By.XPATH, "//span[text()='Archived']"))
    # )
    # archived_button.click()
    
    view_button = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".v-icon.notranslate.mx-1.v-icon--link.v-icon--dense.mdi.mdi-eye.theme--light.grey--text.text--darken-1"))
    )
    view_button.click()


def create_consultation_form():
    timeout = 10
    
    add_consultation_form_button = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Add Consultation Form']"))
    )
    add_consultation_form_button.click()
    
    # Scroll to the "History of Present Illness" label
    scroll_to_element_by_text(driver, "History")
    time.sleep(1)
    fill_out_form_checkbox(driver, "Cough")
    fill_out_form_checkbox(driver, "Fever")
    
    time.sleep(1)
    # scroll_to_element_by_text(driver, "PAST MEDICAL HISTORY")
    time.sleep(1)
    fill_out_form_checkbox(driver, "Hypertension")
    
    
    # New Section
    time.sleep(1)
    scroll_to_element_by_text(driver, "PHYSICAL EXAMINATION")
    fill_out_form(driver, "BP", "120/80")
    fill_out_form(driver, "HR", "80")
    fill_out_form(driver, "RR", "20")
    fill_out_form(driver, "Temperature", "36.5")
    fill_out_form(driver, "O2 Saturation", "98")
    # weight kg
    fill_out_form(driver, "Weight (kg)", "60")
    # height m
    fill_out_form(driver, "Height (m)", "1.7")
    fill_out_form(driver, "Permanent Findings", "Normal")
    
    wait_for_element(driver, By.XPATH, "//span[text()='Proceed']").click()
    
    # Next Page, scroll to Top
    driver.execute_script("window.scrollTo(0, 0);")
    
    fill_out_form_read_only(driver, "Diagnosis", "Acute Gastroenteritis")
    
    # New Section

    scroll_to_element_by_text(driver, "Diagnostics")
    fill_out_form_checkbox(driver, "CBC with PC")
    fill_out_form_checkbox(driver, "ULTRASOUND")
    
    # Medications
    scroll_to_element_by_text(driver, "Medications")    
    fill_out_form(driver, "Specify Medications", "Paracetamol")
    
    # Referral
    scroll_to_element_by_text(driver, "Referral")
    fill_out_form(driver, "Specify Referral", "None")
    
    # Remarks
    scroll_to_element_by_text(driver, "Remarks")
    fill_out_form_date(driver, "Follow Up On", "2024-2025-Jan-13", position=3)
    time.sleep(1)
    fill_out_form_date(driver, "Fit To Work Starting", "2024-2025-Jan-13", position=4)
    fill_out_form(driver, "May Rest For", "3 days")
    
    
    
    
    
    

# Load the environment variables
load_dotenv()
doctor_username = os.getenv("DOCTOR_USERNAME")
doctor_password = os.getenv("DOCTOR_PASSWORD")

    

def main():
    login(driver, doctor_username, doctor_password)
    navigate_to_consultations()
    navigate_to_patients_consultation_view()
    
    create_consultation_form()
    # find_clickable_buttons(driver)
    
    
    
    

if __name__ == "__main__":
    main()