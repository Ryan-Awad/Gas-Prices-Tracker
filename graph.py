import matplotlib.pyplot as plt
import json
state_province = input("Enter a state or province to graph: ").lower()
city = input("Enter a city to graph: ").lower()
company = input("Enter a company to graph: ").lower()

data = json.load(open('gas_data.json', 'r'))

x = []
y = []

colors = ["red", "#59c940", "#524cff", "#ffcd42"]

for i in range(4):
    for obj in data:
        if obj['state-province'] == state_province and obj['city'] == city and obj['company'] == company:
            if "gas-price-" + str(i + 1) in obj:
                gas_company = company.capitalize()
                gas_type = obj["gas-type-" + str(i + 1)].capitalize()
                gas_price = obj["gas-price-" + str(i + 1)]
                
                if gas_price != "unavailable gas":
                    y.append(gas_price)
    
    for i2 in range(len(y)): # assign dates instead
        x.append(i2)

    plt.plot(x, y, label=gas_type, color=colors[i])
    y = []
    x = []

plt.title(gas_company + "'s Gas Prices For Each Type Of Gas")
plt.xlabel("Date")
plt.ylabel("Cost ($)")

plt.legend()
plt.show()