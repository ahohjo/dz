from random import random
N = int(input("Введите число N = "))
a = []
b = []
for i in range(N):
    c = int(random() * 50)
    a.append(c)
print(a)    
s = 0
for i in range(N-1,-1,-1):
     s +=  a[i]
     b.insert(0,s)
print(b)
