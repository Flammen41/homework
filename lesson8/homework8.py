import numbers
from unittest import result
import operator
import kwargs as kwargs

################################################################
#Task1
# def favorite_movie(*movie):
#  print("My favorite movie is named " + movie[0])
#
# favorite_movie("Scarface", "Hitchikers", "Taxi")

# ################################################################
#Task2
# def make_country(country, capital, **country_info):
#  dict = {}
#  dict["country"] = country
#  dict["capital"] = capital
#  for key, values in country_info.items():
#   dict[key] = values
#  return dict
# info = make_country('USA', 'Washington')
# print(info)

###############################
#Task3
def make_operation(operator, numbers_list):
    total=0
    if operator == '+':
        for num in numbers_list:
            total+=num
    print (total)
make_operation('+', (6,8,9))