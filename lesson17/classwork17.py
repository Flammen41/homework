# from module import Car
# a = Car('audi',2020,'black') # 3
# print(a.move_forward(20))
#
# a.set_model('bmw')
# print(a.get_model())
######################
class Car:
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        self.__color = color

    def move_forward(self, speed):
        self.speed = speed
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

a = Car('audi',2020,'black') # 3
print(a.move_forward(20))

a.set_model('bmw')
print(a.get_model())
########################################

class Phone:
    def __init__(self, sim):
        self.__sim = sim


class MobilePhone(Phone):
    def __init__(self, sim, number, contacts):
        super().__init__(sim)
        self.number = number
        self.__contacts = contacts
    def get_contacts(self):
        return list(map(lambda x:x+"-work", self.__contacts))

a = Phone(True)
a1= MobilePhone(a, "093445694",["Artur","Vlad","Yaroslav"])
print(a1.get_contacts())
################################################################

