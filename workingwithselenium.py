from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from _datetime import datetime

driver = webdriver.Chrome()
driver.get("https://www.payableapps.com/")
print("Opened tab 1: Payable -", driver.title)
time.sleep(5)

driver.execute_script("window.open('https://www.payableapps.com/')")
time.sleep(5)

tabs = driver.window_handles
driver.switch_to.window(tabs[1])
print("Switched to tab 2: ", driver.title)
driver.close()
print("Tab 2 closed: Payable WebApp")

tabs_changed = driver.window_handles

driver.switch_to.window(tabs[0])

blog_button = driver.find_element(By.XPATH, '//*[@id="primary-menu"]/ul/li[4]/a')
blog_button.click()
time.sleep(5)
print("Clicked on blog button")

home_button = driver.find_element(By.XPATH, '//*[@id="menu-item-49"]/a')
home_button.click()
time.sleep(5)
print("Clicked back on home button")
time.sleep(5)

print("Extracting text from the page...")
time.sleep(2)

element = driver.find_element(By.XPATH, '/html/body/div[3]/section[1]/div/div/div/div[1]/div/div[1]/h4')
print("Extracted text:", element.text)
print("Text extracted successfully")

target_time = "16:45"

while True:
    current_time = datetime.now().strftime("%H:%M")
    if current_time == target_time:
        print("Target time reached: Closing Chrome...")
        driver.close()
        print("Chrome closed successfully")
        break
    time.sleep(5)
