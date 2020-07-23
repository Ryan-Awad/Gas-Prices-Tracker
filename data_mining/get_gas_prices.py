import requests
from bs4 import BeautifulSoup
import datetime
import csv

def get_gas_prices(_dir, state_province, city):
    url = "https://www.gasbuddy.com" + _dir
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    headers = {'User-Agent': user_agent}
    print("Sending request to: " + url)

    response = requests.get(url, headers=headers)
    print("[Response status code: " + str(response.status_code) + "]")

    if response.status_code == 200:
        gas_data = BeautifulSoup(response.content, 'html.parser')

        prices = gas_data.find("div", {"class", "carousel__scrollContainer___hDjMb"}).find_all("div", {"class", "GasPriceCollection__fuelTypePriceSection___3iGR-"})
        gas_types = []
        gas_types_prices = []

        for g in prices:
            gas_type = g.find("span", {"class", "colors__textGrey___2UWmi text__fluid___1X7fO text__centered___2J9MR"}).get_text()
            gas_type_price = g.find("span", {"class", "text__xl___2MXGo text__bold___1C6Z_ text__left___1iOw3 FuelTypePriceDisplay__price___3iizb"}).get_text()
            if gas_type_price == "- - -":
                gas_type_price = ""
            else:
                for c in [char for char in gas_type_price]:
                    if c != ".":
                        if not c.isdigit():
                            gas_type_price = gas_type_price.replace(c, '')
                gas_type_price = float(gas_type_price)

            gas_types.append(gas_type)
            gas_types_prices.append(gas_type_price)


        company = gas_data.find("h2", {"class", "header__header2___1p5Ig header__header___1zII0 header__evergreen___2DD39 header__snug___lRSNK StationInfoBox__header___2cjCS"}).span.get_text().lower()

        d = datetime.date.today()
        date = str(d).replace('-', '/')

        # Turning data into a one-liner to write to gas_data.csv 

        data_line = "\n" + str(date) + "," + str(company) + "," + str(state_province.replace("%20", " ").lower()) + "," + str(city.replace("%20", " ").lower())

        for i in range(len(gas_types)):
            data_line += ("," + str(gas_types_prices[i]))
        
        with open('gas_data.csv', 'a') as gas_db:
            print("Recieved Data Line: " + str(data_line))
            gas_db.write(data_line)

    else:
        print("Something went wrong with Gas price URL. Skipping this one!") # make it try again a certain amount of times