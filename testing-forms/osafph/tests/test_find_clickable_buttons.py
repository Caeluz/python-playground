from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def find_clickable_buttons(driver):
    timeout = 10
    time.sleep(5)
    
    # buttons = WebDriverWait(driver, timeout).until(
    # EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".v-icon.notranslate.mx-1.v-icon--link.v-icon--dense.mdi.mdi-eye.theme--light.grey--text.text--darken-1"))
    # )
    
    buttons = WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "v-input--selection-controls__ripple"))
    )

    # Print the number of clickable buttons found
    print(f"Number of clickable buttons: {len(buttons)}")

    # Iterate through each button and print its text
    for button in buttons:
        print("Button Text:", button.text)
