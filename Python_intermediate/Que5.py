# 5. Merge two dictionaries by adding values for common keys.
# Given two dictionaries, merge them by adding the values for the common keys
# and keeping the values from both dictionaries for unique keys.


def merge_two_dict(dict1, dict2):
    for i in dict2:
        if i in dict1:
            dict1[i] += dict2[i]
        else:
            dict1[i] = dict2[i]
    return dict1

dictionary1 = {'a': 1, 'b': 2, 'c': 3}
dictionary2 = {'b': 3, 'c': 4, 'd': 5}

result = merge_two_dict(dictionary1,dictionary2)
print(result)
