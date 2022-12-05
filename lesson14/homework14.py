from functools import wraps
#Task1
# def my_print_func():
#     def my_fun(x):
#         print("my_fun was called with the argument")
#         return x
#     return my_fun
# @my_print_func()
# def my_main(x):
#     return x
# my_main("Hello World!")
# print(type(my_main))
# print(type(my_print_func))
#TAsk2
# def censor_words(stop_words):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             for word in stop_words:
#                 result = result.replace(word, '*')
#             return result
#         return wrapper
#     return decorator
#
# @censor_words(['bmw', 'pepsi'])
# def sentence(name):
#     return f"{name} drinks pepsi in his brand new BMW!"
#
# print(sentence('John')) # John drinks * in his brand new *!

#Task3
def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if type(arg) != type_:
                    print('Argument type is not valid')
                    return False
                if len(arg) > max_length:
                    print('Argument length is too long')
                    return False
                if not all(x in arg for x in contains):
                    print('Argument does not contain required symbols')
                    return False
            return func(*args, **kwargs)
        return wrapper
    return decorator
@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
print(create_slogan('johndoe05@gmail.com'))