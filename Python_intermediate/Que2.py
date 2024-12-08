# 2. Sort a list of tuples based on the second element in each tuple.
# Given a list of tuples, sort the list based on the second element of each tuple.

l1 = [(1, 2), (3, 1), (4, 5), (2, 3)]

sorted_list = sorted(l1, key =lambda x:x[1])
print(sorted_list)
