logo = '''
 #     #                                  #######           #                                   
 #     # #  ####  #    # ###### #####     #     # #####     #        ####  #    # ###### #####  
 #     # # #    # #    # #      #    #    #     # #    #    #       #    # #    # #      #    # 
 ####### # #      ###### #####  #    #    #     # #    #    #       #    # #    # #####  #    # 
 #     # # #  ### #    # #      #####     #     # #####     #       #    # # ## # #      #####  
 #     # # #    # #    # #      #   #     #     # #   #     #       #    # ##  ## #      #   #  
 #     # #  ####  #    # ###### #    #    ####### #    #    #######  ####  #    # ###### #    # 
'''
from name_dict import name_list

import random
print("Let's play Higher or Lower!")
print(logo)

hasLost = False
select_list = random.sample(name_list, 2)
name1 = select_list[0]
name2 = select_list[1]
new_list = name_list
new_list.remove(name1)
new_list.remove(name2)
while not hasLost:

    print("Who do you think has more followers? \n")
    print(f"{name1["name"]}, who is a {name1["profession"]} from {name1["country"]}")
    print("OR")
    print(f"{name2["name"]}, who is a {name2["profession"]} from {name2["country"]}")
    guess = input(f"Type their name.{name1["name"]} or {name2["name"]} ").lower()
    print("\n")
    if name1["followersK"] > name2["followersK"]:
        if guess == name1["name"].lower():
            print("That's right!\n")
        else:
            print("No, that's wrong!")
            print(f"{name2["name"]} has {name2["followersK"]}k followers while {name1["name"]} has {name1["followersK"]}k followers")
            hasLost = True
    else:
        if guess == name2["name"].lower():
            print("That's right!\n")
        else:
            print("No, that's wrong!")
            print(f"{name1["name"]} has {name1["followersK"]}k followers while {name2["name"]} has {name2["followersK"]}k followers")
            hasLost = True
        name1 = name2


    if len(new_list) != 0:
        name2 = random.choice(new_list)
        #print(new_list)
        new_list.remove(name2)
    else:
        hasLost = True
        print("Well Done! You win! Game Over.")


