# def make_country(country, capital, **country_info):
#  dict = {}
#  dict["country"] = country
#  dict["capital"] = capital
#  for key, values in country_info.items():
#   dict[key] = values
#  return dict
# info = make_country('USA', 'Washington')
# print(info)


def join(lists):
result = ([])
for list in lists:
 result.extend(list)
return result

join([1, 2, 3], [4, 5, 6], [1, 123, 98, 97, 88, 78, 68, 58, 48, 38, 88, 98], [-1, 0, 100])