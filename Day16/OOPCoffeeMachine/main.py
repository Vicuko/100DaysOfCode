from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

class CoffeeMachine:

    def __init__(self):
        self.on = True
        self.menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()

    def start(self):
        while self.on:
            print("Welcome to your coffee machine!\n")
            request = input(f"\nWhat would you like? ({self.menu.get_items()}):").lower()
            if request == "off":
                self.on = False
                print ("Bye bye!")
            elif request == "report":
                self.coffee_maker.report()
                self.money_machine.report()
            else:
                order = self.menu.find_drink(request)
                if order:
                    sufficient_resources = self.coffee_maker.is_resource_sufficient(order)
                    if sufficient_resources:
                        cost = order.cost
                        print (f"\nIt will be {self.money_machine.CURRENCY}{cost}")
                        if self.money_machine.make_payment(cost):
                            self.coffee_maker.make_coffee(order)

my_coffee_machine = CoffeeMachine()
my_coffee_machine.start()

