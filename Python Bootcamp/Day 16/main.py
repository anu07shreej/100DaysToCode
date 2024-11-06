from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_coffee_maker = CoffeeMaker()
my_menu = Menu()
my_money_machine = MoneyMachine()

run = True


while run :
    print("Welcome to the Coffee Machine")
    my_coffee_maker.report()
    print("\n")
    print("What do you want to get?")
    print(my_menu.get_items())
    selection = input("Type the name.")

    order =  my_menu.find_drink(selection)
    #print(order.cost)
    if my_coffee_maker.is_resource_sufficient(order):
        if my_money_machine.make_payment(order.cost):
            my_coffee_maker.make_coffee(order)
            my_money_machine.report()
    else:
        run = False








