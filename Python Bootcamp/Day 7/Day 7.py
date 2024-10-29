#HANGMAN GAME
Hangman_pics = [
'''

''' 
'''

'''


]
import random

print("Welcome to Hangman!!")
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

word_list = ["Apple","Banana","Cherry","Dragonfruit"]

chosen_word = random.choice(word_list)
chosen_word_len = len(chosen_word)
print("Guess the word: "+ "__"*chosen_word_len)