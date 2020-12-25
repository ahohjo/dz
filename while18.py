n = int(input("Введите число n:"))
print(n)
def func(n):
    k = 0
    summ = 0
    while n > 0:
        a = n%10
        summ += a
        k+=1
        n = n//10
    return k, summ
print(func(n))
