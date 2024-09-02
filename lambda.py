# x = lambda a, b, c : a+b+c
# print(x(5,5,5))

# def myfunc(n):
#     return lambda a:a*n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))


# x = lambda a, b : a - b
# print(x(5, 3))

names = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank"]
filter_name = list(filter(lambda name : len(name) >=5, names))

print(filter_name)
