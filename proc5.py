x1 = int(input("введите значение координаты х1 = "))
x2 = int(input("введите значение координаты х2 = "))
y1 = int(input("введите значение координаты y1 = "))
y2 = int(input("введите значение координаты y2 = "))
def RectPS(x1,x2,y1,y2):
    S = abs((x2 - x1) * (y2 - y1))
    P = (abs((x2 - x1) + (y2 - y1)))*2
    return S,P
print(RectPS(x1,x2,y1,y2))
