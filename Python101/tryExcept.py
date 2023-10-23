"""Exception Handling in Python"""
try:
    1/0
except ZeroDivisionError:
    print("You cannot divide by zero!")

'''Bare except'''
# Bare except is to catch any and all exceptions. It is not recommended because we don't know what is the targe.
try:
    1/0
except:
    print("You cannot divide by zero!")

my_dict = {'a':1,'b':1,'c':3}
try:
    value = my_dict['d']
except KeyError:
    print("That key doesn't exist")

my_list = [1,2,3,4,5]
try:
    my_list[5]
except IndentationError:
    print("That index is not in the list")
