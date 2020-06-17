import requests
from bs4 import BeautifulSoup
import json
import datetime
from data_mining.get_gas_prices import *

print("Data from: https://www.gasbuddy.com/")

while True:
    state_province = input("State or province to check: ").capitalize().strip().replace(" ", "%20")
    city = input("City to check: ").capitalize().strip().replace(" ", "%20")

    if state_province == "" or city == "":
        print("Invalid location, try again!\n\n")
        continue

    url = "https://www.gasbuddy.com/GasPrices/" + state_province + "/" + city # idiot proof
    print("-" * 100 + "\nState or province: " + state_province + "\nCity: " + city + "\nURL: " + url + "\n" + "-" * 100) # remove at end! (for dev only)

    response = requests.get(url) # sends GET request

    print("Response status code: " + str(response.status_code)) # remove what done (for dev only)

    if response.status_code != 200:
        print("Invalid location, try again!\n\n")
        continue


    gas_url_data = BeautifulSoup(response.content, 'html.parser')

    price_URLs = gas_url_data.find("tbody", {"class", "prices-table"}).find_all("tr", {"class", "accordion-toggle"})
    p_URLs = []

    for pu in price_URLs:
        p_URLs.append(pu.a.get('href'))

    for url in p_URLs: # execute web scrape function using all the urls in the p_URLs array
        get_gas_prices(url, state_province, city)


    retry = input("Would you like to build more data? (y/n): ").lower()
    if retry == "y":
        continue
    else:
        break
