##############Task1
square = ()
cube = ()
funcs = {square: lambda x: x**2, cube: lambda x: x**3}
def get_square(value): return funcs[square](value)
def get_cube(value): return funcs[cube] (value)
print(get_square(5), get_cube(5))
##############Task2