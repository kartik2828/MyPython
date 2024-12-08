# 9. Flatten a list of tuples into a single list of elements.
# Given a list of tuples, flatten it into a single list by extracting all the elements from the tuples.

def flatten_list(list):
    flatten_list = []
    for i in list:
        for j in i:
            flatten_list.append(j)
    return flatten_list

l1 = [(1, 2, 3), (4, 5), (6, 7, 8)]
re = flatten_list(l1)
print(re)

