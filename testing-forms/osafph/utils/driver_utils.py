from selenium import webdriver

hosts = ["https://api.osafphmabalacatcity.com/login", "http://localhost:8080/login"]

def driver():
    driver = webdriver.Chrome()
    driver.get(hosts[1])
    driver.maximize_window()
    return driver

# driver = webdriver.Chrome()
# driver.get(hosts[1])
# driver.maximize_window()