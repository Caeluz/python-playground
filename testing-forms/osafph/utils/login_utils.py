from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.form_utils import fill_out_form

def login(driver, username, password, timeout=10):
    fill_out_form(driver, "Username", username)
    fill_out_form(driver, "Password", password)

    login_button = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Login']"))
    )
    login_button.click()