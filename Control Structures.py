#Booleans & Comparisons
my_boolean = True
print(my_boolean)
print(2 == 3)
print("hello" == "hello")

#Booleans & Comparisons
print(1 != 1)
print("eleven" != "seven")
print(2 != 10)

print(7 <= 8)
print(9 >= 9.0)

# if Statements
if 10 > 5:
    print("10 greater than 5")
print("Program ended")

spam = 7
if spam > 5:
    print("five")

if spam > 8:
    print("eight")

# else Statements
x = 4
if x == 5:
    print("Yes")
else:
    print("No")

if 1 + 1 == 2:
    if 2 * 2 == 8:
        print("if")
    else:
        print("else")


num = 3
if num == 1:
    print("One")
else:
    if num == 2:
        print("Two")
    else:
        if num == 3:
            print("Three")
        else:
            print("Something else")

num = 3
if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
else:
    print("Something else")

print(1 == 1 and 2 == 2)
print(1 == 1 and 2 == 3)
print(1 != 1 and 2 == 2)
print(2 < 1 and 3 > 6)

print(1 == 1 or 2 == 2)
print(1 == 1 or 2 == 3)
print(1 != 1 or 2 == 2)
print(2 < 1 or 3 > 6)

print(not 1 == 1)
print(not 1 > 7)

if not True:
    print("1")
elif not (1 + 1 == 3):
    print("2")
else:
    print("3")

# Multiple Operators & Conditions
print(False == False or True)
print(False == (False or True))
print((False == False) or True)

if 1 + 1 * 3 == 6:
    print("Yes")
else:
    print("No")

grade = 88
if(grade >= 70 and grade <= 100):
    print("Passed!")

x = 4
y = 2
if not 1 + 1 == y or x == 4 and 7 == 8:
    print("Yes")
elif x > y:
    print("No")

# Lists
words = ["Hello", "world", "!"]

words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

nums = [5, 4, 3, 2, 1]
print(nums[1])

nums = [5, 4, 3, 2, 1]
print(nums[1])

empty_list = []
print(empty_list)

number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])

str = "Hello world!"
print(str[6])


num = [5, 4, 3, [2], 1]
print(num[0])
print(num[3][0])
# print(num[5]) -> IndexError: list index out of range

# List Operations
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]
print(nums[3])

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

nums = [10, 9, 8, 7, 6, 5]

nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

# List Functions
nums = [1, 2, 3]
nums.append(4)
print(nums)

words = ["hello"]
words.append("world")
print(words[1])

nums = [1, 3, 5, 2, 4]
print(len(nums))

letters = ["a", "b", "c"]
letters.append("d")
print(len(letters))

words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)

nums = [9, 8, 7, 6, 5]
nums.append(4)
nums.insert(2, 11)
print(len(nums))

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
# print(letters.index('z')) -> ValueError: 'z' is not in list

# while Loops
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Finished!")

i = 3
while i >= 0:
    print(i)
    i = i - 1

x = 1
while x < 10:
    if x % 2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")
    x += 1

i = 0
while 1 == 1:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break
print("Finished")

i = 5
while True:
    print(i)
    i = i - 1
    if i <= 2:
        break

i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 3:
        print("Skipping 3")
        continue
# for Loops
words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")

str = "testing for loops"
count = 0
for x in str:
    if(x == 't'):
        count += 1
print(count)

list = [2, 3, 4, 5, 6, 7]
for x in list:
    if(x % 2 == 1 and x > 4):
        print(x)
        break

# Range
numbers = list(range(10))
print(numbers)

nums = list(range(5))
print(nums[4])

numbers = list(range(3, 8))
print(numbers)
print(range(20) == range(0, 20))

nums = list(range(5, 8))
print(len(nums))

numbers = list(range(5, 20, 2))
print(numbers)

nums = list(range(3, 15, 3))
print(nums[2])
