"""This is a virtual Coffee machine"""
from art import logo
from data import MENU, resources
from time import sleep
from replit import clear

from src.Intermediate.Day15.simple_coffee import payment

# print(logo)

profit = 0


def set_profit(x):
    """To save data on profit"""
    global profit
    profit = profit + x


def choice():
    """To get user input if they would like to get another cup of coffee"""
    print(logo)
    order_again = input("Would you like to order again? Y or N : ").lower()
    if order_again == "y":
        return start()
    elif order_again == "admin":
        return process_admin()
    else:
        print("Invalid Input")


def process_admin():
    """This function for report and refill the coffee resources and turn off the machine."""
    print("Welcome to the Admin panel")
    """Report on resources and profit"""
    print("Current Resources")
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} ml")
    print(f"Money: ${round(profit, 2)}")
    check = input("What would you like to do? Homepage, refill or off: ").lower()
    if check == "homepage":
        choice()
    elif check == "refill":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        process_admin()
    elif check == "off":
        exit()
    else:
        print("Invalid Input")
        process_admin()


def process_making(user_choice, coffee):
    """Deduct the required ingredients from the resources."""
    for item in resources:
        resources[item] -= coffee[item]
    print(f"Enjoy your {user_choice} ☕")
    sleep(2)
    clear()
    choice()


def get_player_int(text):
    valid_user_input = False
    while not valid_user_input:
        a_string = input(text)

        try:
            user_input = int(a_string)

            if user_input > 0:
                valid_user_input = True
            else:
                print("You must enter a positive integer...")

        except:
            print("I'm terribly sorry, but we require an integer...")
    return user_input


def process_coins(coffee):
    """calculate the total money and check for change or refund """

    quarters = get_player_int("Please insert quarters: ") * 0.25
    dime = get_player_int("Please insert dimes: ") * 0.1
    nickle = get_player_int("Please insert nickles: ") * 0.05
    penny = get_player_int("Please insert penny: ") * 0.01

    total = (quarters + dime + nickle + penny)

    if total == coffee["cost"]:
        set_profit(coffee['cost'])
    elif total > coffee["cost"]:
        charge = total - coffee['cost']
        print(f"Here is your change ${round(charge, 2)}")
        set_profit(coffee['cost'])
    else:
        print(f"Sorry that's not enough money. Money refunded.${total}")
        sleep(2)
        clear()
        choice()
    return None


def check_resources(coffee):
    """TO check if resources are sufficient."""
    for item in resources:
        if resources[item] >= coffee[item]:
            return True
        else:
            print(f"Sorry there is not enough {item}.")
            sleep(2)
            clear()
            start()


def start():
    """To get user choice of coffee """
    print(logo)
    print("Here is what we offer:\nespresso:$1.5 \nlatte:$2.5 \ncappuccino:$3.0 ")
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    access = ["espresso", "latte", "cappuccino", "admin"]
    if user_choice in access:
        if user_choice == "admin":
            return process_admin()
        else:
            coffee = MENU[user_choice]
            if check_resources(coffee["ingredients"]):
                process_coins(coffee)
                if payment != 0:
                    process_making(user_choice, coffee["ingredients"])
    else:
        print("Invalid input")
        start()


start()
