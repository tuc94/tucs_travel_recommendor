from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Selenium driver (e.g., Chrome)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://destinationinsights.withgoogle.com/intl/en_ALL/")

# Wait for 10 seconds
time.sleep(30)

element = driver.find_element(By.XPATH, "//*[@aria-controls='outbound-destination-interest']")
element.click()

# Click the element with the specified XPath
element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div/a')
element.click()

time.sleep(30)


# Proceed with your scraping or further actions
# ...

# Close the browser
driver.quit()
