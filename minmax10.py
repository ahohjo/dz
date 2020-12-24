from random import randint
N = int(input("введите число n: "))
numbers = []
for i in range(N+1):
    numbers.append(randint(-10,10))
a = numbers.sort()
b = numbers[N]
c = numbers[0]
print(numbers)
print("min =",c,"max =",b)
