
# 7. Create a list of tuples where each tuple contains a key and its corresponding value from a dictionary.
# Given a dictionary, create a list of tuples where each tuple contains the key and its corresponding value.


def dict_to_tupleList(dict):

    return [(key,value) for key, value in dict.items()]

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
result = dict_to_tupleList(my_dict)
print(result)

