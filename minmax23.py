from random import randint
N = int(input("N(>3)="))
a = [randint(-10,10) for i in range(N+1)]
print(a, a[N-1])

a.sort()
print(a)
print(a[N],a[N-1],a[N-2])
