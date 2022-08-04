#the transposition cypher
import string

sentence_1 = "i am the master of the universe"
#[*string.ascii_lowercase[-4:], *string.ascii_lowercase[:-4]]
#alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#genrate transpositional alphabet(offset)
#given the offset, generate a new dictionary where the keys are the regular alphabet and the values are the new ones.

def trans_dict(offset):
    alphabet = string.ascii_lowercase
    t_alphabet = [*alphabet[-offset:], *alphabet[:-offset]]
    # print(list(alphabet))
    # print(t_alphabet)
    return dict(zip(alphabet, t_alphabet))

def sanitize(message):
    sanitized = []
    for character in message:
        if(character.isalpha()):
            sanitized.append(character.lower())

    return "".join(sanitized)

def encode_string(message, dictionary):
    encoded_message = []

    for letter in message:
        encoded_letter = dictionary.get(letter)
        encoded_message.append(encoded_letter)

    return "".join(encoded_message)

def chunk_message(message, chunk_size):
    chunk_message = []
    index = 1
    for character in message:
        chunk_message.append(character)
        #print(f"index: {index} modulo: {index % chunk_size}")
        if(index % chunk_size == 0):
            chunk_message.append(" ")

        index += 1

    return "".join(chunk_message)

# ''' This function should add characters, if needed, to the message in order
#     to make the total length of the message an even multiple of the chunk_size. For example:
#     if the message is 17 characters long and the chunk size is 5, then you need to add 3 characters to
#     get to a length of 20, which is an even multiple of 20.
# '''
def pad_message(message, chunk_size):
    message_length = len(message)
    new_message_list = []
    remainder = message_length % chunk_size
    # print(f"remainder: {remainder} message_length: {message_length} chunk size: {chunk_size}")
    if(message_length % chunk_size == 0):
        return message
    elif(message_length % chunk_size != 0):
        new_message_list.append("x" * remainder)
        x = message.join(new_message_list)
        return message + x

def encode(message, chunk_size, offset):
    message = encode_string(sanitize(message), trans_dict(offset))
    print(message)
    message = pad_message(message, chunk_size)
    print(message)
    message = chunk_message(message, chunk_size)
    return message

#code start.
user_input = input("Input your message.\n")
#test_message = "billmiketwoelectricboogaloo"
print(encode(user_input, 5, 4))
