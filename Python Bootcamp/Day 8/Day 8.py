# def greet_and_meet(name,location):
#     print(f"Hello {name}!")
#     print(f"What is it like in {location}")
#
# greet_and_meet("A","Switzerland?")
#---------------------------Ceaser Cypher -------------



alphabets =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input('Type "encode" to encrypt or "decode" to decrypt.\n').lower()
text = input("Type your message here. \n").lower()
shift_by = int(input("Type the shift number. \n"))

def encrypt(text, shift_by):
    encrypted_text=""
    for letter in text:
        if letter in alphabets:
            letter_index = alphabets.index(letter)
            if letter_index < len(alphabets)-shift_by:
                encrypted_text += alphabets[letter_index+shift_by]
            else:
                encrypted_text += alphabets[shift_by-(len(alphabets)-letter_index)]
        else:
            encrypted_text += letter
    print("Encrypted Text: ")
    print(encrypted_text)
    return(encrypted_text)

def decrypt(text, shift_by):
    decrypted_text = ""
    for letter in text:
        if letter in alphabets:
            letter_index = alphabets.index(letter)
            #shift = len(alphabets)-shift_by
            if letter_index >= shift_by :
                decrypted_text += alphabets[letter_index-shift_by]
            else:
                decrypted_text += alphabets[(len(alphabets)-(shift_by-letter_index))]
        else:
            decrypted_text += letter
    print("Decrypted Text: ")
    print(decrypted_text)
    return(decrypted_text)




