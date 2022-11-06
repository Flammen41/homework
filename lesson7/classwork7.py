# Compute the average of tuple items
from random import *
list1 = tuple([randint(1,10) for i in range(20)])
#
# print(sum(list)/len(list))

import random

list_1 = tuple([random.randint(1, 100) for _ in range(20)])
print(list_1)
print(sum(list_1) / len(list_1))

# 2. Reverse list using while loop
new_list_1 = []
i = -1
while i != -len(list_1)-1:
    new_list_1.append(list_1[i])
    i -= 1
print(new_list_1)

# Remove an empty tuple(s) from a list of tuples
arr = [(1,2), (True, "fefse"), (), (), ()]

while () in arr:
    arr.remove(())
print(arr)

# Turn every item of a list into its square
list_4 = [2,4,6]
list_5 = [i * i for i in list_4]
print(list_5)

# Program to convert Set into Tuple and Tuple into Set
my_tuple = tuple(list_1)
print(type(my_tuple))
my_set= set(my_tuple)
print(type(my_set))
# Multiply all numbers in the list/tuple/set
print(sum(list_1) * len(list_1))

# Given list of tuples, remove all the tuples with length K
# Given a list of integers with duplicate elements in it. Generate another list, which contains only the duplicate elements and prints back to user
# Remove empty List from List
# Get Only unique items from two sets
# Concatenate two lists index-wise
arr1 = [1,2,3]
arr2 = [4,5,6]
for i in range(len(arr2)):
    arr1 += [arr2[i]]
print(arr1)

# Remove all occurrences of a specific item from a list
# Swap two tuples in Python