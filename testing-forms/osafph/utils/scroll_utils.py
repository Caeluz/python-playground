from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scroll_to_element_by_text(driver, label_text):
    try:
        # Wait for the element by its text content using XPath
        label_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[text()='{label_text}']"))
        )

        # Scroll to the element using JavaScript
        driver.execute_script("arguments[0].scrollIntoView(true);", label_element)

    except Exception as e:
        print(f"Error scrolling to element with text '{label_text}': {e}")


