# task 3
def decorate(filename:str):
    def input_func(func):
        def wrapper(name:str):
            with open(filename, 'w') as file:
                if name == name.capitalize():
                    file.write(name)
                else:
                    file.write('Bad type')
            return func(name)
        return wrapper
    return input_func

@decorate('file15.txt')
def write_name(name:str):
    return 'Hello ' + name + '!'


def main():
    print(write_name(input('Write your name: ')))

if __name__ == '__main__':
    main()