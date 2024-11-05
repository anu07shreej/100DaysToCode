#----------------Coffee Machine----------------
from coffee import MENU

WATER = 300
MILK = 200
COFFEE = 100

def report():
    global WATER, MILK, COFFFEE
    print("We have: ")
    print(f"{WATER} ml of water.")
    print(f"{MILK} ml of milk.")
    print(f"{COFFEE} g of coffee.")

def check_amount(quarters,dimes,nickels,cents):
    total = (quarters*0.25 + dimes*0.10 + nickels*0.05 + cents*0.01)
    print(f"That's a total of {total}")
    return total

def update_resources(water,milk,coffee):
    global WATER, MILK, COFFEE
    WATER -= water
    MILK -= milk
    COFFEE -= coffee

def check_resources(option):
    global WATER, MILK, COFFEE
    milk_enough = MILK >= MENU[option]['milk']
    water_enough = WATER >= MENU[option]['water']
    coffee_enough = COFFEE >= MENU[option]['coffee']
    if milk_enough and water_enough and coffee_enough:
        return True
    else :
        return False


print("            Welcome to the Coffee Machine!          ")
enough = True
give_coffee = False

#---------------1. Coffee Report --> How much resources are left?-------------
while enough:
    selection = ""
    to_do = input("What would you like? Espresso/Latte/Cappuccino? Type 'e', 'l' or 'c'").lower()
    if to_do == 'e':
        selection = 'espresso'
    elif to_do == 'l':
        selection = 'latte'
    elif to_do == 'c':
        selection = 'cappuccino'
    print(selection)
    report()

    enough = check_resources(selection)
    if enough:
        print(f"That will be ${MENU[selection]['price']} for the {selection}.")
        print("\n")
        print("Please insert coins.")
        num_quarters = int(input("How many quarters?"))
        num_dimes = int(input("How many dimes?"))
        num_nickels = int(input("How many nickels?"))
        num_cents = int(input("How many cents?"))
        amount = check_amount(num_quarters, num_dimes, num_nickels, num_cents)
        if amount == MENU[selection]["price"]:
            print("That's the right amount. Will get your coffee now!")
            give_coffee = True
        elif amount > MENU[selection]["price"]:
            print(f"Alright. This is your change back {amount - MENU[selection]["price"]}$. Will get your coffee now!")
            give_coffee = True
        else:
            print(f"Need more {MENU[selection]["price"] - amount}$. Then will get your coffee.")
            give_coffee = False

        if give_coffee:
            update_resources(MENU[selection]["water"], MENU[selection]["milk"], MENU[selection]["coffee"])
            print("\n")
            print(f"Here is your {selection}.")
    else:
        print(f"Don't have enough ingredients at the moment. Come back later?")
















