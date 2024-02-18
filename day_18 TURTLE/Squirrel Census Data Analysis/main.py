import pandas

PLACEHOLDER = 'Primary Fur Color'
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240218.csv")
data_dict = {"Fur Color": [], "Count": []}

unique_color = (data[PLACEHOLDER].unique()).tolist()

for color in unique_color[1:]:
    count = (data[data[PLACEHOLDER] == color]).size
    data_dict['Fur Color'].append(color)
    data_dict['Count'].append(count)
d

data = pandas.DataFrame(data_dict)
data.to_csv('data.csv')

