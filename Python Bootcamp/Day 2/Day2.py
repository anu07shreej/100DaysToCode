# print(type(1234))
# print(type("Hello"))
# print(type(True))
# print(type(123.456))
#
# print("abc"+str("123"))
#
# print(5 % 2)
# # print(2 ** 3)
#
# a = 3 * 3 + 3 / 3 - 3
# print(round(a,1))
#
# score = 34.5
# print(f"Your score is: {score}")
from sympy import floor

# Tip Calculator
print("Welcome to the tip calculator!")
bill_amt = float(input("What was the total bill? "))
tip_prc = float(input("What much tip would you like to give? 10, 12, or 15? "))
num_ppl= int(input("How many people to split the bill?"))
tip_per_person = (bill_amt * (1 + tip_prc)) / num_ppl
tip_total=round(tip_per_person,2)

print(f"Each person should pay: {tip_total}")

