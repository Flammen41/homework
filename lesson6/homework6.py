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
# list_1 = set([random.randint(1, 10) for _ in range(10)])
# list_2 = set([random.randint(1, 10) for _ in range(10)])
# list_3 = list()
# for i in list_1:
#      if i in list_2 and i not in list_3:
#         list_3.append(i)
# print(list_3)
#Task3
list_4 = set([random.randint(1, 100) for _ in range(100)])
list_5 = list()
i = 0
for i in list_4:
    if (i%7==0) and not (i*5==0):
        list_5.append(i)
# while i in list_4:
#     list_5 = list_5 + (random.randint(1, 100),)
#     i = i + 7
print(list_5)