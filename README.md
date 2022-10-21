# Python Task 1(L2):
print("Чтобы закончить вычисления введите STOP")
while True:
    sign = input('Введите знак (+;-;/; *):')
    if sign.lower() == "stop":
        break
    elif sign in '+-/*':
        a = float(input("Введите число 1: "))
        b = float(input("Введите число 2: "))
        if sign == "+":
            print("Итог: ", a+b)
        elif sign == "-":
            print("Итог: ", a-b)
        elif sign == "*":
            print("Итог: ",a*b)
        elif sign == "/":
            print("Итог: ", a/b)
        else:
            print("Вы ввели неверный знак!")
            
