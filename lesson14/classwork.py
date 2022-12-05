def check_digits(fn):
    def wrapper(x):
        try:
            fn(x)
        except ValueError:
            print("Digit!")
        return fn(x)

    return wrapper


@check_digits
def myfunction():
    print("hello world!")
    return 20


try:
    assert myfunction() == "hello world!"
except ValueError:
    print("oops")