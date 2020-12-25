N = int(input("N ="))
k = -1
r = 0
for i in range(1,N+1):
    k *= (-1)
    r += k*(1+0.1*i)
print(r)
