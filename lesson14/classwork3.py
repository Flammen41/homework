from functools import wraps
from time import time, sleep
# def digit_decorator(function):
#     @wraps(function)
#     def wrapper(x):
#         try:
#             if x.isdigit() is True:
#                 print('digit')
#             else:
#                 raise Exception
#         except:
#             print('Wrong value')
#     return wrapper
# @digit_decorator
# def take_digit(x):
#     print(x)
# x = input("Enter a digit ")
# take_digit(x)
################################################################
def lower_letter_decorator(fn):
    def wrapper():
        x = fn()
        print(x.lower())
        return x
    return wrapper
def upper_letter_decorator(fn):
    def wrapper():
        x = fn()
        print(x.upper())
    return wrapper
def measure_time(func):
    def wrapper():
        n = time()
        func()
        sleep(2)
        print(time() - n)
    return wrapper
@measure_time
@upper_letter_decorator
@lower_letter_decorator
def my_func():
    return "Hello World!"
my_func()
################################################################
# from functools import wraps
# def print_func(func):
#     # @wraps(func)
#     def wrapper():
#         print('Hello ' + func.__name__)
#         func()
#     return wrapper
#
# @print_func
# def test_func():
#     print('inside function')
#
# test_func()
