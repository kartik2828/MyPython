from importlib.resources.readers import remove_duplicates

# If you're a beginner in List then you can start your python programming from this file

# How to create a list

L1 = [1,2,3,4,5]
print(L1)


# 1. Find the sum of all elements in a list.

l1 = [1,2,3,4,5,6]
sum=0
for i in l1:
    sum = sum + i
print(sum)

# 2. Find the largest element in a list.

l1 = [1,2,3,4,10,5]
largest = l1[0]
for i in l1:
    if i>largest:
        largest = i
print(largest)

# 3. Count occurrences of an element in a list.

l1 = [1, 2, 3, 4, 10, 5, 2, 2]
element_to_count = 2

count_ = l1.count(element_to_count)
print(count_)

# 4. Check if a list is empty.

l1 = [1,2,3]
l2 = []

if len(l2)==0:
    print("empty")
else:
    print("not empty")

# 5. Reverse a list.

l1 = [1,2,3,4,5]
reverse = l1[::-1]
print(reverse)

# 6. Remove duplicates from a list.

l1 = [1,2,2,3,4,5,5,6]

eleminate_dupliocates = list(set(l1))
print(eleminate_dupliocates)

# 7. Find the intersection of two lists.

l1 = [1,2,3,4,6,7,9]
l2 = [2,3,6,0,5,8]
l3 = []
for i in l2:
    if i in l1:
        l3.append(i)
print(l3)

# 8. Find the second largest element in a list.

l1 = [1, 2, 3, 4, 6, 7, 9]
largest = l1[0]
second_largest = l1[0]
for i in l1:
    if i>largest:
        second_largest = largest
        largest = i
print(second_largest)

# 9. Sort a list in ascending order.

l1 = [1, 2, 3, 5,9,6,5,3]
l1.sort()
print(l1)

# 10. Flatten a list of lists into a single list.

l1 = [[1, 2, 3], [4, 5], [6, 7, 8]]

flatten_list = []
for i in l1:
    for j in i:
        flatten_list.append(j)
print(flatten_list)

