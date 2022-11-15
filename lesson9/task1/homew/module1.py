def make_country(country, capital, **country_info):
 dict = {}
 dict["country"] = country
 dict["capital"] = capital
 for key, values in country_info.items():
  dict[key] = values
 return dict
info = make_country('USA', 'Washington')
print(info)