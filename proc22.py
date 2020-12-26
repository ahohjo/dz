A = int(input("A ="))
B = int(input("B ="))

print("Выберите нужное действие, где 1 - вычитание, 2 - умножение, 3 - деление, если будет выбрано число >3, то будет автоматическое сложение")

a = int(input("Действие?"))
if a == 1:
    rez = A - B
    print(rez)
elif a == 2:
    rez = A * B
    print(rez)
elif a == 3:
    rez = A // B
    print(rez)
else:
    if a > 3:
        rez = A + B
        print(rez)
    
