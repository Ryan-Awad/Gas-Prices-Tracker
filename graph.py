import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ** WORK ON THIS!! **

state_province = input("Enter a state or province to graph: ").lower()
city = input("Enter a city to graph: ").lower()
company = input("Enter a company to graph: ").lower()

gas_data = pd.read_csv("gas_data.csv", sep=',')
sns.set(style="ticks")

f, ax = plt.subplots(figsize=(7,6))
ax.set_xscale("linear")

sns.swarmplot(x="Regular", y="Company", data=gas_data)
ax.xaxis.grid(True)
sns.despine(trim=True, left=True)
plt.show()