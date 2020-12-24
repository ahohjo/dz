import random
M = int(input("M ="))

matrix = [[random.randrange(0,10) for y in range(M)] for x in range(M)]
for i in range(M):
    print (matrix[i])

summ = 0
for i in range(0,M):
    summ+=matrix[i][i]
print(summ)



