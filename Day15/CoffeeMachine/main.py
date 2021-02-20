from resources import MENU, resources

POWER_ON = True
RESOURCES = resources
RESOURCES["money"] = 0

# TODO 2 - Create function to prompt user for information -- DONE
def prompt_user():
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return request

# TODO 4 - Create function to print report of machine status -- DONE
def print_report():
    report = \
f"""
Water: {RESOURCES["water"]}ml
Milk: {RESOURCES["milk"]}ml
Coffee: {RESOURCES["coffee"]}ml
Money: ${RESOURCES["money"]}
"""
    print(report)

# TODO 5 - Create function to check if there are enough resources for the request -- DONE
def confirm_request(request):
    """
    Checks if there are enough resources for the request. If there are, it returns
    the cost of the request, otherwise, it returns False
    """
    resources_available = True
    non_available_resources = []
    for ingredient, amount in MENU[request]["ingredients"].items():
        if amount > RESOURCES[ingredient]:
            resources_available = False
            non_available_resources.append(ingredient)

    if not resources_available:
        print(f"Sorry, there is not enough {' nor '.join(non_available_resources)}.\n")
        return False
    else:
        return MENU[request]["cost"]

# TODO 6 - Create function to introduce amount of coins -- DONE
def introduce_coins():
    print ("Please introduce the money: ")
    quarters = float(input("How many quarters? ")) * 0.25
    dimes = float(input("How many dimes? ")) * 0.1
    nickles = float(input("How many nickles? ")) * 0.05
    pennies = float(input("How many pennies? ")) * 0.01

    total_amount = quarters + dimes + nickles + pennies
    return total_amount

# TODO 7 - Create function to confirm amount introduced (refund, add, change) -- DONE
def confirm_total_amount(money_introduced, cost):
    if money_introduced < cost:
        print ("Sorry, that's not enough money. Money refunded.\n")
        return False
    elif money_introduced > cost:
        print (f"Here is ${round(money_introduced - cost, 2)} dollars in change.\n")

    return True

# TODO 8 - Create function for making coffee -- DONE
def make_coffee(coffee):
    for ingredient, value in MENU[coffee]["ingredients"].items():
        RESOURCES[ingredient] -= value
    RESOURCES["money"] += MENU[coffee]["cost"]
    print_report()
    print (f"Here is your {coffee}. Enjoy!")

# TODO 1 - Create function to manage the whole process with customers
def operate():
    global POWER_ON
    while POWER_ON:
        request = prompt_user()
        # TODO 3 - Turn off the machine when receiving the "off" command -- DONE
        if request == "off":
            POWER_ON = False
        elif request in MENU:
            print_report()
            cost = confirm_request(request)
            if cost:
                print (f"That will be ${cost}\n")
                money_introduced = introduce_coins()
                enough_money = confirm_total_amount(money_introduced, cost)
                if enough_money:
                    make_coffee(request)
        else:
            print ("Sorry, but that is not in the menu. Please try again.\n")

operate()
