# # task1 Create a list from elements of a range from 700 to 4000 with steps of 130, using list comprehension.
#
# # list_1 = list()
# # for i in range(700, 4000,130):
# #     list_1.append([i])
# #     print(list_1)
# # task1
# # list_2 = [i for i in range(700, 4000,130)]
# # print(list_2)
#
#task2 Find all of the words in a string that are less than 5 letters
#________________________________________________________________
# sentence = 'On a summer day somner smith went simming in the sun and his red skin stung'
# sentence = sentence.split(" ")
# box = []
# for i in sentence:
#     if len(i) < 5:
#         box.append(i)
# print(box)
################################################################
# sentence = 'On a summer day somner smith went simming in the sun and his red skin stung'
# sentence = [word for word in sentence.split(" ") if len(word) < 5] # splitting sentence into words
# message = ''
# for i in sentence:
#     message += i + ""
# print(sentence)
# print(message)
#Task3 Find the the same numbers in two lists (without using a tuple or set)
# list_1 = [1, 2, 3, 4, 4, 3, 5]
# list_2 = [5, 2, 3, 7, 9, 1, 5]
# list_3 = [item for item in list_1 if item in list_2]
# print(list_3)
#Task4 Produce a list containing the word ‘minus’ if a number in the numbers is < 0, and the word ‘plus’ if the number is > 0. Result would look like [‘plus’, ’plus’, ‘minus’]

# list_1 = [1, 2, 3, -1, 2, -3]
# list_1 = ["plus" if i > 0 else "minus" for i in list_1]
# print(list_1)

#Task5 Write a program to sum all the items in a dictionary
fruits = {"apple": 5,
          "orange": 8,
          "plum": 3,
          "pear": 9,}

# print(fruits["apple"])
# print(sum([cost for cost in fruits.values()]))
# print(fruits.items())
# print(fruits.keys())

#Task6 Check whether a given key already exists in a dictionary. And print appropriate statement to user.
fr = input("Write a fruits name: ")
#print(fruits.get("apple"))
if fruits.get(fr) is None:
    print("No such fruits")
else:
    print(f"{fr} costs {fruits.get(fr)}")
#print(fruits.get(""))


#Task7 Write an address book, using dictionaries, where I can query contact info, insert new contact, delete contact information, exit address book program
