import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.makemytrip.com/holidays-india/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

packages = soup.find_all("div", class_="listingRow")

package_names = []
starting_points = []
destinations = []
dates = []
package_prices = []

for package in packages:
    package_name = package.find("span", class_="row-title").text.strip()
    starting_point = package.find("div", class_="txtBorderBottom").find_all("p")[0].text.strip()
    destination = package.find("div", class_="txtBorderBottom").find_all("p")[1].text.strip()
    date = package.find("div", class_="depart_on").text.strip()
    package_price = package.find("span", class_="from-price").text.strip()
    
    package_names.append(package_name)
    starting_points.append(starting_point)
    destinations.append(destination)
    dates.append(date)
    package_prices.append(package_price)

data = {
    "Package Name": package_names,
    "Starting Point": starting_points,
    "Destination": destinations,
    "Date": dates,
    "Price": package_prices
}
df = pd.DataFrame(data)

print(df)

df.to_csv("holiday_packages.csv", index=False)
