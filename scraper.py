import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL of the MakeMyTrip page containing holiday packages
url = "https://www.makemytrip.com/holidays-india/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all elements containing holiday package data
packages = soup.find_all("div", class_="listingRow")

# Initialize lists to store data
package_names = []
starting_points = []
destinations = []
dates = []
package_prices = []

# Loop through each package and extract relevant information
for package in packages:
    # Extract package details such as name, starting point, destination, date, price, etc.
    package_name = package.find("span", class_="row-title").text.strip()
    starting_point = package.find("div", class_="txtBorderBottom").find_all("p")[0].text.strip()
    destination = package.find("div", class_="txtBorderBottom").find_all("p")[1].text.strip()
    date = package.find("div", class_="depart_on").text.strip()
    package_price = package.find("span", class_="from-price").text.strip()
    
    # Append data to lists
    package_names.append(package_name)
    starting_points.append(starting_point)
    destinations.append(destination)
    dates.append(date)
    package_prices.append(package_price)

# Create a DataFrame using the extracted data
data = {
    "Package Name": package_names,
    "Starting Point": starting_points,
    "Destination": destinations,
    "Date": dates,
    "Price": package_prices
}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
