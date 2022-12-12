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