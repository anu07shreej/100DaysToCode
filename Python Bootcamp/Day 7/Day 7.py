#HANGMAN GAME

import random
from hangman import hangmanpics

print("Welcome to Hangman!!")
print("FRUIT EDITION!!")
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   
''')

word_list = ["Apple","Apricot","Avocado","Banana","Bilberry","Blackberry","Blackcurrant","Blueberry","Boysenberry","Currant","Cherry","Cherimoya","Chico fruit","Cloudberry","Coconut","Cranberry","Cucumber","Custard apple","Damson","Date","Dragonfruit","Durian","Elderberry","Feijoa","Fig","Goji berry","Gooseberry","Grape","Raisin","Grapefruit","Guava","Honeyberry","Huckleberry","Jabuticaba","Jackfruit","Jambul","Jujube","Juniper berry","Kiwano","Kiwifruit","Kumquat","Lemon","Lime","Loquat","Longan","Lychee","Mango","Mangosteen","Marionberry","Melon","Cantaloupe","Honeydew","Watermelon","Miracle fruit","Mulberry","Nectarine","Nance","Olive","Orange","Blood orange","Clementine","Mandarine","Tangerine","Papaya","Passionfruit","Peach","Pear","Persimmon","Physalis","Plantain","Plum","Prune","Pineapple","Plumcot","Pomegranate","Pomelo","Purple mangosteen","Quince","Raspberry","Salmonberry","Rambutan","Redcurrant","Salal berry","Salak","Satsuma","Soursop","Star fruit","Solanum quitoense","Strawberry","Tamarillo","Tamarind",	"Ugli fruit","Yuzu"]


chosen_word = random.choice(word_list).lower()
chosen_word_len = len(chosen_word)
word_list = list(chosen_word)

guess_list = list("_"*chosen_word_len)
print("Guess the word: "+ ''.join(guess_list))
hangman_cnt = 0
letters_guessed = 0

while (letters_guessed != chosen_word_len) and hangman_cnt != 6 :
    guess = input("Guess the letter").lower()
    letter_found = False
    for i in range(chosen_word_len):
        if guess == word_list[i]:
            letter_found = True
            letters_guessed += 1
            guess_list[i] = guess
            word_list[i] = '#'
            break
    if not letter_found:
        hangman_cnt += 1
        print(hangmanpics[hangman_cnt])

    print(''.join(guess_list))

if (letters_guessed != chosen_word_len) and hangman_cnt == 6 :
    print("GAME OVER!")
    print("Word was: "+ chosen_word.upper())

if (letters_guessed == chosen_word_len) and hangman_cnt != 0 :
    print("YOU GUESSED IT RIGHT! AWESOME!")







