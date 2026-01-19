from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
machine = MoneyMachine()
coffee_maker = CoffeeMaker()

coffee_program = True
while coffee_program:
    coffee_menu = menu.get_items()
    coffee_order = input(f"何になさいますか？({coffee_menu}): ").lower()
    if coffee_order == "off":
        coffee_program = False
    elif coffee_order == "report":
        coffee_maker.report()
        machine.report()
    else:
        drink = menu.find_drink(coffee_order)
        # print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            if machine.make_payment(drink.cost):#20,21行はandでまとめられる
                coffee_maker.make_coffee(drink)

