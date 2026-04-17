

dictionary = {
    "red" :"color of rose",
    "blue" : "color of berries",
    "orange": "color of sacrifice",
    1:"inital num"
}

print(dictionary["red"])
print(dictionary[1])

dictionary["pink"] = "color of beauty";
print(dictionary)

# dictionary = {};
print(dictionary)

for things in dictionary:
    print(things)

for things in dictionary:
    print(dictionary[things])    
# print(dictionary.get())
# print(dictionary.values())


travel_log  = {
    "France": ["Paris","Little","Dijon"],
    "Germany": ["Shutgart","Berlin"],
}
print(travel_log)
print(travel_log["France"][2])

covid_data = {
    "france" : {
        "death" : "This is total death",
        "state" : ["A","B","C"]
    }
}

