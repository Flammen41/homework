import random
import math
import shlex
#task1
# game = random.randrange(1,10,1)
# answer = int(input("Guess what number is "))
# if answer == game:
#     print("You win")
# elif answer != game:
#     print("You lose game")

#task2
#
# name = input("Write your name ")
# age = int(input("Write your age "))
# i=age+1
# while age +1:
#     break
# print(f'Hello {name.capitalize()}, on your next birthday you’ll be {i} years')

#task3
from random import shuffle
word = list(input("Write your word to combine "))
i=0
while i !=5: #<len(word) или привязка к количеству символов в слове
    random.shuffle(word)
    i+=1
    print(''.join(word))
