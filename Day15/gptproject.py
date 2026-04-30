# Coffee Machine Program (Procedural Approach)

# MENU with ingredients and cost
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

# Machine resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0  # total profit


# ---------------- FUNCTIONS ---------------- #

def print_report():
    """Print current resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources.get('milk', 0)}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(drink):
    """Check if enough resources exist"""
    for item in drink["ingredients"]:
        if resources.get(item, 0) < drink["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def process_coins():
    """Calculate total money inserted"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    total = quarters + dimes + nickels + pennies
    return round(total, 2)


def check_transaction(inserted_money, cost):
    """Check if payment is enough"""
    global money
    if inserted_money < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(inserted_money - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
            money += cost
            return True


def make_coffee(drink_name, drink):
    """Deduct resources and serve coffee"""
    for item in drink["ingredients"]:
        resources[item] -= drink["ingredients"][item]

        print(f"Here is your {drink_name}. Enjoy!")


        # ---------------- MAIN LOOP ---------------- #

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        print_report()

    elif choice in MENU:
        drink = MENU[choice]

    if check_resources(drink):
        payment = process_coins()

    if check_transaction(payment, drink["cost"]):
        make_coffee(choice, drink)

    else:
        print("Invalid choice. Try again.")