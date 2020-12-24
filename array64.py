from random import random
N1 = int(input("Введите число N1 ="))
N2 = int(input("Введите число N2 ="))
N3 = int(input("Введите число N3 ="))

A = []
B = []
C = []
D = []
for i in range(N1):
    a = int(random()*54)
    A.append(a)
    A = sorted(A, reverse=True)
for i in range(N2):
    b = int(random()*54)
    B.append(b)
    B = sorted(B, reverse=True)
for i in range(N3):
    c = int(random()*54)
    C.append(c)
    C = sorted(C, reverse=True)
print(A,B,C)

D = A + B + C
D = sorted(D, reverse=True)
print(D)
