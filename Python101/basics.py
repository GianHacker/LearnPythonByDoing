from random import randint

limit = int(input("Enter the range: "))
nl = []
while limit > 0:
    nl.append(randint(1,limit))
    limit -= 1

print(nl)
nl.sort()
print(nl)

# print(dir('a'))
# print(help('a'.center())) 
# print('SRIKANT'.casefold()) # casefold() method converts non ASCII also into small case unlike lower() method
