from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fill_out_form(driver, label_text, input_value, is_read_only=False, timeout=10, sleep_time=0.50):
    label_element = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")
    for_attribute_value = label_element.get_attribute("for")
    input_element = driver.find_element(By.ID, for_attribute_value)

    # Click the input element to make it visible
    
    input_element.click()
    
    if not is_read_only:
        input_element.send_keys(input_value)
    time.sleep(sleep_time)

    # Use WebDriverWait to wait for the input element to be clickable
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.ID, for_attribute_value))
    )


def fill_out_form_read_only(driver, label_text, option_text):
    fill_out_form(driver, label_text, option_text, is_read_only=True)
    dropdown_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//div[text()='{option_text}']"))
    )
    dropdown_option.click()


def fill_out_form_date(driver, label_text, date):
        # Find the input element associated with the label
    input_element = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")
    for_attribute_value = input_element.get_attribute("for")
    driver.find_element(By.ID, for_attribute_value).click()
    
    # print(date.split('-')[0], date.split('-')[1], date.split('-')[2], date.split('-')[3])

    # Wait for the calendar to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//div[text()='{date.split('-')[3]}']"))
    )


    # Choose the date
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{date.split('-')[0]}']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[text()='{date.split('-')[1]}']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{date.split('-')[2]}']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{date.split('-')[3]}']"))).click()