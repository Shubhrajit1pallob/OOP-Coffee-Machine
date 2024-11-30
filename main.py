from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    option = menu.get_items()
    choice = input(f"What would you like to order. ({option}): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # Here the drink is the menuItem object that is created here that is to identify
        drink = menu.find_drink(choice)

        if money_machine.make_payment(drink.cost) and coffee_maker.is_resource_sufficient(drink):
            coffee_maker.make_coffee(drink)