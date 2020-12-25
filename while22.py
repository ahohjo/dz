N = int(input("N = "))

def numb(N):
    d = 2
    while N % d !=0:
        d += 1
    return d == N
print(numb(N))
