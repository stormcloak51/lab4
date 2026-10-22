try:
    N = int(input("Введите число в десятичной системе: "))
    binN = bin(N)[2:]
    octN = oct(N)[2:]
    hexN = hex(N)[2:]
    print(f"Число {N} в двоичной системе: {binN}")
    print(f"Число {N} в восьмеричной системе: {octN}")
    print(f"Число {N} в шестнадцатеричной системе: {hexN}")
except ValueError:
    print("Введите корректное число")
