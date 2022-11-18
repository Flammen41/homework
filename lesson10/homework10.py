###### Task1
# def oops(message):
#      raise Exception(message)
# oops('oops')
# def catch_oops(name):
#     try:
#         oops(name)
#     except Exception as e:
#         pass
# catch_oops('exceptions are fun')
## Task2
def math_square_division(a, b):
 try:
  num_a = int(input("Input numerator "))
  num_b = int(input("Input denominator"))
  blaba = num_a ** 2 / num_b
except TypeError: 
print("Invalid input or exception")
return blaba
print("Results of a squared divided by b", math_square_division(a, b))