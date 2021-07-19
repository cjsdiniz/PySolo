file = open("books.txt", "r")

# your code goes here
with file as f:
    for line in file:
        lst = line.split()
        enc = ""
        for w in lst:
            enc += w[:1]
        print(enc)
file.close()
