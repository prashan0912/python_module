print("Welcome to the Lunch, Dinner claculator");
bill = float(input("what was the bill?"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
amt = bill + tip
total = amt/people
# actual_total = tip/100*bill+bill;
print("Each person should pay:",total);