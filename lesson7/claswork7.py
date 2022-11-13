# task 3
# arr = [(1,2), (True, "fefse"), (), (), ()]

# while () in arr:
#     arr.remove(())
# print(arr)

# task 7
# k = int(input("Choose a count of tuple from 1 to 5: "))
# arr1 = [(1,),(2, 2), (3, 3, 3), (4, 4, 4, 4), (5, 5, 5, 5, 5), (2, 2)]
# for i in arr1:
#     if len(i) == k:
#         arr1.remove(i)
# print(arr1)

# task 9
# box3 = [1,2,3, [], 6 ,5 , 4, []]
# while [] in box3:
#     box3.remove([])
# print(box3)

# task 8 
# box = [1,1,1 , 2, 64, 5 , 5 , 8]
# box2 = list()
# st = set(box)
# for i in st:
#     if box.count(i) > 1:
#         box2.append(i)
# print(box2)

# task 11
# arr1 = [1,2,3]
# arr2 = [4,5,6]
# for i in range(len(arr2)):
#     arr1 += [arr2[i]]
# print(arr1)

# superbox = [i for i in range(10)]
# superbox = [i for i in superbox if i not in (1, 5, 7)]
# print(superbox)

# list_1 = list()
# for i in range(700,4000,130):
#     list_1.append(i)

# task 1
# list_2 = [i for i in range(700,4000,130)]
# print(list_2)

# task 2
# ______________________________
# sentence = 'On a summer day somner smith went simming in the sun and his red skin stung'
# sentence = sentence.split(" ")
# box = []
# for i in sentence:
#     if len(i) < 5:
#         box.append(i)
# print(box)
# # __________________________
# sentence = 'On a summer day somner smith went simming in the sun and his red skin stung'
# sentence = [word for word in sentence.split() if len(word) < 5]
# message = ''
# for i in sentence:
#     message += i + " "
# print(sentence)
# print(message)

# task 3
# list_1 = [1,6,7,8,3,1,4]
# list_2 = [5,1,8,3,7,7]
# list_3 = [item for item in list_1 if item in list_2]
# print(list_3)

# task 4
# list_1 = [1, 2, -5, -7 , 8 , -3]
# print(list_1)
# list_2 = ["plus" if i > 0 else "minus" for i in list_1]
# print(list_2)

#----------dictionary-----------------
# task 1
fruits = {"apple": 5,
          "orange": 8,
          "plum": 3,
          "pear": 9
          }

# print(fruits["apple"])
# print(sum([cost for cost in fruits.values()]))
# print(fruits.items())

# dict_2 = {  5: "hello",
#             2: "world",
#             6: "feufueh",
#             1: "ewqret"
#         }       
# print(dict_2.items())

# task 2
# fr = input("Write a fruit name: ")
# if fruits.get(fr) is None:
#     print("No such fruit here.")
# else:
#     print(f"{fr} costs {fruits.get(fr)}.")
