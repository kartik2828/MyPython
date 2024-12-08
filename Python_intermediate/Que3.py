
# 3. Count the frequency of each element in a list and return a dictionary.
# Write a function that takes a list of elements and returns a dictionary
# where the keys are the elements and the values are their respective counts in the list.


def cnt_frequency(list):
    frequency_dic = {}
    for element in list:
        if element in frequency_dic:
           frequency_dic[element] +=1
        else:
            frequency_dic[element] = 1
    return frequency_dic
my_list = [1,2,2,3,4,5,5,6,6,6,7]
result = cnt_frequency(my_list)
print(result)

