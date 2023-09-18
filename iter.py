# x = {1,2,3,4}
# s = iter(x)
# print(next(s))
# print(next(s))

# x = [6,3,1]
# g = (i**2 for i in x)
# print(next(g))


# def gen_fun():
#     x = [6,3,1]
#     for i in x:
#         yield i**2

# x = gen_fun()
# y = next(x)
# print(y)

nl = 'Srikanth Vadapalli'
s = " "
print(nl)
for i in nl:
    if i in s:
        nl.remove(i)
    else:
        continue
print(nl)

