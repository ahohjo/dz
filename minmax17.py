from random import randint
n = int(input("введите число n:"))
a = []
for i in range(n+1):
    a.append(randint(-10,10))
b = a.sort()
print(a)
c = a.pop(n)
array = a
summ = 0
for i in range(len(array)):
    summ += array[i]
print(summ)

