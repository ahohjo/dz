A = int(input("A ="))
B = int(input("B ="))
C = A

if A != B:
    A = A + B
    B = C + B
else:
    A = 0
    B = 0
print(A,B)
