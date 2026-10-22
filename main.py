number = int(input("Введите число: "))

if number % 2 == 0:
    print(f"Число {number} - чётное")
else:
    print(f"Число {number} - нечётное")

# ==== ДОПОЛНИТЕЛЬНЫЕ ЗАДАНИЯ ======


if number % 3 == 0:
    print(f"Число {number} делится на 3")
else:
    print(f"Число {number} не делится на 3")

if number > 0:
    print(f"Число {number} - положительное")
elif number < 0:
    print(f"Число {number} - отрицательное")
else:
    print(f"Число {number} - ноль")
