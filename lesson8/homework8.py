from unittest import result

import kwargs as kwargs

################################################################
#Task1
# def favorite_movie(*movie):
#  print("My favorite movie is named " + movie[0])
#
# favorite_movie("Scarface", "Hitchikers", "Taxi")

# ################################################################
#Task2
def make_country(country, capital, **country_info):
 dict = {}
 dict["country"] = country
 dict["capital"] = capital
 for key, values in country_info.items():
  dict[key] = values
 return dict
info = make_country('USA', 'Washington')
print(info)

###############################
#Task3
# #
# def make_operation('+'):
#  return_value = 0
#  for num in args:
#   return_value += num**2
#  return return_value

# print(make_operation((7,11,4)))
# def custom_summer(a,b,c):
#  return a+b+c
# print(custom_summer(1,2,8))
