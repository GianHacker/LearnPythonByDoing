""" top_100Lottery """
# Program is an example and exercise on usage of sets in python
from random import randint

n = int(input("Enter tha maximum range of winners from the pool: "))
result_set = set()
while n > 0:
    result_set.add(randint(1, 10000000))
    n = n - 1

print(result_set)

