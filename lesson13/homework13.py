# #####Task1
# def count_variables():
#     x = 1
#     y = 2
#     z = 3
#     str1= "blablablablablablablablablablablabl"
#     str2= "get_locals"
#
# print(count_variables.__code__.co_nlocals)
# #####Task2
# def inner():
#     while True:
#         print('inside')
# def outer():
#     return inner
#     print('main')
# a = outer()
# print(a())  # prints inside
# def foo():
#     def bar():
#         print("hello world")
#     return bar
# f = foo()
# f()
################################################################
#Task3
nums1 = [1, -2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
def choose_func(nums: list, func1, func2):
    if (all(num > 0 for num in nums)):
        return ([num ** 2 for num in nums] * 0) + func1(nums)
    else:
        return func2(nums)
def square_nums(nums):
    return [num ** 2 for num in nums]
def remove_negatives(nums):
    return [num for num in nums if num > 0]

#assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]