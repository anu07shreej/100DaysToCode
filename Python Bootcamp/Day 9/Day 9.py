# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# student_grades = {}
# for k in student_scores:
#     score = student_scores[k]
#     if score < 100 and score >= 91:
#         student_grades[k] = "Outstanding"
#     elif score < 90 and score >= 81:
#         student_grades[k] = "Exceeds Expectations"
#     elif score < 80 and score >= 71:
#         student_grades[k] = "Acceptable"
#     else:
#         student_grades[k] = "Fail"
#
# print(student_grades)

#---------------AUCTION------------

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
''')
print("Welcome to secret auction program")
y_n = 'yes'
bid_dict = {}

while y_n == 'yes' or y_n == 'y':
    name = input("What is your name?")
    bid = float(input("What is your bid?"))
    bid_dict[name] = bid
    print("\n" * 100)
    y_n = input("Are there any other bidders? Type 'yes or 'no'").lower()


v = list(bid_dict.values())
#print(v)
k = list(bid_dict.keys())
#print(k)
max_val = max(v)
#print(max_val)
print(f"The winner of the auction is: {k[v.index(max_val)]} and their bid is: {max_val}")

