a, b, c = (
    float(input("Введите 1 число: ")),
    float(input("Введите 2 число: ")),
    float(input("Введите 3 число: ")),
)

if a >= b and a >= c:
    maxi = a
elif b >= a and b >= c:
    maxi = b
else:
    maxi = c

print(f"Максимум - {maxi}")

# ====== ДОПОЛНИТЕЛЬНО ======

print(f"Максимум - {max(a, b, c)}")
