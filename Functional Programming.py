from itertools import product, permutations
from itertools import takewhile
from itertools import accumulate, takewhile
from itertools import count
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

print("\n\n*** generators ***")
print("\n#1")


def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1


for i in countdown():
    print(i)

print("\n\n*** Recursion ***")
print("\n#1")


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


print(factorial(5))


print("\n#2")


def fib(x):

    if x == 0 or x == 1:

        return 1

    else:

        return fib(x-1) + fib(x-2)


print(fib(4))

print("\n\n*** sets ***")
print("\n#1")
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)


print("\n#2")
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)


print("\n#3")
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

print("\n\n*** itertools ***")
print("\n#1")
for i in count(3):
    print(i)
    if i >= 11:
        break

print("\n#2")

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))

print("\n#3")
nums = [2, 4, 6, 7, 9, 8]
a = takewhile(lambda x: x % 2 == 0, nums)
print(list(a))

print("\n#4")
letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

print("\n#5")
a = {1, 2}

print(len(list(product(range(3), a))))

print("\n\n*** M7 Quiz ***")
print("\n#1")
nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))


print("\n#2")


def power(x, y):

    if y == 0:

        return 1

    else:

        return x * power(x, y-1)


print(power(2, 3))


print("\n *** fibonacci ***")

num = int(input("Num: "))


def fibonacci(n):
    # complete the recursive function
    if n == 0 or n == 1:

        print(1)
        return 1

    else:
        print(n)
        #  return fibonacci(n-1) + fibonacci(n-2)
        return n-fibonacci(n-1)


fibonacci(num)

a = int(input('Give amount: '))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for x in fib(a):
    print(x)
