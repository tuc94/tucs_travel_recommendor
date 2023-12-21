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


# Locate the <ul> element inside the div with id="GeographicDemandCountry"
ul_element = driver.find_element(By.CSS_SELECTOR, '#GeographicDemandCountry ul')

# Find all <li> elements within the <ul>
li_elements = ul_element.find_elements(By.TAG_NAME, 'li')

# Initialize a list to hold the scraped data
scraped_data = []

# Loop through each <li> element
for li in li_elements:
    # Extract text from spans
    name_span = li.find_element(By.CLASS_NAME, 'geographic-demand__name')
    total_span = li.find_element(By.CLASS_NAME, 'geographic-demand__total')

    name = name_span.text
    total = total_span.text

    # Store the data in a dictionary and add it to the list
    scraped_data.append({'name': name, 'total': total})

# Close the browser
driver.quit()

# Print or process the scraped data
for data in scraped_data:
    print(data)