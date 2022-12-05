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
def censor_words(stop_words):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in stop_words:
                result = result.replace(word, '*')
            return result
        return wrapper
    return decorator

@censor_words(['bmw', 'pepsi'])
def sentence(name):
    return f"{name} drinks pepsi in his brand new BMW!"

print(sentence('John')) # John drinks * in his brand new *!