#Day 12 files
#Number Guessing Game
import random

print("Welcome to the Number Thinking Game!")
print("\n")


play = True

while play == True:
    print("I'm thinking of a number between 1 and 100 \n")
    num = random.randint(1, 100)
    choice = input("Choose a difficulty level. Type 'easy' or 'hard'").lower()
    attempts = 0
    if choice == 'easy':
        attempts += 10
    elif choice == 'hard':
        attempts += 5
    print(f"You have {attempts} attempts remianing to guess the number.")
    while attempts != 0:
        guess = int(input ("Make a guess"))
        diff = abs(guess - num)
        if diff == 0:
            print(f"That's right. You guessed it correct! The number is {num}")
            play = input("Wanna play again? Type 'y or 'n'").lower()
            if play == 'y':
                play = True
            else:
                play = False
        elif diff <= 3:
            attempts -= 1
            if attempts != 0:
                print(f"That's very near to the actual number. Make another guess. You have {attempts} more attempts left.")
        elif diff <= 6:
            attempts -= 1
            if attempts != 0:
                print(f"That's near. Make another guess. You have {attempts} more attempts left.")
        elif diff > 6:
            attempts -= 1
            if attempts != 0:
                print(f"That's far. Make another guess. You have {attempts} more attempts left.")
    print(f"You lose. All your attempts were wrong. The number was {num}.")
    play = input("Wanna play again? Type 'y or 'n'").lower()
    if play == 'y':
        play = True
    elif play == 'n':
        play = False










