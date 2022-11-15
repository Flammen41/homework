import random
#Task1
#
# message = "On a summer day somner smith went simming in the sun and his red skin stung"
# values=['Number', '']
# list = message.split()
# mydict = dict(zip(range(len(message))))
# print(mydict)
def Count(message):
    my_Dict = {}
    mySentence = message.lower().split()
    for word in mySentence:
        if word in my_Dict:
            my_Dict[word] += 1
        else:
            my_Dict[word] = 1
    return my_Dict
d = Count("On a summer day somner smith went simming in the sun and his red skin stung skin")
print(d)

############################################################3
#task2

#
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# total_price = {
#     key: stock.get(key, 0) * prices.get(key, 0) for key in prices.keys()
# }
# print(total_price)
###################################################################################
#Task3
# i_list = [i**2 for i in range(10)]
# # for x in range(10):
# #     i_list.append(x**2)
# print(i_list)

#
# #Task4
# days_of_week = (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
# dict = {"days_of_week"}

