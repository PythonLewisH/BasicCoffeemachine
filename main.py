MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
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


def run_report(money):
    print(f'{resources["water"]}ml')
    print(f'{resources["milk"]}ml')
    print(f'{resources["coffee"]}ml')
    print(f"${money}")


def enough_resources(user_choice):
    water = resources["water"] - (MENU[user_choice]["ingredients"]["water"])
    milk = resources["milk"] - (MENU[user_choice]["ingredients"]["milk"])
    coffee = resources["coffee"] - (MENU[user_choice]["ingredients"]["coffee"])
    if water < 0:
        print("Sorry there is not enough water")
        return False
    elif milk < 0:
        print("Sorry there is not enough milk")
        return False
    elif coffee < 0:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True


def enough_money(quarters, dimes, nickels, pennies, user_choice):
    money_inserted = 0
    money_inserted += (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    if money_inserted < MENU[user_choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_inserted == MENU[user_choice]["cost"]:
        print("Exact change received")
        return True
    else:
        change = round(money_inserted - MENU[user_choice]["cost"], 2)
        print(f"Here is ${change} in change")
        return True


def deduct_resources(user_choice):
    resources["water"] -= (MENU[user_choice]["ingredients"]["water"])
    resources["milk"] -= (MENU[user_choice]["ingredients"]["milk"])
    resources["coffee"] -= (MENU[user_choice]["ingredients"]["coffee"])


def make_coffee():
    machine_on = True
    money = 0

    while machine_on:

        # TODO: 1. Prompt user by asking what they would like
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # TODO: 2. Turn off the coffee Machine by entering "off" to the prompt
        if user_choice == "off":
            machine_on = False

        # TODO 3. Print report

        elif user_choice == "report":
            run_report(money)

    # TODO 4. Check resources are sufficient

        else:
            if enough_resources(user_choice):
                # TODO 5. Process coins

                quarters = float(input("How many quarters?: "))
                dimes = float(input("How many dimes?: "))
                nickels = float(input("How many nickles?: "))
                pennies = float(input("How many pennies?: "))

                # TODO 6. Check transaction successful

                # TODO 7. Make Coffee

                if enough_money(quarters, dimes, nickels, pennies, user_choice):
                    deduct_resources(user_choice)
                    print(f"Here is your {user_choice}, Enjoy!")
                    money += MENU[user_choice]["cost"]


make_coffee()
