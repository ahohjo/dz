import random
M = int(input('M ='))
matr = [[random.randrange(0,10) for y in range(M)] for x in range(M)]

for i in range(len(matr)):
    print([0 for j in range(i)]+ matr[i][i:])
