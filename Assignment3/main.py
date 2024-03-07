from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Go to the Shein website
driver.get('https://www.shein.com/')

# Wait for demonstration purposes
time.sleep(8)

# Find sign in/registration button
registration_button = driver.find_element("xpath","/html/body/div[1]/header/div[2]/div[1]/div/div[2]/div[3]/div[1]/a")
registration_button.click()

# Wait for demonstration purposes
time.sleep(5)

# Find the email input field and enter the email address
email_input = driver.find_element("xpath","/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/input")
email_input.send_keys("Swati09december1997@gmail.com")

# Wait for demonstration purposes
time.sleep(7)

# Find the countinue button and click it
countinue_button = driver.find_element("xpath","/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div[3]/div/button")
countinue_button.click()

# Wait for the page to load
time.sleep(5)

# Find the password input field and enter the password
password_input = driver.find_element("xpath","/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div[4]/div[2]/div/div/input")
password_input.send_keys("Swativish09")

# Wait for demonstration purposes
time.sleep(3)

# Find the signin button and click it
Signin_button = driver.find_element("xpath","/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div[4]/div[8]/div[1]/button")
Signin_button.click()

# Wait for the page to load
time.sleep(5)

# Close the browser
driver.quit()
