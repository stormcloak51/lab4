x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))

if x == y == 0:
    print("В начале отсчета")
elif x == 0:
    print("На оси ординат")
elif y == 0:
    print("На оси абсцисс")
elif x > 0:
    if y > 0:
        print("В первой четверти")
    elif y < 0:
        print("В четвертой четверти")
else:
    if y > 0:
        print("Во второй четверти")
    elif y < 0:
        print("В третьей четверти")
