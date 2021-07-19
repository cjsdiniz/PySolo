def spell(txt):
    # your code goes here
    l = []
    for c in txt:
        l.insert(0, c)
    for w in l:
        print(w)


txt = input()
spell(txt)
