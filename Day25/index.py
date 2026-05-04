# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data);

######################################################

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)  
#     tempertures = []  
#     for row in data:
#         if row[1] != "temp":
#             tempertures.append(row[1])

# print(tempertures)    

import panda as pd
data = pd.read_csv("weather_data.csv")



        