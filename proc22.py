A = float(input("введите A ="))
B = float(input("введите B ="))
print("1 - вычитание","2 - умножение","3 - деление","числа > 3 - сложение")
N = int(input("Введите желаемую операцию: "))

def Calc(N):
    if N == 1:
        return A - B
    if N == 2:
        return A * B
    if N == 3:
        return A / B
    if N > 3:
        return A + B
print(Calc(N))
