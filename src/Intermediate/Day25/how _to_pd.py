import pandas

data = pandas.read_csv("weather-data.csv")
print(data)

temp_list = data.temp.to_list
print(temp_list)

print(data.temp.mean())
print(data.temp.max())
#
# # Get Data in Columms
#
print(data.condition)

print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

# how to create a dataframe from scratch

data_dict = {
    "Students": ["Amy", "James", "Angela", "Rachamv"],
    "Scores": [74, 90, 78, 100]
}
data_style = pandas.DataFrame(data_dict)
data_style.to_csv("new_file.csv")
print(data_style)