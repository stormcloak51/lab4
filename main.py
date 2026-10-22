height = float(input("Введите рост (м): "))
weight = float(input("Введите вес (кг): "))

imt = weight / (height**2)
print(f"ИМТ: {imt:.1f}")

if imt < 18.5:
    print("Недостаточный вес")
elif imt < 25:
    print("Норма")
elif imt < 30:
    print("Избыточный вес")
else:
    print("Ожирение")
