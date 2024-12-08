# 1. Find the common elements between two lists.
# Given two lists, write a function to find the common elements between them.

l1 = [1,2,4,8]
l2 = [2,3,4,5,6,7]
common_element =[]
def my_func():
    for i in l2:
        if i in l1:
            common_element.append(i)
    return common_element
result  = my_func()
print(result)

