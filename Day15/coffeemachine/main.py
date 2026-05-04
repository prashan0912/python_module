



from data import menu
from data import resource

def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item]>=resource[item]:
            print(f"sorry there is not enough{item}")
            is_enough = False

def process_coin():
    print("insert coin")    
        
    
    
is_on = True
while not is_on:
    
    choice = input("Enter what would you like?(espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice =="report":
        print(f"Water:{resource["water"]} ml")   
        print(f"coffee:{resource["coffee"]} ml")   
        print(f"milk:{resource["milk"]} gm")   
        print(f"money:{resource["money"]} ₹")   

    elif choice ==""     
    choose_menu(my_input);
    
        