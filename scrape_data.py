import requests
from bs4 import BeautifulSoup

url = "https://www.lionsclub-mettmann-wuelfrath.de/aktivitaeten/adventskalender_gewinnerlose.html"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table with the desired information
    table = soup.find('table', {'class': 'contenttable'})

    # Check if the table is found
    if table:
        # Extract data from the table
        for row in table.find_all('tr')[1:]: # Skip the header row
            columns = row.find_all('td')
            
            # Assuming the first column contains numbers and the second contains text
            number = columns[0].text.strip()
            text = columns[1].text.strip()

            # Print or store the extracted data as needed
            print(f"Number: {number}, Text: {text}")
    else:
        print("Table not found on the page.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
