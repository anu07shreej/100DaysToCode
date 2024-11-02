from blackjack_art import blackjack_art

print("Welcome to BlackJack!!")
print(blackjack_art[0])
#Cards

cards = ['Ace','2','3','4','5','6','7','8','9','Jack','Queen','King']
cards_val ={'Ace':[1,11],'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'Jack':10,'Queen':10,'King':10 }
suits = ["Heart","Spade","Diamond","Club"]

import random

val_player = 0
val_computer = 0
player_aces= 0
print("Lets play!")
print("\n")
print("First card for player A:")
player_card_1 = random.choice(suits) +" "+  random.choice(cards)
print(f"{player_card_1}")

if  player_card_1.split(' ')[1] == 'Ace':
    player_aces += 1
val_player =  cards_val[player_card_1.split(' ')[1]]


print("Second card for player A:")
player_card_2 = random.choice(suits) +" "+ random.choice(cards)
print(f"{player_card_2}")

if player_aces == 0 :
    if  player_card_2.split(' ')[1] != 'Ace':
        val_player +=  cards_val[player_card_2.split(' ')[1]]
    else:
        player_aces += 1
else:
    print(val_player)


print("First card for computer is:")
computer_card_1 = random.choice(suits) +" "+ random.choice(cards)
print(f"{computer_card_1}")



print("Second card for computer is:")
computer_card_2 = random.choice(suits) +" "+ random.choice(cards)
#print(f"{computer_card_2}")

third_draw = input("Do you want to draw the third card? Type 'y' or 'n'").lower()
if third_draw == 'yes' or third_draw == 'y':
    print("Third card for player A:")
    player_card_3 = random.choice(suits) + " " + random.choice(cards)
    print(f"{player_card_3}")
    if player_card_3.split(' ')[1] != 'Ace':
        val_player += cards_val[player_card_3.split(' ')[1]]
        if val_player > 21:
            print("You loose! :( ")
        else:
            print(f"Your score is {val_player}")



