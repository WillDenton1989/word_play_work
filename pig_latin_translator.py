 #pig latin exercise!
#isalph() would be helpful btw
words_list = ["apple", "cherry", "banana", "coke"]
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
vowels = ["a", "e", "i", "o", "u"]
consonants = "bcdfghjklmnpqrstvwxyz"

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

def translate_to_pig_latin(word):
    index = 0
    for letter in word:
        if(is_vowel(letter)):
            print("first vowel")
            break
        print(f"{letter} - {is_consonant(letter)}")
        index += 1

    print(f"index of last consanant {index}")
    leading_consonants = word[:index]
    rest_of_word = word[index:]
    return rest_of_word + leading_consonants + "ay"

def translate_list_to_pig_latin():
    for word in words_list:
        print(translate_to_pig_latin(word))
