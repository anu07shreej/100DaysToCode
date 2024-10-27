#Random Numbers
#import random
from random import randint
#
# print("Random num generated: ", randint(1,10))
# Pay the bill

# friends = ["Alice","Bob","Charlie","David","Emanuel"]
# num = len(friends)
#
# sel = randint(0,num)
# print(friends[sel])

#------Rock Paper Scissor--------------
choice = input("What do you choose? Rock 1 Paper 2 and Scissors 3?")
comp_choice = str(randint(1,3))

print("You chose: " + choice)
if choice == "1":
    print("ROCK")
    print('''
         _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
    ''')
elif choice == "2":
    print("PAPER")
    print('''
        _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
  
    ''')
elif choice == "3":
    print("SCISSORS")
    print('''
         _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
    ''')
else:
    print("Invalid choice")

print("Computer chose: " + comp_choice)
if comp_choice == "1":
    print("ROCK")
    print('''
             _______
          ---'   ____)
                (_____)
                (_____)
                (____)
          ---.__(___)
        ''')

elif comp_choice == "2":
    print("PAPER")
    print('''
        _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
    ''')
elif comp_choice == "3":
    print("SCISSORS")
    print('''
         _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
    ''')
else:
    print("Invalid choice")

if choice == comp_choice:
    print("Nobody wins!")
elif(   (choice == "1" and comp_choice == "2")
     or (choice == "2" and comp_choice == "3")
     or (choice == "3" and comp_choice == "1") ):
    print("Computer wins!")
elif(  (choice == "1" and comp_choice == "3")
     or (choice == "2" and comp_choice == "1")
     or (choice == "3" and comp_choice == "2")):
    print("You win!")


