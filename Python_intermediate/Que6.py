from itertools import count


# 6. Find the longest word in a list of strings and return its length.
# Write a function to find the longest word in a list of strings and return its length.


def longest_word(list):

    result = max(list, key = lambda x: len(x))
    return len(result)

my_list_of_strings = ["apple", "banana", "cherry", "date", "elderberry"]
obj = longest_word(my_list_of_strings)
print(obj)


