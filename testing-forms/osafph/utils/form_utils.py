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


def fill_out_form_date(driver, label_text, date, position=2):
        # Find the input element associated with the label
    input_element = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")
    for_attribute_value = input_element.get_attribute("for")
    driver.find_element(By.ID, for_attribute_value).click()
    
    # //*[@id="app"]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[6]/button/div
    # //*[@id="app"]/div[3]/div/div[2]/div/div[2]/table/tbody/tr[3]/td[3]/button/div
    

    
    
    year_now, chosen_year, month, day = date.split('-')

    # Choose the date
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{year_now}']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[text()='{chosen_year}']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{month}']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{day}']"))).click()
    
    # wait.until(EC.element_to_be_clickable((By.XPATH, f"//html/body/div/div[{position}]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[6]/button/div"))).click()
    # wait.until(EC.element_to_be_clickable((By.XPATH, f"//html/body/div/div[{position}]/div[text()='{day}']"))).click()
    # xpath = "//div[3]/div/div[text()='{}']".format(day)
    # print(xpath)


def fill_out_form_checkbox(driver, label_text):
    # Find the input element associated with the label
    input_element = driver.find_element(By.XPATH, f"//label[text()='{label_text}']")
    for_attribute_value = input_element.get_attribute("for")
    print(for_attribute_value)
    
    # Find the checkbox by ID and click on it
    # checkbox = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.ID, for_attribute_value))
    # )
    
    checkbox = driver.find_element(By.ID, for_attribute_value)
    
    # Click on the next sibling div element
    div_element = checkbox.find_element(By.XPATH, 'following-sibling::div')
    div_element.click()
    
def fill_out_form_checkbox_same(driver, label_text):
    # Find the input element associated with the label
    input_element = driver.find_element(By.XPATH, f"//label[text()='{label_text}'][-1]")
    for_attribute_value = input_element.get_attribute("for")
    print(for_attribute_value)
    

    
    checkbox = driver.find_element(By.ID, for_attribute_value)
    
    # Click on the next sibling div element
    div_element = checkbox.find_element(By.XPATH, 'following-sibling::div')
    div_element.click()
