# txt = input()
txt = "this is an awesome text "
# your code goes here
words = txt.split(" ")
# print(words)

c = 0
i = 0
for w in words:
    if c < len(w):
        c = len(w)
        p = words[i]
    i += 1
print(p)
# print(p)
