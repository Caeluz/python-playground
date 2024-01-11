# All Imports pip
# pip install selenium
# pip install webdriver-manager
# pip install python-dotenv

from dotenv import load_dotenv
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
    

def navigate_to_registrants():
    timeout = 10
    # After logging in, click the "Register" button
    # After logging in, navigate to the Registrants page
    # Wait for the navigation drawer button to be clickable
    navdrawer = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "v-btn__content"))
    )
    navdrawer.click()

    # Wait for the "Citizens" element to be clickable and then click it
    citizens_div = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Citizens']"))
    )
    citizens_div.click()

    # Wait for the "Registrants" element to be clickable and then click it
    registrants_div = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Registrants']"))
    )
    registrants_div.click()



def register_citizen():
    register_button = driver.find_element(By.XPATH, "//span[text()='Register']")
    register_button.click()

    # Category
    fill_out_form_read_only(driver, "Category", "A1 - FRONTLINE HEALTH WORKERS")
    fill_out_form_read_only(driver, "Identification Card", "GOVERNMENT_ISSUED_ID")
    fill_out_form_read_only(driver, "Type of Id", "SSS")
    fill_out_form(driver, "Id Number", "1234567890")

    # Click the "Proceed" button
    # proceed_button = driver.find_element(By.XPATH, "//span[text()='Proceed']").click()
    wait_for_element(driver, By.XPATH, "//span[text()='Proceed']").click()


    # Personal Details
    fill_out_form(driver, "Last Name", "Doe")
    fill_out_form(driver, "First Name", "John")
    fill_out_form(driver, "Middle Name", "Herbert")
    
    # Year Today, Year of Birth, Month of Birth, Day of Birth
    fill_out_form_date(driver, "Birthday", "2024-2013-Jan-13")

    fill_out_form_read_only(driver, "Sex", "MALE")
    fill_out_form_read_only(driver, "Civil Status", "SINGLE")
    fill_out_form(driver, "Place of Birth", "Mabalacat City")
    fill_out_form(driver, "Contact Number", "09876543210")
    fill_out_form(driver, "Blood Type", "O+")
    fill_out_form(driver, "Religion", "Buddhist")
    fill_out_form(driver, "Nationality", "American")
    fill_out_form(driver, "TIN", "12304560789")
    fill_out_form(driver, "Passport Number", "AB123455")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    wait_for_element(driver, By.XPATH, "(//span[text()='Proceed'])[2]").click()

    # Address
    fill_out_form(driver, "Unit/Building/House No./Purok/Street/Subdivision", "569-A Purok 1, Barangay San Jose")
    fill_out_form_read_only(driver, "Country", "PHILIPPINES")
    fill_out_form_read_only(driver, "Region", "REGION III (CENTRAL LUZON)")
    fill_out_form_read_only(driver, "Province", "PAMPANGA")
    fill_out_form_read_only(driver, "Municipality", "MABALACAT CITY")
    fill_out_form_read_only(driver, "Barangay", "DAU")

    # Click the "Proceed" button
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # third_proceed_button = driver.find_element(By.XPATH, "(//span[text()='Proceed'])[3]")
    # third_proceed_button.click()
    wait_for_element(driver, By.XPATH, "(//span[text()='Proceed'])[3]").click()
    time.sleep(1)


    # Emergency Contact
    input_element = driver.find_element(By.XPATH, "(//input[@type='text'])[24]")
    input_element.click()
    input_element.send_keys("Jane Doe")

    # fill_out_form_input_type(driver, "text", 25, "Jane Doe")

    # Contact Person's Number
    input_element = driver.find_element(By.XPATH, "(//input[@type='number'])[2]")
    input_element.click()
    input_element.send_keys("09876543210")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    wait_for_element(driver, By.XPATH, "(//span[text()='Proceed'])[4]").click()
    time.sleep(1)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    proceed_button = driver.find_element(By.XPATH, "//span[text()='Submit'][1]").click()
    time.sleep(1)
    # wait_for_element(driver, By.XPATH, "//span[text()='Submit'][1]")

    # alert = driver.find_element(By.XPATH, "//div[text()='Register and verification failed. Please try again']")
    alert = driver.find_element(By.CLASS_NAME, "v-alert__content")


# Load environment variables
load_dotenv()
username = os.getenv("ADMIN_USERNAME")
password = os.getenv("ADMIN_PASSWORD")



# Login
login(driver, username, password)
navigate_to_registrants()
register_citizen()

try:
    # Explicitly wait for the alert element to be present
    alert = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "v-alert__content"))
    )

    # Get the text of the alert
    alert_text = alert.text

    # Check if the desired text is present in the alert
    if "Register and verification failed. Please try again." in alert_text:
        # print("Register and verification failed. Please try again.")
        register_citizen()
    else:
        register_citizen()

except TimeoutException:
    # Handle timeout exception (element not found within the specified time)
    print("Timeout: Alert element not found within the specified time")

time.sleep(200)

driver.quit()

# <div data-v-4d473584="" role="alert" class="v-alert v-sheet theme--dark error"><div class="v-alert__wrapper"><i aria-hidden="true" class="v-icon notranslate v-alert__icon mdi mdi-alert theme--dark"></i><div class="v-alert__content">Register and verification failed. Please try again.</div><button type="button" class="v-alert__dismissible v-btn v-btn--icon v-btn--round theme--dark v-size--small" aria-label="Close"><span class="v-btn__content"><i aria-hidden="true" class="v-icon notranslate mdi mdi-close-circle theme--dark"></i></span></button></div></div>