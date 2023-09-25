if __name__ == "__main__":
    try:
        1/0
    except ZeroDivisionError:
        print("You cannot divide by zero!")

# Bare Except
# Bare except is not recommended since it will catch any and all exceptions
    try:
        1/0
    except:
        print("You cannot divide by zero.")

# Few more examples

my_dict = {'a': 1, 'b': 2, 'c': 3}
try:
    value = my_dict['d']
except KeyError:
    print('That key does not exist!')

my_list = [1,2,3,4,5]
try:
    my_list[6]
except IndexError:
    print('That index is not in the list')
