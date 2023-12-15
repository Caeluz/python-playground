import requests
from bs4 import BeautifulSoup

# Specify the URL of the web page you want to crawl
url = "https://api.osafphmabalacatcity.com/citizens/register"

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all input forms on the page
    input_forms = soup.find_all('form')

    # Print information about each form
    for form in input_forms:
        print("Form found:")
        print("Action:", form.get('action'))
        print("Method:", form.get('method'))
        print("---")

else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
