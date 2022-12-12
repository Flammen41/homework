# #Task1
# class Person( object ):
#     def __init__( self, firstname, lastname, age ):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#     def talk( self ):
#         print( "Hello, my name is {0} {1} and I'm {2} years old".format( self.firstname, self.lastname, self.age ) )
#
# jim = Person( "Jim", "Carrey", 64 )
# jim.talk()
########
#Task2
# age_factor = 7
#
# class Dog:
#     def __init__( self, age ):
#         self.age = age
#     def human_age( self ):
#         return( self.age * age_factor )
#
# d = Dog(3)
# print(d.human_age())
#########
#Task3

# class TVController:
#     def __init__(self):
#         self.channels = ["BBC", "CNN", "ESPN", "FOX"]
#         self.current_channel = 0
#
#     def first_channel(self):
#         self.current_channel = 0
#
#     def last_channel(self):
#         self.current_channel = len(self.channels) - 1
#
#     def turn_channel(self, N):
#         if N > 0 and N <= len(self.channels):
#             self.current_channel = N - 1
#
#     def next_channel(self):
#         if self.current_channel == len(self.channels) - 1:
#             self.current_channel = 0
#         else:
#             self.current_channel += 1
#
#     def previous_channel(self):
#         if self.current_channel == 0:
#             self.current_channel = len(self.channels) - 1
#         else:
#             self.current_channel -= 1
#
#     def current_channel(self):
#         return self.channels[self.current_channel]
#
#     def is_exist(self, N_or_name):
#         if type(N_or_name) == int:
#             if N_or_name > 0 and N_or_name <= len(self.channels):
#                 return "Yes"
#             else:
#                 return "No"
#         elif type(N_or_name) == str:
#             if N_or_name in self.channels:
#                 return "Yes"
#             else:
#                 return "No"

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel = 0

    def first_channel(self):
        self.current_channel = 0
        return self.channels[self.current_channel]

    def last_channel(self):
        self.current_channel = len(self.channels) - 1
        return self.channels[self.current_channel]

    def turn_channel(self, n):
        if n > len(self.channels) or n < 1:
            return "No"
        else:
            self.current_channel = n - 1
            return self.channels[self.current_channel]

    def next_channel(self):
        if self.current_channel == len(self.channels) - 1:
            self.current_channel = 0
            return self.channels[self.current_channel]
        else:
            self.current_channel += 1
            return self.channels[self.current_channel]

    def previous_channel(self):
        if self.current_channel == 0:
            self.current_channel = len(self.channels) - 1
            return self.channels[self.current_channel]
        else:
            self.current_channel -= 1
            return self.channels[self.current_channel]

    def current_channel(self):
        return self.channels[self.current_channel]

    def is_exist(self, n):
        if n in CHANNELS:
            return "Yes"
        else:
            return "No"
    def set_channel(self, n):
        if n > 100 or n < 1:
            raise ValueError("Channel not exist")
        else:
            self.current_channel = n - 1
            return self.current_channel
