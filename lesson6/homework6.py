import random
#task1
# from random import sample
# list = sample(range(0,100),10)
# max_lists = max(list)
# print(max_lists)

from random import sample
# a = sample(range(1,11),10)
# i = 0
# while i < len(a):
#     number = i
#     j = i+1
#     while j < len(a):
#         if a[number] >a [j]:
#             number = j
#         j+=1
#     a[i],a[number]=a[number],a[i]
#     i+=1
# print(a[-1])

#task2
list_1 = tuple([random.randint(1, 100) for _ in range(10)])
list_2 = tuple([random.randint(1, 100) for _ in range(10)])
c = list_1.union(list_2)
print(c)
#Task3
