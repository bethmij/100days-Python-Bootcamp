import csv
import pandas

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for datum in data:
#         if datum[1] != 'temp':
#             temperature.append(int(datum[1]))
#
#     print(temperature)

data = pandas.read_csv("weather_data.csv")
temperatures_max = data['temp'].max()
# average_temp = sum(temperatures)//len(temperatures)
print(temperatures_max)

