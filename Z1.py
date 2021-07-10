nums = list(range(5))
print(nums[4])
print(nums)
nums = list(range(20, 3, -3))
print(nums)

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

N = int(input("#: "))
# your code goes here
s = 0
for i in range(N):
    s += i
print(s+N)
