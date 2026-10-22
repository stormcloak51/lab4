from random import randint

n = randint(1, 100)
print(n)
flag = False
while not flag:
    x = int(input("Введите число: "))

    if x > n:
        print("больше")
    elif x < n:
        print("меньше")
    else:
        flag = True
        print("Угадал")
