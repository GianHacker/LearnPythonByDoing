
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
print(len(name)) # finds the length of the string
# Can use find() or index() to get the index of the substring 
print(name.find("S")) # find() will return -1 if the substring isn't found
print(name.index("S")) # index(0) will throw an error if the substring isn't found
print(name.upper()) # To print the value in the variable name in upper case
print(name.lower()) # To print the value in the variable name in lower case
print(name.title()) # # To print the value in the variable name with capital letter in every word
print(name.capitalize()) # To print the first word of the value in capital
print(name.replace('ka','n')) # It will replace the substring with the user desired substring
print(name.center()) 


kaliyug = 432000

print("Total human years in kaliyu: ",kaliyug)
print("# of human years in kaliyug 1st padam: ", kaliyug*0.4)
print("# of human years in kaliyug 2nd padam: ", kaliyug*0.3)
print("# of human years in kaliyug 3rd padam: ", kaliyug*0.2)
print("# of human years in kaliyug 4th padam: ", kaliyug*0.1)


mahaYug = 4320000
print("# of human years in Kritayugam: ",mahaYug*0.4)
print("# of human years in Tretayugam: ",mahaYug*0.3)
print("# of human years in Dwaparayugam: ", mahaYug*0.2)
print("# of human years in Kaliyugam: ", mahaYug*0.1)

print("# of human years in Manvantaram: ",mahaYug*71 )
print("# of human years in Kalpa: ", 14*(mahaYug*71))

