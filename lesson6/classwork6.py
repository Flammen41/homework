#Явное создание списка через фигурные скобки и кому перечисляющий список
test1 = {1,2,3,4,5,4}
print(test1)
#Через конструктор передать список или создать переменную и поместить в конструктор
st = 'dsgtrt'
    test2 = set(1,2,3)
print(test2)

# •Union and Intersection обьединение список
# set1 = {1, 2, 3, 4, 98, 11, 23, 4}
# set2 = {5, 6, 7, 4, 8, 98}
# set3 = set1.union(set2) #объединение
# set3 = set1 | set2  #объединение
# set3 = set1 & set2  #пересечение

# set4 = set1.difference(set2)
# set5 = set2.difference(set1)
# set6 = set1 - set2
# print(set6, set4)

#Copying
# set3 = set1.copy()
# set1.add(105)
# print(set1, set3)


#Iterating
# for i in set1:
#     print(i)

#Find maximum from set of ints
print(max(set1))
#
first_set = {1, 2, 3, 4, 5}
first_set_2 = {1, 2, 3, 4, 6}
first_set.add((1, 2, 3))
# first_set.discard(9) # discard игнорирует элемент в множестве
# first_set.remove() # remove удаляет элемент  в множестве
print(first_set)
print(first_set.pop())
print(first_set)
print(first_set_2.clear())
print(first_set_2)
