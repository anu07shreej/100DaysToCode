# Working with the csv
import pandas as pd
import csv
# temp = []
# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
#print(temp)

states = pd.read_csv("weather_data.csv")
print(states["temp"])
