
# print() func to print anything on the console
print("Hello, Welcome to the python learning hub")

# user input with input() func
"""Below statement will prompt the user to enter their name & will display it on the conosle.
input() will consider the value entered by the user as string by default.
Though user feed numeric value as input, python will infer it as string.
Play with examples as needed to understand better. """
print("Your user name is: "+ input("Enter your user name: "))

# Variables in python are the entities which hold the values of various data types
x = input() # Here x is a variable which will hold.
print(x, type(x)) # Refer the input() comment for explaination

# Primitive data types
name = input("enter your name: ")
print(type(name)) # Variable name holds string type value

age = int(input("enter your age: "))
print(type(age)) # Variable age holds numeric value. Precisely integer

weight = float(input("enter your height in cms:"))
print(type(weight)) # Variable weight holds float(decimal) value

boolValue = bool(input("enter a boolean value: "))
print(type(boolValue)) # Variable boolValue holds boolean type value

# Exercise on strings
name = 'Srikanth Vadapalli'
print(name[:])
print(name[-9:])
print(name[:17])
print(name[-len(name)])
print("My name is '{:>9}'".format(name))
print(len(name)) # finds the length of the string
# Can use find() or index() to get the index of the substring 
print(name.find("S")) # find() will return -1 if the substring isn't found
print(name.index("S")) # index(0) will throw an error if the substring isn't found
print(name.upper()) # To print the value in the variable name in upper case
print(name.lower()) # To print the value in the variable name in lower case
print(name.title()) # # To print the value in the variable name with capital letter in every word
print(name.capitalize()) # To print the first word of the value in capital
print(name.replace('ka','n')) # It will replace the substring with the user desired substring
print(name.split()) # It will be used to split the string into list
print(name.strip()) # It will strip off the extra spaces which are present preceeding & succeeding 


# Excercise on List - []: List is a data type which is a collection of heterogeneous data
# List can be initiated in two ways - Applicable for Empty List 
firstList = [] # first way of initializing 
secondList = list() # second way of initializing
numList = [1,4,7,9,34,23,68,1256,4678]
strList = ['name', 'age', 'occupation', 'nation']
print(numList, strList)



# Sets in python 
set1 = {'srikanth', 'sameer', 'pranuthi', 'sherly', 'vaddi'}
set2 = {'vaddi','surya','ajay','soma'}
set3 = {'srikanth', 1} # Sets contain unordered non redundant heterogeneous data
print(set1, set2, set3)
set3.remove(1)
set3.add(35)
print(set3)
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.intersection(set2))
print(set1.union(set2))

'''Sets in python '''










