#-------------------------CALCULATOR ----------------------
print('''
 __________
| ________ |
||12345678||
|""""""""""|
|[M|#|C][-]|
|[7|8|9][+]|
|[4|5|6][x]|
|[1|2|3][%]|
|[.|O|:][=]|
"----------"

''')

def calc (n1, first_time= True):
    result = 0.0
    operation = input("Pick an operation: + - * /")
    if first_time:
        num1 = float(input("What's the first number?"))
    else:
        num1 = n1
    num2 = float(input("What's the next number?"))
    if operation == "+":
        result += num1+num2
        print(f"{num1} {operation} {num2} = {result}")
    elif operation == "-":
        result += num1-num2
        print(f"{num1} {operation} {num2} = {result}")
    elif operation == "*":
        result += num1*num2
        print(f"{num1} {operation} {num2} = {result}")
    elif operation == "/":
        result += num1/num2
        print(f"{num1} {operation} {num2} = {result}")
    else:
        print("Invalid operation selected.")

    choice = input(f"Type 'y' to continue with {result} or type 'n' to start with new calculation")
    if choice == 'y':
        calc(result, False)
    else:
        calc(0.0, True)

calc(0.0, True)

