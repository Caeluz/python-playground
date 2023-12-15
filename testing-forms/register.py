from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

driver = webdriver.Chrome()
driver.get("https://api.osafphmabalacatcity.com/login")

def wait_for_element(driver, by, value):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))

def fill_out_form(driver, label_text, input_value, is_read_only=False, time_sleep=0.25):
    label_element = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")
    for_attribute_value = label_element.get_attribute("for")
    input_element = driver.find_element(By.ID, for_attribute_value)

    input_element.click()
    if not is_read_only:
        input_element.send_keys(input_value)
    time.sleep(time_sleep)

def fill_out_form_read_only(driver, label_text, option_text):
    fill_out_form(driver, label_text, option_text, is_read_only=True)
    dropdown_option = driver.find_element(By.XPATH, f"//div[text()='{option_text}']")
    dropdown_option.click()

def login():


    fill_out_form(driver, "Username", users[0])
    fill_out_form(driver, "Password", users[0])


    # Click the "Login" button
    login_button = driver.find_element(By.CLASS_NAME, "v-btn__content")
    wait_for_element(driver, By.CLASS_NAME, "v-btn__content").click()


    # After logging in, click the "Register" button
    # After logging in, navigate to the Registrants page
    time.sleep(1)
    navdrawer = driver.find_element(By.CLASS_NAME, "v-btn__content")
    navdrawer.click()
    time.sleep(1)
    citizens_div = driver.find_element(By.XPATH, "//div[text()='Citizens']")
    citizens_div.click()
    time.sleep(1)
    registrants_div = driver.find_element(By.XPATH, "//div[text()='Registrants']")
    registrants_div.click()


    
# Login
# driver.find_element("id", "input-18").send_keys("admin")
# driver.find_element("id", "input-21").send_keys("admin")

def register():
    register_button = driver.find_element(By.XPATH, "//span[text()='Register']")
    register_button.click()

    # Category
    fill_out_form_read_only(driver, "Category", "ALL ADULT POPULATION ELIGIBLE TO BE CATEGORIZES AS PRIORITY GROUP A1")
    fill_out_form_read_only(driver, "Identification Card", "GOVERNMENT_ISSUED_ID")
    fill_out_form_read_only(driver, "Type of Id", "SSS")
    fill_out_form(driver, "Id Number", "1234567890")
    fill_out_form(driver, "HUB Registrant Number", "1234567890")

    # Click the "Proceed" button
    # proceed_button = driver.find_element(By.XPATH, "//span[text()='Proceed']").click()
    wait_for_element(driver, By.XPATH, "//span[text()='Proceed']").click()


    # Personal Details
    fill_out_form(driver, "Last Name", "Doe")
    fill_out_form(driver, "First Name", "John")
    fill_out_form(driver, "Middle Name", "Herbert")

    label_text = "Birthday"
    # Find the input element associated with the label
    birthday_input = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")
    for_attribute_value = birthday_input.get_attribute("for")
    birthday_input_element = driver.find_element(By.ID, for_attribute_value).click()

    # Wait for the calendar to appear
    calendar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='13']"))
    )

    # Choose the date
    time.sleep(0.25)
    calendar_year = driver.find_element(By.XPATH, "//div[text()='2023']").click()
    time.sleep(0.25)
    calendar_year_2 = driver.find_element(By.XPATH, "//li[text()='2013']").click()
    time.sleep(0.25)
    calendar_month = driver.find_element(By.XPATH, "//div[text()='Jan']").click()
    time.sleep(0.25)
    calendar_day = driver.find_element(By.XPATH, "//div[text()='13']").click()
    time.sleep(0.25)

    fill_out_form_read_only(driver, "Sex", "MALE")
    fill_out_form_read_only(driver, "Civil Status", "SINGLE")
    fill_out_form(driver, "Place of Birth", "Mabalacat City")
    fill_out_form(driver, "Contact Number", "09876543210")

    # Example usage for different form fields
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
    input_element = driver.find_element(By.XPATH, "(//input[@type='text'])[25]")
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

login()
register()

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
        register()
    else:
        register()

except TimeoutException:
    # Handle timeout exception (element not found within the specified time)
    print("Timeout: Alert element not found within the specified time")

time.sleep(200)

driver.quit()

# <div data-v-4d473584="" role="alert" class="v-alert v-sheet theme--dark error"><div class="v-alert__wrapper"><i aria-hidden="true" class="v-icon notranslate v-alert__icon mdi mdi-alert theme--dark"></i><div class="v-alert__content">Register and verification failed. Please try again.</div><button type="button" class="v-alert__dismissible v-btn v-btn--icon v-btn--round theme--dark v-size--small" aria-label="Close"><span class="v-btn__content"><i aria-hidden="true" class="v-icon notranslate mdi mdi-close-circle theme--dark"></i></span></button></div></div>