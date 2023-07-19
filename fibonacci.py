n = int(input("Enter a number of your choice: "))
a , b = 0, 1
while a < n:
    print(a)
    a , b = b, a+b
