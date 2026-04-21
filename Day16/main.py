

# from another_module import another_variable
# import another_module

# print(another_variable)
# print(another_module.another_variable) 
# print(another_module)
# print(type(another_module))



#############################


# constructing object and accessing their attributes and methods 
# from turtle import Turtle , Screen 

#class -> object() 
# timmy = Turtle();   # here turtle is class and timmy is object 
# print(timmy)
# timmy.shape()
# timmy.color("red")
# timmy.forward(100)
# timmy.circle(200)


# my_screen = Screen();
# print(my_screen.canvheight)
# print(my_screen.window_width())
# my_screen.exitonclick()



###########################################
# How to add python package using PyPi (python package index)


# import prettytable 

from prettytable import PrettyTable

table = PrettyTable()

# Add columns
table.add_column("Name", ["Virat Kohli", "MS Dhoni", "Rohit Sharma"])
table.add_column("Profession", ["Cricketer", "Cricketer", "Cricketer"])
table.add_column("Followers", [10000000, 8500000, 9200000])

print(table)

#######################################

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Name", "Profession", "Followers"]

table.add_row(["Virat Kohli", "Cricketer", 10000000])
table.add_row(["MS Dhoni", "Cricketer", 8500000])
table.add_row(["Rohit Sharma", "Cricketer", 9200000])

print(table)