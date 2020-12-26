from random import randint
N = int(input("N ="))

nabor = [randint(-10,10) for i in range(N+1)]
print(nabor)

nabor.sort()
print(nabor)
print("max =",nabor[N],"min =",nabor[0])
