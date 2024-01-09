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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO'S:-
# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: 3. Print report.
# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins.
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.


new_key, new_value = "money", 0
new_dict = resources.copy()
new_dict[new_key] = new_value

quarters, dimes, nickles, pennies = 0, 0, 0, 0


def coin_store():
    global quarters, dimes, nickles, pennies
    print("Please insert coins:")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickels: "))
    pennies = int(input("Pennies: "))


def choose():
    global choice
    choice = input('What would you like? (espresso/latte/cappuccino): ')


def order(choice):
    if choice == "report":
        for key, value in new_dict.items():
            print(key, ":", value)
    else:
        if new_dict['water'] < MENU[choice]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif new_dict['coffee'] < MENU[choice]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        elif choice != "espresso" and new_dict['milk'] < MENU[choice]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        else:
            coin_store()


def coin_processing(quarters, dimes, nickles, pennies):
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    print(f"Total inserted: ${total:.2f}")

    if total >= MENU[choice]["cost"]:
        new_dict[new_key] += MENU[choice]["cost"]
        change = total - MENU[choice]["cost"]
        print(f"Here is your {choice}. Enjoy! Your change: ${change:.2f}")
    else:
        print("Sorry that's not enough money. Money refunded.")


def make_coffee(choice, MENU):
    element = MENU[choice]["ingredients"]
    for item in element:
        new_dict[item] -= element[item]
        if new_dict[item] < 0:
            return
    coin_processing(quarters=quarters, dimes=dimes, nickles=nickles, pennies=pennies)





while True:
    choose()
    if choice in ["espresso", "latte", "cappuccino", "report"]:
        order(choice=choice)
        if choice != "report":
            make_coffee(choice, MENU)

    else:
        print("Switching off machine.")
        break
