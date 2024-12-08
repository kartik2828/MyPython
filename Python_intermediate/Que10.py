from Python_intermediate.Que8 import result


# 10. Write a function to find the intersection of two dictionaries.
# Given two dictionaries, write a function to find the common keys and their corresponding values in both dictionaries.

def common_element(dic1,dic2):
    intersection = {}
    for i in dic2:
        if i in dic1:
            intersection[i] =dic1[i]

    return intersection

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'b': 2, 'c': 3, 'e': 5, 'f': 6}
obj = common_element(dict1,dict2)
print(obj)