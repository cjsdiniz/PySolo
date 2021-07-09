# none
# Ex1
print(None)

# Ex2


def some_func():
    print("Hi!")


var = some_func()
print(var)

# Ex3
foo = print()
if foo == None:

    print(1)

else:

    print(2)

# Dictionaries
# 1
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

# 2
cars = {"BMW": "blue", "Volvo": "red"}
print(cars)

# 3
primary = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
}

# 4
print(primary["red"])
# print(primary["yellow"]) # Dá natural/ erro

# 5
test = {}
# print(test[0]) # KeyError: 0

# 6 - Erro TypeError: unhashable type: 'list'
# bad_dict = {
#     [1, 2, 3]: "one two three",
# }

# Dictionary Functions
print("\n# 1")
squares = {1: 1, 2: 4, 3: "error", 4: 16, }
squares[8] = 64
squares[3] = 9
print(squares)

print("\n# 2")
primes = {1: 2, 2: 3, 4: 7, 7: 17}
print(primes[primes[4]])

print("\n# 3")
nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)


print("\n# 4")
pairs = {1: "apple",
         "orange": [2, 3, 4],
         True: False,
         None: "True",
         }

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))


print("\n# 5")
fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))


print("\n# 6\n*** Tuples ***")
print("\n #1")
words = ("spam", "eggs", "sausages",)
print(words[0])
# Dá erro: words[1] = "cheese"

print("\n# 7\nOutra forma de criar tuplos:")
my_tuple = "one", "two", "three"
print(my_tuple[0])


print("\n# 8")
tuple = (1, (1, 2, 3))
print(tuple[1])

print("\n\n*** List Slices ***")
print("\n#1")
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

print("\n#2")
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64]
print(sqs[4:7])

print("\n#3")
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

print("\n#4")
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

print("\n#5")
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

print("\n#6")
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])

print("\n\n*** List Comprehensions ***")
# a list comprehension
print("\n#1")
cubes = [i**3 for i in range(5)]
print(cubes)

print("\n#2")
nums = [i*2 for i in range(10)]
print(nums)

print("\n#3")
evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

print("\n#4")
print("\neven = [2*i for i in range(10**100)] -> No output.")

print("\n\n*** String Formatting ***")
print("\n#1")
# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

print("\n#2")
print("{0}{1}{0}".format("abra", "cad"))

print("\n#3")
a = "{x}, {y}".format(x=5, y=12)
print(a)


print("\n#4")
str = "{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)


print("\n\n*** Useful Functions ***")
print("\n#1")
print(", ".join(["spam", "eggs", "ham"]))
# prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
# prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
# prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
# prints "['spam', 'eggs', 'ham']"

print("\n#2")
print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))

print("\n#3")
a = min([sum([11, 22]), max(abs(-30), 2)])
print(a)

print("\n#4")
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)


print("\n#5")
nums = [-1, 2, -3, 4, -5]
if all([abs(i) < 3 for i in nums]):
    print(1)
else:
    print(2)


print("\n\n***Text Analyzer***")
print("\n#1")
# filename = input("Enter a filename: ")
# filename = "/Users/cjdiniz/Tek/GitHub/PySolo/test.txt"
filename = "./test.txt"
with open(filename) as f:
    text = f.read()
print(text)


def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


print("\n#2")
print(count_char(text, "r"))

print("\n#3")
for char in "abcdefghijklmnopqrstuvwxyz":

    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))
