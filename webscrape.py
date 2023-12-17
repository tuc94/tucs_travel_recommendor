import requests
from bs4 import BeautifulSoup

url = 'https://destinationinsights.withgoogle.com/intl/en_ALL/'

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate and extract the data you need using BeautifulSoup
    # For example, find all the links on the page
    links = soup.find_all('a', href=True)

    # Process and print the extracted data
    for link in links:
        print(link['href'])
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
