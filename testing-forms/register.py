from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://api.osafphmabalacatcity.com/login")

driver.find_element("id", "input-18").send_keys("admin")
driver.find_element("id", "input-21").send_keys("admin")

# driver.find_element("id", "input-21").send_keys(Keys.ENTER)

login_button = driver.find_element(By.CLASS_NAME, "v-btn__content")
login_button.click()

time.sleep(2)

navdrawer = driver.find_element(By.CLASS_NAME, "v-btn__content")
navdrawer.click()

time.sleep(3)

citizens_div = driver.find_element(By.XPATH, "//div[text()='Citizens']")
citizens_div.click()
# citizens_button = driver.find_element(By.CLASS_NAME, "v-list-item__title")
# citizens_button.click()
time.sleep(1)

registrants_div = driver.find_element(By.XPATH, "//div[text()='Registrants']")
registrants_div.click()

register_button = driver.find_element(By.XPATH, "//span[text()='Register']")
register_button.click()

#
# Fill out the form fields
# category_input = driver.find_element(By.CSS_SELECTOR, "v-select[label='Category']") 
category_input = driver.find_element(By.CLASS_NAME, "v-select__slot") 
category_input.click()  # This may open a dropdown, handle accordingly
time.sleep(1)

category_option = driver.find_element(By.XPATH, "//div[text()='ALL ADULT POPULATION ELIGIBLE TO BE CATEGORIZES AS PRIORITY GROUP A1']")
category_option.click()
time.sleep(2)

# identification_card_input = driver.find_element(By.XPATH, "//input[label='Identification Card']")

label_text = "Identification Card"
identification_card_input = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")

# Get the 'for' attribute value from the label
for_attribute_value = identification_card_input.get_attribute("for")
id_input_element = driver.find_element(By.ID, for_attribute_value)

id_input_element.click()

time.sleep(1)

id_option = driver.find_element(By.XPATH, "//div[text()='GOVERNMENT_ISSUED_ID']")
id_option.click()

label_text = "Type of Id"
type_of_id_input = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")

for_attribute_value = type_of_id_input.get_attribute("for")
type_of_id_input_element = driver.find_element(By.ID, for_attribute_value)

type_of_id_input_element.click()

type_of_id_option = driver.find_element(By.XPATH, "//div[text()='SSS']")
type_of_id_option.click()

# type_of_id_input = driver.find_element(By.ID, "input-230")
# type_of_id_input.send_keys("SSS")
# time.sleep(1)

label_text = "Id Number"
id_number_input = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")

for_attribute_value = id_number_input.get_attribute("for")
id_number_input_element = driver.find_element(By.ID, for_attribute_value)

id_number_input_element.send_keys("1234567890")



label_text = "HUB Registrant Number"
id_number_input = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")

for_attribute_value = id_number_input.get_attribute("for")
id_number_input_element = driver.find_element(By.ID, for_attribute_value)

id_number_input_element.send_keys("1234567890")

# Click the "Proceed" button
proceed_button = driver.find_element(By.XPATH, "//span[text()='Proceed']")
proceed_button.click()

label_text = "Last Name"
id_number_input = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")

for_attribute_value = id_number_input.get_attribute("for")
id_number_input_element = driver.find_element(By.ID, for_attribute_value)

id_number_input_element.send_keys("Doe")

label_text = "First Name"
id_number_input = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")

for_attribute_value = id_number_input.get_attribute("for")
id_number_input_element = driver.find_element(By.ID, for_attribute_value)

id_number_input_element.send_keys("John")

label_text = "Middle Name"
id_number_input = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")

for_attribute_value = id_number_input.get_attribute("for")
id_number_input_element = driver.find_element(By.ID, for_attribute_value)

id_number_input_element.send_keys("Herbert")

label_text = "Birthday"
birthday_input = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")

for_attribute_value = birthday_input.get_attribute("for")
birthday_input_element = driver.find_element(By.ID, for_attribute_value)

birthday_input_element.click()
time.sleep(1)

# calendar_day = driver.find_element(By.XPATH, "//div[text()='13']")
# id_number_input_element.send_keys("01/01/1990")

calendar_year = driver.find_element(By.XPATH, "//div[text()='2023']")
calendar_year.click()
time.sleep(1)

calendar_year_2 = driver.find_element(By.XPATH, "//li[text()='2013']")
calendar_year_2.click()
time.sleep(0.5)

calendar_month = driver.find_element(By.XPATH, "//div[text()='Jan']")
calendar_month.click()
time.sleep(0.5)


calendar_day = driver.find_element(By.XPATH, "//div[text()='13']")
calendar_day.click()
time.sleep(0.5)


label_text = "Sex"
sex_input = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")

for_attribute_value = sex_input.get_attribute("for")
sex_input_element = driver.find_element(By.ID, for_attribute_value)

# sex_input_element.click()
time.sleep(1)
sex_input_element.send_keys("MALE")


# Civil Status
label_text = "Civil Status"
civil_input = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")

for_attribute_value = civil_input.get_attribute("for")
civil_input_element = driver.find_element(By.ID, for_attribute_value)

# sex_input_element.click() 
time.sleep(1)
civil_input_element.send_keys("SINGLE")

# Place of Birth
label_text = "Place of Birth"
POB_input = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")

for_attribute_value = POB_input.get_attribute("for")
POB_input_element = driver.find_element(By.ID, for_attribute_value)

# POB_input_element.click()
time.sleep(1)
POB_input_element.send_keys("Baguio City")

# Contact Number
label_text = "Contact Number"
contact_number_input = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")

for_attribute_value = contact_number_input.get_attribute("for")
contact_number_input_element = driver.find_element(By.ID, for_attribute_value)

# contact_number_input_element.click()
time.sleep(1)
contact_number_input_element.send_keys("01234567890")

# Function to fill out form fields
def fill_out_form(driver, label_text, input_value):
    label_element = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")
    for_attribute_value = label_element.get_attribute("for")
    input_element = driver.find_element(By.ID, for_attribute_value)

    input_element.click()
    time.sleep(1)
    input_element.send_keys(input_value)




# Example usage for different form fields
fill_out_form(driver, "Blood Type", "O+")
fill_out_form(driver, "Religion", "Buddhist")
fill_out_form(driver, "Nationality", "American")
fill_out_form(driver, "TIN", "123-456-789")
fill_out_form(driver, "Passport Number", "AB123456")

# Function to click the button containing a span
# def click_button_with_span(driver, button_text):


# # Example usage for the "Proceed" button
# click_button_with_span(driver, "Proceed")

button_text = "Proceed"
button_element = driver.find_element(By.XPATH, f"//button[contains(span, '{button_text}')]")
button_element.click()

time.sleep(3)

driver.quit()

