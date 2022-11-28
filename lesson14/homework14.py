#Task1
def my_print_func():
    def my_fun(x):
        print("my_fun was called with the argument")
        return x
    return my_fun
@my_print_func()
def my_main(x):
    return x
my_main("Hello World!")
print(type(my_main))
print(type(my_print_func))
#TAsk2
#Task3
