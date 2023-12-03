MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_sufficient(drink_ing):
    """Sprawdź czy masz wystarczająco zasobów na zrobienie tej kawy."""
    for item in drink_ing:
        if drink_ing[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def press_coints():
    print("Please, insert coints: ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successfull(received_money, drink_cost):
    """Check czy wystarczajaco kaski dał"""
    if received_money >= drink["cost"]:
        change = round(received_money - drink_cost, 2)
        print(f"Great! You will receive ${change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, drink_ingr):
    for item in resources:
        resources[item] -= drink_ingr[item]
    print("Ready! Enjoy your coffe!")


is_on = True



while is_on:
    choice = input("Which drink you want? espresso, latte, cappucino?: ")
    if choice == "off":
        is_on = False
    elif choice == "raport":
        print(f'Water: {resources["water"]} ml')
        print(f'Milk: {resources["milk"]} ml')
        print(f'Coffe: {resources["coffee"]} ml')
        print(f'Money: $ {profit}')
    else:
        drink = MENU[choice]

        if is_sufficient(drink["ingredients"]):
            received_money = press_coints()
            if is_transaction_successfull(received_money, drink["cost"]):
                make_coffee(drink, drink["ingredients"])
