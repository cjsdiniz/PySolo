text = input("Word: ")
dict = {}
# your code goes here
for c in text:
    n = text.count(c)
    dict[c] = n
print(dict)
