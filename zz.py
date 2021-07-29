class A:
    A = 1

    def __init__(self):
        self.a = 0


print(hasattr(A, 'a'))

import os
# os.mkdir('pic')
# os.chdir('pic')
# print(os.getcwd())
print(os.uname())

t = (1, 2, 3, 4)
t = t[-2:-1]
t = t[-1]
print(t)
# os.makedirs('pics/th')
# os.rmdir('th')


d = {}
d['2'] = [1, 2]
d['1'] = [3, 4]
for x in d.keys():
    print(d[x][1], end='')
