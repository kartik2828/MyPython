# 4. Remove a key from a dictionary if it exists, and return the updated dictionary.
# Given a dictionary and a key, remove the key if it exists in the dictionary
# and return the updated dictionary.


def remove_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary

my_dict = {1:'a',2:'b',3:'c',4:'d',5:'e'}
key_to_remove = 2
result  = remove_key(my_dict,key_to_remove)
print(result)



