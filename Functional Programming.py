print("\n\n*** Functional Programming ***")
print("\n#1")


def apply_twice(func, arg):
    return func(func(arg))


def add_five(x):
    return x + 5


print(apply_twice(add_five, 10))


print("\n#2")


def test(func, arg):

    return func(func(arg))


def mult(x):
    return x * x


print(test(mult, 2))


print("\n\n*** Pure Functions ***")

print("\n#1")


def pure_function(x, y):

    temp = x + 2*y

    return temp / (2*x + y)


some_list = []


def impure(arg):

    some_list.append(arg)


print("\n\n*** Lambdas ***")
print("\n#1")


def my_func(f, arg):

    return f(arg)


print(my_func(lambda x: 2*x*x, 5))


print("\n#2")
# named function


def polynomial(x):
    return x**2 + 5*x + 4


print(polynomial(-4))

# lambda
print((lambda x: x**2 + 5*x + 4)(-4))

print("\n#3")
def double(x): return x * 2


print(double(7))

print("\n#4")
def triple(x): return x * 3


def add(x, y): return x + y


print(add(triple(3), 4))

# map
print("\n\n*** Map ***")

print("\n#1")


def add_five(x):
    return x + 5


nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)


print("\n#2")
nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x+5, nums))
print(result)


print("\n\n*** filter ***")
print("\n#1")
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)


print("\n#2")
nums = [1, 2, 5, 8, 3, 0, 7]
res = list(filter(lambda x: x < 5, nums))
print(res)
