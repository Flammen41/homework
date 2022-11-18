# import json
# from pprint import pprint
#
# import requests
#
# def play_with_pet(pet):
#     pet['status'] = 'pending'
#     pet['tags'].append({"id": 1, "name": "vasya"})
#
# json_response = requests.get("https://petstore.swagger.io/v2/pet/9223372036854398000")
# pet = json.loads(json_response.text)
# pprint(pet)
# play_with_pet(pet)
# pprint(pet)


with open('myfile1.bin', 'wb') as file:
    l=['what','form','toruowe']
    for item in l:
        s=str(item)+'\n'
        bt = s.encode('ascii')
        file.write(bt)


f=open('myfile1.bin', 'rb')
d=f.read()
print("d=",d)
print(bin(d[2]))
