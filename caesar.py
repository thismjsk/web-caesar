import string

def alphabet_position(letter):
    ''' Receives a letter and returns a 0-based numerical position within the alphabet'''
    alphabet = string.ascii_lowercase
    # alphabet = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
    letter = letter.lower()
    position = alphabet.find(letter)
    return position

def rotate_character(char, rot):
    ''' Receieves a character and an integer, Returns new character the integer to the right'''
    if char.isalpha():
        original = alphabet_position(char)
        rotation = (original + rot) % 26
        rot_char = string.ascii_lowercase[rotation]

        if char.isupper():
            rot_char = rot_char.upper()
        elif char.islower():
            rot_char = rot_char.lower()
    else:
        rot_char = char

    return rot_char

def encrypt(text, rot):
    ''' Receive input of string and integer to rotate, returning the result of the rotation'''
    encrypted_text = ""
    for eachChar in text:
        crypt = rotate_character(eachChar, rot)
        encrypted_text = encrypted_text + crypt

    return encrypted_text
