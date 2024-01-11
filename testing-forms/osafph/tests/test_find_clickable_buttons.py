from selenium import webdriver
from selenium.webdriver.common.by import By

# Assuming you have a WebDriver instance already
driver = webdriver.Chrome()
driver.get("")

# Find all clickable buttons using XPath
buttons = driver.find_elements(By.XPATH, "//button[contains(@onclick, 'click')]")

# Print the number of clickable buttons found
print(f"Number of clickable buttons: {len(buttons)}")

# Iterate through each button and print its text
for button in buttons:
    print("Button Text:", button.text)

# Close the browser when done
driver.quit()