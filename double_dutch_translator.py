#double dutch is wacky

import string

d_d_dict = {
        "b": "bub",
        "c": "cash",
        "d": "dud",
        "f": "fud",
        "g": "gug",
        "h": "hash",
        "j": "jay",
        "k": "kuck",
        "l": "lul",
        "m": "mum",
        "n": "nun",
        "p": "pub",
        "q": "quack",
        "r": "rug",
        "s": "sus",
        "t": "tut",
        "v": "vuv",
        "w": "wack",
        "x": "xux",
        "y": "yub",
        "z": "zub",
        }

vowels = ["a", "e", "i", "o", "u"]

sentence_1 = "i am the master of the universe"

def breakdown_user_input(user_input_string):
    delimiter = " "
    new_user_input = user_input_string.split(delimiter)
    return new_user_input

def is_consonant(letter):
    for vowel in vowels:
        if letter == vowel:
            return False
    return True

def is_vowel(letter):
    if(is_consonant(letter) == True):
        return False
    else:
        return True

def is_in_dict(letter):
    for x in d_d_dict:
        if x == letter:
            return d_d_dict.get(x)

def translate_to_dd(word):
    new_word = []

    for letter in word:
        if(is_vowel(letter)):
            new_word.append(letter)
        elif(is_consonant(letter)):
            syllable = d_d_dict[letter]
            for l in syllable:
                new_word.append(l)
    return "".join(new_word)

#def translate_list_to_dd():

#code start
print("Welcome to the double dutch translator.\nbtw dont use capital letters or numbers yet\n")
user_input_string = input("What should i translate into Double Dutch today?\n")
breakdown_user_input(user_input_string)
for word in breakdown_user_input(user_input_string):
    print(translate_to_dd(word))
