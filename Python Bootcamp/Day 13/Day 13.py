#DEBUG

import random

def add (n1,n2):
    return n1 + n2

def mutate(a_list):
    b_list = []
    new_item = 0
    for num in a_list:
        new_item = new_item*2
        new_item += random.randint(1,3)
        new_item = add(new_item,num)
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])