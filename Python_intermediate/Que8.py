
# 8. Check if a tuple contains any duplicate elements.
# Write a function to check whether a tuple contains any duplicate elements and return `True` or `False`.

def duplicate_element(tuple):
    return len(tuple) != len(set(tuple))

my_tuple = (1, 2, 2, 3, 4, 4, 5, 5, 5)
result = duplicate_element(my_tuple)
print(result)
